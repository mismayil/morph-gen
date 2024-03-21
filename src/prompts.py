# Prompt templates in English
MORPH_GEN_EN_INSTRUCTION_TEMPLATE = "You are given a word root and a list of suffixes (separated by comma) in {language} and your task is to generate a grammatically correct word from this root using all the given suffixes. You are allowed to use only the given suffixes and each suffix only once. Answer with only the generated word."

MORPH_GEN_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Suffixes: {suffixes}
Answer: {answer}"""

MORPH_DISC_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of suffixes (separated by comma) and a list of words in {language} that are derived from the given word root using the given suffixes. Your task is to select the grammatically correct option. Output only the correct option number."

MORPH_DISC_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Suffixes: {suffixes}
Options:
{options}
Answer: {answer}"""

MORPH_GEN_NONCE_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition and a list of suffixes (separated by comma) in {language} and your task is to generate a grammatically correct word from this root using all the given suffixes. You are allowed to use only the given suffixes and each suffix only once. Answer with only the generated word."

MORPH_GEN_NONCE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {definition}
Suffixes: {suffixes}
Answer: {answer}"""

MORPH_DISC_NONCE_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of suffixes (separated by comma) and a list of words in {language} that are derived from the given word root using the given suffixes. Your task is to select the grammatically correct option. Output only the correct option number."

MORPH_DISC_NONCE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {definition}
Suffixes: {suffixes}
Options:
{options}
Answer: {answer}"""


# Prompt templates for sentence completion tasks
MORPH_GEN_SENT_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of suffixes (separated by comma) and a sentence with a blank (___) in {language} and your task is to fill in the blank by generating a grammatically correct word from this root using all the given suffixes. You are allowed to use only the given suffixes and each suffix only once. Answer with only the generated word."

MORPH_GEN_SENT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Suffixes: {suffixes}
Sentence: {sentence}
Answer: {answer}"""

MORPH_DISC_SENT_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of suffixes (separated by comma), a sentence with a blank (___) and a list of words in {language} that are derived from the given word root using the given suffixes. Your task is to fill in the blank by selecting the grammatically correct option. Output only the correct option number."

MORPH_DISC_SENT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Suffixes: {suffixes}
Sentence: {sentence}
Options:
{options}
Answer: {answer}"""

MORPH_GEN_NONCE_SENT_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of suffixes (separated by comma) and a sentence with a blank (___) in {language} and your task is to fill in the blank by generating a grammatically correct word from this root using all the given suffixes. You are allowed to use only the given suffixes and each suffix only once. Answer with only the generated word."

MORPH_GEN_NONCE_SENT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {definition}
Suffixes: {suffixes}
Sentence: {sentence}
Answer: {answer}"""

MORPH_DISC_NONCE_SENT_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of suffixes (separated by comma), a sentence with a blank (___) and a list of words in {language} that are derived from the given word root using the given suffixes. Your task is to fill in the blank by selecting the grammatically correct option. Output only the correct option number."

MORPH_DISC_NONCE_SENT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {definition}
Suffixes: {suffixes}
Sentence: {sentence}
Options:
{options}
Answer: {answer}"""



# Prompt templates in Turkish
MORPH_GEN_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök ve bir ek listesi (virgülle ayrılmış) verilecek ve sizden bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {suffixes}
Cevap: {answer}"""

MORPH_DISC_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak verilen kökten türetilmiş kelimelerin bir listesi verilecek. Sizden doğru seçeneği seçmeniz istenecek. Sadece doğru seçeneğin numarasını çıktı olarak verin."

MORPH_DISC_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {suffixes}
Seçenekler:
{options}
Cevap: {answer}"""

MORPH_GEN_NONCE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması ve bir ek listesi (virgülle ayrılmış) verilecek ve sizden bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_NONCE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {definition}
Ekler: {suffixes}
Cevap: {answer}"""

MORPH_DISC_NONCE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak verilen kökten türetilmiş kelimelerin bir listesi verilecek. Sizden doğru seçeneği seçmeniz istenecek. Sadece doğru seçeneğin numarasını çıktı olarak verin."

MORPH_DISC_NONCE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {definition}
Ekler: {suffixes}
Seçenekler:
{options}
Cevap: {answer}"""

# Prompt templates for sentence completion tasks in Turkish
MORPH_GEN_SENT_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış) ve boşluklu (___) bir cümle verilecek ve sizden boşluğu doldurmak için bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_SENT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {suffixes}
Cümle: {sentence}
Cevap: {answer}"""

MORPH_DISC_SENT_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış), boşluklu (___) bir cümle ve bu ekleri kullanarak verilen kökten türetilmiş kelimelerin bir listesi verilecek. Sizden boşluğu doldurmak için doğru seçeneği seçmeniz istenecek. Sadece doğru seçeneğin numarasını çıktı olarak verin."

MORPH_DISC_SENT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {suffixes}
Cümle: {sentence}
Seçenekler:
{options}
Cevap: {answer}"""

MORPH_GEN_NONCE_SENT_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış) ve boşluklu (___) bir cümle verilecek ve sizden boşluğu doldurmak için bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_NONCE_SENT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {definition}
Ekler: {suffixes}
Cümle: {sentence}
Cevap: {answer}"""

MORPH_DISC_NONCE_SENT_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış), boşluklu (___) bir cümle ve bu ekleri kullanarak verilen kökten türetilmiş kelimelerin bir listesi verilecek. Sizden boşluğu doldurmak için doğru seçeneği seçmeniz istenecek. Sadece doğru seçeneğin numarasını çıktı olarak verin."

MORPH_DISC_NONCE_SENT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {definition}
Ekler: {suffixes}
Cümle: {sentence}
Seçenekler:
{options}
Cevap: {answer}"""


# Prompt templates when the target is order of suffixes
MORPH_GEN_ORDER_EN_INSTRUCTION_TEMPLATE = "You are given a word root and a list of suffixes (separated by comma) in {language} and your task is to output the correct order of all suffixes such that if suffixes are applied in this order to the given root, it results in a grammatically correct word. You are allowed to use only the given suffixes and each suffix only once. Answer with only the order of suffixes indicated by their numbers."

MORPH_GEN_NONCE_ORDER_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition and a list of suffixes (separated by comma) in {language} and your task is to output the correct order of all suffixes such that if suffixes are applied in this order to the given root, it results in a grammatically correct word. You are allowed to use only the given suffixes and each suffix only once. Answer with only the order of suffixes indicated by their numbers."