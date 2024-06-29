# Prompt templates when the target is order of affixes
MORPH_GEN_ORDER_EN_INSTRUCTION_TEMPLATE = "You are given a word root and a list of affixes (separated by comma) in {language} and your task is to output the correct order of all affixes such that if affixes are applied in this order to the given root, it results in a grammatically correct word. You are allowed to use only the given affixes and each affix only once. Answer with only the order of affixes indicated by their numbers."

MORPH_GEN_NONCE_ORDER_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition and a list of affixes (separated by comma) in {language} and your task is to output the correct order of all affixes such that if affixes are applied in this order to the given root, it results in a grammatically correct word. You are allowed to use only the given affixes and each affix only once. Answer with only the order of affixes indicated by their numbers."

# Prompt templates for sense understanding in Turkish
MORPH_GEN_SENSE_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış) ve bir tanım verilecek ve sizden bu tanıma uyan bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_SENSE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {affixes}
Tanım: {root_definition}
Cevap: {answer}"""

MORPH_DISC_SENSE_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış), bir tanım ve bu ekleri kullanarak türetilmiş kelimelerin bir listesi verilecek. Sizden tanıma uyan doğru kelimeyi seçmeniz istenecek. Sadece doğru seçeneğin numarasını çıktı olarak verin."

MORPH_DISC_SENSE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {affixes}
Tanım: {root_definition}
Seçenekler:
{options}
Cevap: {answer}"""

MORPH_GEN_NONCE_SENSE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış) ve bir hedef kelime tanımı verilecek ve sizden bu hedef tanıma uyan bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_NONCE_SENSE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root} (tanım: {root_definition})
Ekler: {affixes}
Hedef tanım: {target_definition}
Cevap: {answer}"""

MORPH_DISC_NONCE_SENSE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış), bir hedef kelime tanımı ve bu ekleri kullanarak türetilmiş kelimelerin bir listesi verilecek. Sizden hedef tanıma uyan doğru kelimeyi seçmeniz istenecek. Sadece doğru seçeneğin numarasını çıktı olarak verin."

MORPH_DISC_NONCE_SENSE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root} (tanım: {root_definition})
Ekler: {affixes}
Hedef tanım: {target_definition}
Seçenekler:
{options}
Cevap: {answer}"""