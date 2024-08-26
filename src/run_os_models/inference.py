import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed
from tqdm import tqdm
from torch.utils.data import DataLoader
import argparse
from datasets import Dataset
import torch
from transformers import set_seed
import vllm
import json


device = "cuda:0" if torch.cuda.is_available() else "cpu"


def run_vllm(client, 
             tokenizer, 
             prompt, 
             stop_seq, 
             max_new_tokens=1024, 
             cot=False, 
             temperature=0.0):
    """
    Generates a single output for a given input prompt using the VLLM backend (offline mode).
    Returns the output text.

    Reference:

    :param client: vllm.LLM, the LLM offline generation engine to use for querying the VLLM backend
    :param tokenizer: transformers.PreTrainedTokenizer, the tokenizer to use for inference
    :param prompt: str, the prompt to generate from
    :param stop_seq: list, the stop sequence to use for generation
    :param max_new_tokens: int, the maximum number of tokens to generate
    :param cot: bool, whether to use chain-or-thought or not
    :param temperature: float, the temperature to use for sampling
    """

    response = client.generate(prompt, sampling_params=vllm.SamplingParams(
        # See https://github.com/vllm-project/vllm/blob/main/vllm/sampling_params.py
        best_of=1,
        presence_penalty=0.0,
        frequency_penalty=1.0,
        top_k=-1,
        top_p=1.0,
        temperature=temperature,
        stop=stop_seq,
        use_beam_search=False,
        max_tokens=max_new_tokens,
        logprobs=5
    ))

    def top_answer(logprob):
        top_token = max(logprob, key=logprob.get)
        output_text = tokenizer.decode(top_token, skip_special_tokens=True)
        return output_text

    if len(response) > 0:
        return [r.outputs[0].text for r in response]

    if not cot:
        return top_answer(response[0].outputs[0].logprobs[0])
    else:
        return response[0].outputs[0].text


def get_tokenizer_params(tokenizer, 
                         target, 
                         shots=0, 
                         cot=False):
    """
    Determines the maximum number of tokens to generate for a given prompt and target.
    Also determines the stop sequence to use for generation.

    :param tokenizer: transformers.PreTrainedTokenizer, the tokenizer to use for inference
    :param target: str, the target to generate
    :param shots: int, the number of shots to use for few-shot learning
    :param cot: bool, whether to use chain-or-thought or not
    :param task_type: str, the type of answer to generate (mcq or open)
    """
    stop_seq = ["###"]
    if tokenizer.eos_token is not None:
        stop_seq.append(tokenizer.eos_token)
    if tokenizer.pad_token is not None:
        stop_seq.append(tokenizer.pad_token)

    if cot:
        max_new_tokens = 1024
    else:
        max_new_tokens = len(tokenizer(target, add_special_tokens=False)['input_ids'])
        if shots > 0:
            max_new_tokens += 8

    return max_new_tokens, stop_seq


def run_infer(tokenizer,
              data_loader,
              model_checkpoint,
              token):
    """
    Runs inference on a benchmark and stores generations in a pd.DataFrame.

    :param data_loader: transformers DataLoader, the batched dataset to run inference on
    :param token: str, the hf access token
    return: pd.DataFrame, a DataFrame containing the scores for each answer
    """

    model = AutoModelForCausalLM.from_pretrained(model_checkpoint, use_auth_token=token).to(device)
    print(f'Loaded model \n\tfrom checkpoint: {model_checkpoint}')
    
    preds = list()
    for batch in tqdm(data_loader, 
                      total=len(data_loader), 
                      position=0, 
                      leave=True):
        model_inputs = tokenizer(batch['prompt'], return_tensors="pt", padding=True).to(device)

        generated_ids = model.generate(**model_inputs, max_new_tokens=100)
        outputs = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)

        preds = preds + outputs

    # return predictions
    return preds


def run_vllm_infer(tokenizer,
                   data_loader, 
                   model_checkpoint,
                   max_len,
                   stop_seq,
                   temperature,
                   cot=False):
    """
    :param data_loader: HuggingFace Dataset, the dataset to run inference on
    """
    kwargs = {
        "model": model_checkpoint,
        "tokenizer": model_checkpoint,
        "trust_remote_code": True,
        "max_num_seqs": 1024,
        # "tensor_parallel_size": torch.cuda.device_count(),
        "tensor_parallel_size": 4
    }

    client = vllm.LLM(**kwargs, dtype='float16')

    predictions = list()
    for batch in tqdm(data_loader, 
                      total=len(data_loader), 
                      position=0, 
                      leave=True):
        
        outputs = run_vllm(client=client, 
                           tokenizer=tokenizer,
                           prompt=batch['prompt'], 
                           max_new_tokens=max_len,
                           stop_seq=stop_seq, 
                           cot=cot, 
                           temperature=temperature)
        
        predictions = predictions + outputs

    return predictions


def print_settings(model_checkpoint, cot, fs, 
                   input_file_name, output_file_name, token,
                   max_len, stop_seq, shots, batch_size, temperature):
    print('-'*50)
    print('INFERENCE SETTINGS')
    print('-'*50)
    print('Model checkpoint'.ljust(20) + '{}'.format(model_checkpoint))
    print('CoT'.ljust(20) + '{}'.format('Yes' if cot else 'No'))
    print('Few-shot'.ljust(20) + '{}'.format('Yes' if fs else 'No'))
    print('Access token'.ljust(20) + '{}'.format(token))
    print('-'*50)
    print('Input data file'.ljust(20) + '{}'.format(input_file_name))
    print('Output data file'.ljust(20) + '{}'.format(output_file_name))
    print('-'*50)
    print('Max sequence length'.ljust(20) + '{}'.format(max_len))
    print('Stop sequence'.ljust(20) + '{}'.format(stop_seq))
    print('Number of shots'.ljust(20) + '{}'.format(shots))
    print('Batch size'.ljust(20) + '{}'.format(batch_size))
    print('Temperature '.ljust(20) + '{}'.format(temperature))
    print('-'*50)


def main(input_file, output_file,
         model_checkpoint, 
         token,
         cot, 
         fs,
         seed=1234):
    """
    It runs the inference pipeline.
    
    :param model_checkpoint: str, the name of the model to be run
    :param token: str, the access right token
    """
    set_seed(seed)
    batch_size = 3
    temperature = 0.8 if cot else 0.0

    # read data
    data_json = json.load(open(input_file))
    data = pd.DataFrame(data_json['data'])[['prompt', 'reference']]
    print('Loaded inference data with columns: {}'.format(data.columns))

    ds = Dataset.from_pandas(data)
    data_loader = DataLoader(ds, batch_size=64, shuffle=True)
    
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, use_auth_token=token, padding_side='left')
    print(f'Loaded tokenizer \n\tfrom checkpoint: {model_checkpoint}')
    
    max_len, stop_seq = get_tokenizer_params(tokenizer, 
                                            ds['reference'],
                                            shots= fs,
                                            cot=cot)

    print_settings(model_checkpoint, cot, fs, 
                   input_file, output_file, token,
                   max_len, stop_seq, fs, batch_size, temperature)
    
    print(f'Running inference for {len(data)} samples')
    if 'llama' in model_checkpoint or 'mistral' in model_checkpoint:
        predictions = run_vllm_infer(tokenizer=tokenizer,
                                     data_loader = data_loader,
                                     model_checkpoint=model_checkpoint, 
                                     max_len=max_len,
                                     stop_seq=stop_seq,
                                     temperature=temperature,
                                     cot=cot)   
    else:
        predictions = run_infer(tokenizer=tokenizer,
                                data_loader=data_loader, 
                                model_checkpoint=model_checkpoint, 
                                token=token)

    # store data
    data['output'] = predictions
    data.to_json(output_file, orient='records')
    print('Output file stored.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input',
                        help='Data file path.',
                        default='')
    parser.add_argument('-o', '--output',
                        help='Output data file path.',
                        default='')
    parser.add_argument('-m', '--model',
                        help='Model to run inference.',
                        default='facebook/xglm-564M')
    parser.add_argument('-c', '--cot',
                        help='Adding CoT to the prompt or not.',
                        action='store_true')
    parser.add_argument('-f', '--fs',
                        help='Adding CoT to the prompt or not.',
                        action='store_true')
    parser.add_argument('-t', '--token',
                        help='Access token')

    args = parser.parse_args()

    main(input_file=args.input, 
         output_file=args.output,
         model_checkpoint=args.model, 
         token=args.token,
         cot=args.cot,
         fs=args.fs)
