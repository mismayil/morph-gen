import json

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

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def write_json(data, path, ensure_ascii=True, indent=4):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)

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