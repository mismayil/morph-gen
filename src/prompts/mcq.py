########################### Prompt templates in English ###########################
#### Default
MORPH_DISC_MCQ_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of affixes (separated by comma) and a list of words in {language} that are derived from the given word root using the given affixes. Your task is to select the grammatically correct option. Output only the correct option number."

MORPH_DISC_MCQ_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Affixes: {affixes}
Options:
{options}
Answer: {answer}"""

MORPH_DISC_MCQ_NONCE_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of affixes (separated by comma) and a list of words in {language} that are derived from the given word root using the given affixes. Your task is to select the grammatically correct option. Output only the correct option number."

MORPH_DISC_MCQ_NONCE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Affixes: {affixes}
Options:
{options}
Answer: {answer}"""

#### Sentence
MORPH_DISC_SENT_MCQ_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of affixes (separated by comma), a sentence with a blank (___) and a list of words in {language} that are derived from the given word root using the given affixes. Your task is to fill in the blank by selecting the grammatically correct option. Output only the correct option number."

MORPH_DISC_SENT_MCQ_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Affixes: {affixes}
Sentence: {sentence}
Options:
{options}
Answer: {answer}"""

MORPH_DISC_NONCE_SENT_MCQ_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of affixes (separated by comma), a sentence with a blank (___) and a list of words in {language} that are derived from the given word root using the given affixes. Your task is to fill in the blank by selecting the grammatically correct option. Output only the correct option number."

MORPH_DISC_NONCE_SENT_MCQ_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Affixes: {affixes}
Sentence: {sentence}
Options:
{options}
Answer: {answer}"""

#### Sense
MORPH_DISC_SENSE_MCQ_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of affixes (separated by comma), a definition and a list of words in {language} that are derived from the given word root using the given affixes. Your task is to select the word that fits the given definition. Output only the correct option number."

MORPH_DISC_SENSE_MCQ_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Affixes: {affixes}
Definition: {target_definition}
Options:
{options}
Answer: {answer}"""

MORPH_DISC_NONCE_SENSE_MCQ_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of affixes (separated by comma), a target word definition and a list of words in {language} that are derived from the given word root using the given affixes. Your task is to select the word that fits the given target definition. Output only the correct option number."

MORPH_DISC_NONCE_SENSE_MCQ_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root} (definition: {root_definition})
Affixes: {affixes}
Target definition: {target_definition}
Options:
{options}
Answer: {answer}"""


################################ Prompt templates in Turkish ################################
MORPH_DISC_MCQ_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak verilen kökten türetilmiş kelimelerin bir listesi verilecek. Sizden doğru seçeneği seçmeniz istenecek. Sadece doğru seçeneğin numarasını çıktı olarak verin."

MORPH_DISC_MCQ_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {affixes}
Seçenekler:
{options}
Cevap: {answer}"""

MORPH_DISC_MCQ_NONCE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak verilen kökten türetilmiş kelimelerin bir listesi verilecek. Sizden doğru seçeneği seçmeniz istenecek. Sadece doğru seçeneğin numarasını çıktı olarak verin."

MORPH_DISC_MCQ_NONCE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
Ekler: {affixes}
Seçenekler:
{options}
Cevap: {answer}"""