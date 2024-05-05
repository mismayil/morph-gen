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
Definition: {root_definition}
Suffixes: {suffixes}
Answer: {answer}"""

MORPH_DISC_NONCE_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of suffixes (separated by comma) and a list of words in {language} that are derived from the given word root using the given suffixes. Your task is to select the grammatically correct option. Output only the correct option number."

MORPH_DISC_NONCE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
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
Definition: {root_definition}
Suffixes: {suffixes}
Sentence: {sentence}
Answer: {answer}"""

MORPH_DISC_NONCE_SENT_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of suffixes (separated by comma), a sentence with a blank (___) and a list of words in {language} that are derived from the given word root using the given suffixes. Your task is to fill in the blank by selecting the grammatically correct option. Output only the correct option number."

MORPH_DISC_NONCE_SENT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Suffixes: {suffixes}
Sentence: {sentence}
Options:
{options}
Answer: {answer}"""

# Prompt templates for sense understanding tasks
MORPH_GEN_SENSE_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of suffixes (separated by comma) and a definition in {language} and your task is to generate a word that fits the given definition by using all the given suffixes. You are allowed to use only the given suffixes and each suffix only once. Answer with only the generated word."

MORPH_GEN_SENSE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Suffixes: {suffixes}
Definition: {target_definition}
Answer: {answer}"""

MORPH_DISC_SENSE_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of suffixes (separated by comma), a definition and a list of words in {language} that are derived from the given word root using the given suffixes. Your task is to select the word that fits the given definition. Output only the correct option number."

MORPH_DISC_SENSE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Suffixes: {suffixes}
Definition: {target_definition}
Options:
{options}
Answer: {answer}"""

MORPH_GEN_NONCE_SENSE_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of suffixes (separated by comma) and a target word definition in {language} and your task is to generate a word that fits the given target definition by using all the given suffixes. You are allowed to use only the given suffixes and each suffix only once. Answer with only the generated word."

MORPH_GEN_NONCE_SENSE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root} (definition: {root_definition})
Suffixes: {suffixes}
Target definition: {target_definition}
Answer: {answer}"""

MORPH_DISC_NONCE_SENSE_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of suffixes (separated by comma), a target word definition and a list of words in {language} that are derived from the given word root using the given suffixes. Your task is to select the word that fits the given target definition. Output only the correct option number."

MORPH_DISC_NONCE_SENSE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root} (definition: {root_definition})
Suffixes: {suffixes}
Target definition: {target_definition}
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
Tanım: {root_definition}
Ekler: {suffixes}
Cevap: {answer}"""

MORPH_DISC_NONCE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak verilen kökten türetilmiş kelimelerin bir listesi verilecek. Sizden doğru seçeneği seçmeniz istenecek. Sadece doğru seçeneğin numarasını çıktı olarak verin."

MORPH_DISC_NONCE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
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
Tanım: {root_definition}
Ekler: {suffixes}
Cümle: {sentence}
Cevap: {answer}"""

MORPH_DISC_NONCE_SENT_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış), boşluklu (___) bir cümle ve bu ekleri kullanarak verilen kökten türetilmiş kelimelerin bir listesi verilecek. Sizden boşluğu doldurmak için doğru seçeneği seçmeniz istenecek. Sadece doğru seçeneğin numarasını çıktı olarak verin."

MORPH_DISC_NONCE_SENT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
Ekler: {suffixes}
Cümle: {sentence}
Seçenekler:
{options}
Cevap: {answer}"""


# Prompt templates when the target is order of suffixes
MORPH_GEN_ORDER_EN_INSTRUCTION_TEMPLATE = "You are given a word root and a list of suffixes (separated by comma) in {language} and your task is to output the correct order of all suffixes such that if suffixes are applied in this order to the given root, it results in a grammatically correct word. You are allowed to use only the given suffixes and each suffix only once. Answer with only the order of suffixes indicated by their numbers."

MORPH_GEN_NONCE_ORDER_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition and a list of suffixes (separated by comma) in {language} and your task is to output the correct order of all suffixes such that if suffixes are applied in this order to the given root, it results in a grammatically correct word. You are allowed to use only the given suffixes and each suffix only once. Answer with only the order of suffixes indicated by their numbers."

# Prompt templates for sense understanding in Turkish
MORPH_GEN_SENSE_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış) ve bir tanım verilecek ve sizden bu tanıma uyan bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_SENSE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {suffixes}
Tanım: {root_definition}
Cevap: {answer}"""

MORPH_DISC_SENSE_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış), bir tanım ve bu ekleri kullanarak türetilmiş kelimelerin bir listesi verilecek. Sizden tanıma uyan doğru kelimeyi seçmeniz istenecek. Sadece doğru seçeneğin numarasını çıktı olarak verin."

MORPH_DISC_SENSE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {suffixes}
Tanım: {root_definition}
Seçenekler:
{options}
Cevap: {answer}"""

MORPH_GEN_NONCE_SENSE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış) ve bir hedef kelime tanımı verilecek ve sizden bu hedef tanıma uyan bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_NONCE_SENSE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root} (tanım: {root_definition})
Ekler: {suffixes}
Hedef tanım: {target_definition}
Cevap: {answer}"""

MORPH_DISC_NONCE_SENSE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış), bir hedef kelime tanımı ve bu ekleri kullanarak türetilmiş kelimelerin bir listesi verilecek. Sizden hedef tanıma uyan doğru kelimeyi seçmeniz istenecek. Sadece doğru seçeneğin numarasını çıktı olarak verin."

MORPH_DISC_NONCE_SENSE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root} (tanım: {root_definition})
Ekler: {suffixes}
Hedef tanım: {target_definition}
Seçenekler:
{options}
Cevap: {answer}"""

# Prompt templates for morphological discriminatation tasks (binary) in English
MORPH_DISC_BIN_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of suffixes (separated by comma) and a word in {language} that is derived from the given word root using the given suffixes. Your task is to determine whether the derived word is grammatically correct. Answer only with Yes or No."

MORPH_DISC_BIN_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Suffixes: {suffixes}
Derived word: {derived_word}
Answer: {answer}"""

MORPH_DISC_NONCE_BIN_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of suffixes (separated by comma) and a word in {language} that is derived from the given word root using the given suffixes. Your task is to determine whether the derived word is grammatically correct. Answer only with Yes or No."

MORPH_DISC_NONCE_BIN_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Suffixes: {suffixes}
Derived word: {derived_word}
Answer: {answer}"""

# Prompt templates for morphological discriminatation tasks (binary) in Turkish
MORPH_DISC_BIN_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Sadece Evet veya Hayır ile cevap verin."

MORPH_DISC_BIN_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {suffixes}
Türetilmiş kelime: {derived_word}
Cevap: {answer}"""

MORPH_DISC_NONCE_BIN_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Sadece Evet veya Hayır ile cevap verin."

MORPH_DISC_NONCE_BIN_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
Ekler: {suffixes}
Türetilmiş kelime: {derived_word}
Cevap: {answer}"""