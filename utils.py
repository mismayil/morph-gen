import json
import tiktoken
import uuid
import os

from turkish_morphology import decompose, analyze

TURKISH_MORPH_MAP = {
    "A": ["", "a", "e"],
    "H": ["", "ı", "i", "u", "ü"],
    "D": ["d", "t"],
    "N": ["", "n"],
    "Y": ["", "y"],
    "S": ["", "s"],
    "C": ["c", "ç"],
    "E": ["e", "i"],
}

MODEL_COSTS = {
    "gpt-3.5-turbo": {'input': 0.0000015, 'output': 0.000002},
    "gpt-4": {'input': 0.00003, 'output': 0.00006},
    "text-davinci-003": {'input': 0.00002, 'output': 0.00002},
}

MODEL_ENCODINGS = {
    "gpt-3.5-turbo": "cl100k_base",
    "gpt-4": "cl100k_base",
    "text-davinci-003": "p50k_base"
}

POS_MAP = {
    "N": "noun",
    "V": "verb",
    "Adj": "adjective",
    "Adv": "adverb",
    "Conj": "conjunction",
    "Pron": "pronoun",
    "Postp": "postposition",
    "Det": "determiner"
}

def num_tokens_from_string(text, model):
    encoding_name = MODEL_ENCODINGS[model]
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(text))
    return num_tokens

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def write_json(data, path, ensure_ascii=True, indent=4):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)

def generate_unique_id():
    return str(uuid.uuid4()).split("-")[-1]

def find_json_files(directory):
    json_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))
    return json_files

def get_morphemes(word, analysis_index=-1):
    analyses = analyze.surface_form(word, use_proper_feature=False)
    
    if analysis_index >= len(analyses):
        analysis_index = -1

    if not analyses:
        return []

    decomposition = decompose.human_readable_analysis(analyses[analysis_index])

    morphemes = []

    for ig in decomposition.ig:
        root = getattr(ig, "root")
        if root:
            morpheme = root.morpheme
            if morpheme:
                morphemes.append(morpheme)

        if hasattr(ig, "derivation"):
            morpheme = getattr(ig.derivation, "meta_morpheme")
            if morpheme:
                morphemes.append(morpheme)

        if hasattr(ig, "inflection"):
            for inflection in ig.inflection:
                morpheme = getattr(inflection, "meta_morpheme")
                if morpheme:
                    morphemes.append(morpheme)

    return morphemes

def get_morphemes_from_sentence(sentence, analysis_index=-1):
    sentence_morphemes = []
    for word in sentence.split():
        morphemes = get_morphemes(word, analysis_index=analysis_index)
        sentence_morphemes.append({
            "word": word,
            "morphemes": morphemes
        })
    return sentence_morphemes