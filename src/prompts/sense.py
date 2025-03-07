########################################## Prompt templates in English ##########################################
MORPH_GEN_SENSE_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of affixes (separated by comma) and a definition in {language} and your task is to generate a word that fits the given definition by using all the given affixes. You are allowed to use only the given affixes and each affix only once. Answer with only the generated word."

MORPH_GEN_SENSE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Affixes: {affixes}
Definition: {target_definition}
Answer: {answer}"""

MORPH_DISC_SENSE_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of affixes (separated by comma), a definition and a word in {language} that is derived from the given word root using the given affixes. Your task is to determine whether the derived word fits the given definition. Answer only with Yes or No."

MORPH_DISC_SENSE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Affixes: {affixes}
Definition: {target_definition}
Derived word: {derived_word}
Answer: {answer}"""

MORPH_GEN_NONCE_SENSE_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of affixes (separated by comma) and a target word definition in {language} and your task is to generate a word that fits the given target definition by using all the given affixes. You are allowed to use only the given affixes and each affix only once. Answer with only the generated word."

MORPH_GEN_NONCE_SENSE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root} (definition: {root_definition})
Affixes: {affixes}
Target definition: {target_definition}
Answer: {answer}"""

MORPH_DISC_NONCE_SENSE_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of affixes (separated by comma), a target word definition and a word in {language} that is derived from the given word root using the given affixes. Your task is to determine whether the derived word fits the given target definition. Answer only with Yes or No."

MORPH_DISC_NONCE_SENSE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root} (definition: {root_definition})
Affixes: {affixes}
Target definition: {target_definition}
Derived word: {derived_word}
Answer: {answer}"""
####################################################################################