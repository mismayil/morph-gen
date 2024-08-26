from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# model_id = "ytu-ce-cosmos/Turkish-Llama-8b-Instruct-v0.1"
model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
cache_dir = "/mnt/nlpdata1/home/ismayilz/.cache/huggingface/hub"

tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    cache_dir=cache_dir
)

print("Model loaded")

# messages = [
#     {"role": "user", "content": "Size Türkçe bir kök, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Sadece Evet veya Hayır ile cevap verin.\n\nÖrnek 1:\nKök: kayıt\nEkler: sız\nTüretilmiş kelime: kayıtsız\nCevap: Evet\n\nÖrnek 2:\nKök: sohbet\nEkler: ler\nTüretilmiş kelime: sohbetler\nCevap:"},
# ]

messages = [
    {"role": "user", "content": "tell me a joke"},
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

terminators = [
    tokenizer.eos_token_id,
    tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = model.generate(
    input_ids,
    max_new_tokens=40,
    eos_token_id=terminators,
    do_sample=False,
    temperature=0,
    top_p=1,
)
response = outputs[0][input_ids.shape[-1]:]
print(outputs[0])
print(tokenizer.decode(response, skip_special_tokens=True))