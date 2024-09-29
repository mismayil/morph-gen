##################################### Prompt templates in English #####################################
MORPH_DISC_NO_AFFIX_EN_INSTRUCTION_TEMPLATE = "You are given a word root and a word in {language} that is derived from the given word root. Your task is to determine whether the derived word is grammatically correct. Answer only with Yes or No."

MORPH_DISC_NO_AFFIX_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Derived word: {derived_word}
Answer: {answer}"""

MORPH_DISC_NONCE_NO_AFFIX_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition and a word in {language} that is derived from the given word root. Your task is to determine whether the derived word is grammatically correct. Answer only with Yes or No."

MORPH_DISC_NONCE_NO_AFFIX_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Derived word: {derived_word}
Answer: {answer}"""
############################################################################################
