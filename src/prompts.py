# Prompt templates in English
MORPH_GEN_EN_INSTRUCTION_TEMPLATE = "You are given a word root and a list of suffixes in {language} and your task is to generate a grammatically correct word from this root using all the given suffixes. You are allowed to use only the given suffixes and each suffix only once. Answer with only the generated word."

MORPH_GEN_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Suffixes: {suffixes}
Answer: {answer}"""

MORPH_DISC_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of suffixes and a list of words in {language} that are derived from the given word root using the given suffixes. Your task is to select the grammatically correct option. Output only the correct option number."

MORPH_DISC_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Suffixes: {suffixes}
Options:
{options}
Answer: {answer}"""

# Prompt templates in Turkish
MORPH_GEN_TR_INSTRUCTION_TEMPLATE = "Size bir kök ve bir ek listesi verilecek ve sizden bu kökten verilen ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {suffixes}
Cevap: {answer}"""

MORPH_DISC_TR_INSTRUCTION_TEMPLATE = "Size bir kök, bir ek listesi ve bu ekleri kullanarak verilen kökten türetilmiş kelimelerin bir listesi verilecek. Sizden doğru seçeneği seçmeniz istenecek. Sadece doğru seçeneğin numarasını çıktı olarak verin."

MORPH_DISC_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {suffixes}
Seçenekler:
{options}
Cevap: {answer}"""