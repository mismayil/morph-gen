############################### Prompt templates in English ###############################
MORPH_GEN_SENT_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of suffixes (separated by comma) and a sentence with a blank (___) in {language} and your task is to fill in the blank by generating a grammatically correct word from this root using all the given suffixes. You are allowed to use only the given suffixes and each suffix only once. Answer with only the generated word."

MORPH_GEN_SENT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Suffixes: {suffixes}
Sentence: {sentence}
Answer: {answer}"""

MORPH_DISC_SENT_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of suffixes (separated by comma), a sentence with a blank (___) and a word in {language} that is derived from the given word root using the given suffixes. Your task is to determine whether the derived word is the correct option to fill in the blank. Answer only with Yes or No."

MORPH_DISC_SENT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Suffixes: {suffixes}
Sentence: {sentence}
Derived word: {derived_word}
Answer: {answer}"""

MORPH_GEN_NONCE_SENT_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of suffixes (separated by comma) and a sentence with a blank (___) in {language} and your task is to fill in the blank by generating a grammatically correct word from this root using all the given suffixes. You are allowed to use only the given suffixes and each suffix only once. Answer with only the generated word."

MORPH_GEN_NONCE_SENT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Suffixes: {suffixes}
Sentence: {sentence}
Answer: {answer}"""

MORPH_DISC_NONCE_SENT_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of suffixes (separated by comma), a sentence with a blank (___) and a word in {language} that is derived from the given word root using the given suffixes. Your task is to determine whether the derived word is the correct option to fill in the blank. Answer only with Yes or No."

MORPH_DISC_NONCE_SENT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Suffixes: {suffixes}
Sentence: {sentence}
Derived word: {derived_word}
Answer: {answer}"""
##############################################################################################

############################### Prompt templates in Turkish #################################################
MORPH_GEN_SENT_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış) ve boşluklu (___) bir cümle verilecek ve sizden boşluğu doldurmak için bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_SENT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {suffixes}
Cümle: {sentence}
Cevap: {answer}"""

MORPH_DISC_SENT_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış), boşluklu (___) bir cümle ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden boşluğu doldurmak için bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Sadece Evet veya Hayır ile cevap verin."

MORPH_DISC_SENT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {suffixes}
Cümle: {sentence}
Türetilmiş kelime: {derived_word}
Cevap: {answer}"""

MORPH_GEN_NONCE_SENT_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış) ve boşluklu (___) bir cümle verilecek ve sizden boşluğu doldurmak için bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_NONCE_SENT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
Ekler: {suffixes}
Cümle: {sentence}
Cevap: {answer}"""

MORPH_DISC_NONCE_SENT_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış), boşluklu (___) bir cümle ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden boşluğu doldurmak için bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Sadece Evet veya Hayır ile cevap verin."

MORPH_DISC_NONCE_SENT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
Ekler: {suffixes}
Cümle: {sentence}
Türetilmiş kelime: {derived_word}
Cevap: {answer}"""
#############################################################################################
