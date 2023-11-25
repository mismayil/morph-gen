from itertools import product

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
                break

    return valid_decompositions