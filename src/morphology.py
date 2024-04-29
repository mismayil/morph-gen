import random
from itertools import product
import tiktoken

from turkish_morphology import decompose, analyze
from utils import MODEL_ENCODINGS, levenshtein_distance

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

class Decomposition:
    def __init__(self, root, pos, meta_morphemes, morphemes=None):
        self.root = root
        self.pos = pos
        self.meta_morphemes = meta_morphemes
        self.morphemes = morphemes

    def __repr__(self):
        return f"Decomposition(root={self.root}, pos={self.pos}, meta_morphemes={self.meta_morphemes}, morphemes={self.morphemes})"

    def __str__(self):
        return f"{self.root} + {self.meta_decomposition} = {self.decomposition}" 
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Decomposition):
            return False
        return self.root == other.root and self.meta_morphemes == other.meta_morphemes

    def __hash__(self) -> int:
        return hash((self.root, tuple(self.meta_morphemes)))

    def to_json(self):
        return {
            "root": self.root,
            "pos": self.pos,
            "meta_morphemes": self.meta_morphemes,
            "morphemes": self.morphemes,
        }

def decompose_from_analysis_tr(analysis):
    decomposition = decompose.human_readable_analysis(analysis)

    morphemes = []
    root = None
    pos = None

    for ig in decomposition.ig:
        root_obj = getattr(ig, "root")
        if root_obj and root_obj.morpheme:
            root = root_obj.morpheme

        if getattr(ig, "pos"):
            pos = getattr(ig, "pos")

        if hasattr(ig, "derivation"):
            morpheme = getattr(ig.derivation, "meta_morpheme")
            if morpheme:
                morphemes.append(morpheme)

        if hasattr(ig, "inflection"):
            for inflection in ig.inflection:
                morpheme = getattr(inflection, "meta_morpheme")
                if morpheme:
                    morphemes.append(morpheme)

    return Decomposition(root=root, pos=pos, meta_morphemes=morphemes)

def surface_tr(morpheme):
    char_sets = []
    
    for i, char in enumerate(morpheme):
        char_set = TURKISH_MORPH_MAP.get(char, [char.lower()])
        if i == len(morpheme) - 1 and char == "k":
            char_set.append("ğ")
        char_sets.append(char_set)

    return ["".join(char_set) for char_set in list(product(*char_sets))]

def decompose_tr(word):
    analyses = analyze.surface_form(word, use_proper_feature=False)

    if not analyses:
        return []

    decompositions = set()

    for analysis in analyses:
        decomposition = decompose_from_analysis_tr(analysis)
        if decomposition:
            decompositions.add(decomposition)
    
    valid_decompositions = []

    for decomposition in decompositions:
        root = decomposition.root
        surface_decompositions = [[root]]

        for morpheme in decomposition.meta_morphemes:
            surface_forms = surface_tr(morpheme)
            surface_decompositions.append(surface_forms)

        surface_combinations = list(product(*surface_decompositions))

        for surface_combination in surface_combinations:
            surface_form = "".join(surface_combination)
            if surface_form == word:
                decomposition.morphemes = list(surface_combination[1:])
                valid_decompositions.append(decomposition)

    return valid_decompositions

def generate_nonce_word_tr(word):
    word = word.lower()

    hard_vowels = ["a", "ı", "o", "u"]
    soft_vowels = ["e", "i", "ö", "ü"]
    consonants = ["b", "c", "ç", "d", "f", "g", "ğ", "h", "j", "k", "l", "m", "n", "p", "r", "s", "ş", "t", "v", "y", "z"]

    last_vowel_index = None

    for i, char in enumerate(word):
        if char in hard_vowels or char in soft_vowels:
            last_vowel_index = i
    
    immutable_part = word[last_vowel_index:]
    mutable_part = word[:last_vowel_index]

    if not mutable_part:
        prefix = ""
        for i in range(3):
            if i % 2 == 0:
                prefix += random.choice(consonants)
            else:
                prefix += random.choice(soft_vowels) if immutable_part[0] in soft_vowels else random.choice(hard_vowels)
    else:
        prefix = ""

        for char in mutable_part:
            if char in hard_vowels:
                prefix += random.choice(list(set(hard_vowels)-set([char])))
            elif char in soft_vowels:
                prefix += random.choice(list(set(soft_vowels)-set([char])))
            else:
                prefix += random.choice(consonants)
    
    nonce_word = prefix + immutable_part
    return nonce_word

def generate_nonce_word_en(word):
    word = word.lower()

    hard_vowels = ["a", "o", "u"]
    soft_vowels = ["e", "i"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w", "y", "z"]

    last_vowel_index = None

    for i, char in enumerate(word):
        if char in hard_vowels or char in soft_vowels:
            last_vowel_index = i
    
    immutable_part = word[last_vowel_index:]
    mutable_part = word[:last_vowel_index]

    if not mutable_part:
        prefix = ""
        for i in range(3):
            if i % 2 == 0:
                prefix += random.choice(consonants)
            else:
                prefix += random.choice(soft_vowels) if immutable_part[0] in soft_vowels else random.choice(hard_vowels)
    else:
        prefix = ""

        for char in mutable_part:
            if char in hard_vowels:
                prefix += random.choice(list(set(hard_vowels)-set([char])))
            elif char in soft_vowels:
                prefix += random.choice(list(set(soft_vowels)-set([char])))
            else:
                prefix += random.choice(consonants)
    
    nonce_word = prefix + immutable_part
    return nonce_word

def segment_by_tokenizer(text, model, root, return_tokens=False):
    encoding_name = MODEL_ENCODINGS[model]
    encoding = tiktoken.get_encoding(encoding_name)
    encodings = encoding.encode(text)
    tokens = [encoding.decode_single_token_bytes(enc).decode("utf-8") for enc in encodings]
    root_end_idx = 0
    best_diff = len(root)

    for i in range(len(tokens)):
        cand_root = "".join(tokens[:i+1])
        root_diff = levenshtein_distance(cand_root, root)
        if root_diff < best_diff:
            root_end_idx = i+1
            best_diff = root_diff
    
    segmentation = ["".join(tokens[:root_end_idx])] + tokens[root_end_idx:]

    if len(segmentation) == 1:
        segmentation = tokens

    if return_tokens:
        return segmentation, tokens
    
    return segmentation

def filter_decompositions_tr(word, decompositions):
    valid_decompositions = []

    for decomposition in decompositions:
        if not decomposition["meta_morphemes"]:
            continue
        
        morpheme_tuples = [(decomposition["meta_morphemes"][i], decomposition["meta_morphemes"][i+1]) for i in range(len(decomposition["meta_morphemes"])-1)]
        morpheme_triples = [(decomposition["meta_morphemes"][i], decomposition["meta_morphemes"][i+1], decomposition["meta_morphemes"][i+2]) for i in range(len(decomposition["meta_morphemes"])-2)]

        if "s" in decomposition["morphemes"]:
            s_index = decomposition["morphemes"].index("s")
            meta_s = decomposition["meta_morphemes"][s_index]
            if meta_s == "sH" or meta_s == "SH":
                continue
        
        if "lArH" in decomposition["meta_morphemes"]:
            continue
        
        if ("lAr", "Hm", "YHz") in morpheme_triples or ("lAr", "Hn", "YHz") in morpheme_triples:
            alt_la = any([("HmHz" in decomp["meta_morphemes"] or "HnHz" in decomp["meta_morphemes"]) for decomp in decompositions])
            if alt_la:
                continue

        if ("lA", "Hr") in morpheme_tuples or ("lA", "Hn") in morpheme_tuples or ("lA", "Hş") in morpheme_tuples:
            alt_la = any([("lAr" in decomp["meta_morphemes"] or "lAn" in decomp["meta_morphemes"] or "lAş" in decomp["meta_morphemes"]) for decomp in decompositions])
            if alt_la:
                continue
        
        for decomp in valid_decompositions:
            if decomp["root"] == decomposition["root"] and decomp["pos"] == decomposition["pos"] and decomp["morphemes"] == decomposition["morphemes"] and decomp["meta_morphemes"] == decomposition["meta_morphemes"]:
                continue

        valid_decompositions.append(decomposition)
    
    return valid_decompositions