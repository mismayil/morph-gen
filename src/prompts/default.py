##################################### Prompt templates in English #####################################
MORPH_GEN_EN_INSTRUCTION_TEMPLATE = "You are given a word root and a list of suffixes (separated by comma) in {language} and your task is to generate a grammatically correct word from this root using all the given suffixes. You are allowed to use only the given suffixes and each suffix only once. Answer with only the generated word."

MORPH_GEN_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Suffixes: {suffixes}
Answer: {answer}"""

MORPH_DISC_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of suffixes (separated by comma) and a word in {language} that is derived from the given word root using the given suffixes. Your task is to determine whether the derived word is grammatically correct. Answer only with Yes or No."

MORPH_DISC_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Suffixes: {suffixes}
Derived word: {derived_word}
Answer: {answer}"""

MORPH_GEN_NONCE_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition and a list of suffixes (separated by comma) in {language} and your task is to generate a grammatically correct word from this root using all the given suffixes. You are allowed to use only the given suffixes and each suffix only once. Answer with only the generated word."

MORPH_GEN_NONCE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Suffixes: {suffixes}
Answer: {answer}"""

MORPH_DISC_NONCE_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of suffixes (separated by comma) and a word in {language} that is derived from the given word root using the given suffixes. Your task is to determine whether the derived word is grammatically correct. Answer only with Yes or No."

MORPH_DISC_NONCE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Suffixes: {suffixes}
Derived word: {derived_word}
Answer: {answer}"""
############################################################################################


#################################################### Prompt templates in Turkish ####################################################
MORPH_GEN_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök ve bir ek listesi (virgülle ayrılmış) verilecek ve sizden bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {suffixes}
Cevap: {answer}"""

MORPH_DISC_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Sadece Evet veya Hayır ile cevap verin."

MORPH_DISC_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {suffixes}
Türetilmiş kelime: {derived_word}
Cevap: {answer}"""

MORPH_GEN_NONCE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması ve bir ek listesi (virgülle ayrılmış) verilecek ve sizden bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_NONCE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
Ekler: {suffixes}
Cevap: {answer}"""

MORPH_DISC_NONCE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Sadece Evet veya Hayır ile cevap verin."

MORPH_DISC_NONCE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
Ekler: {suffixes}
Türetilmiş kelime: {derived_word}
Cevap: {answer}"""
####################################################################################################################################

##################################### Prompt templates in Finnish #####################################
MORPH_GEN_FI_INSTRUCTION_TEMPLATE = "Sinulle annetaan sanan sanavartalo ja luettelo pilkulla erotettuja päätteitä kielellä {language}. Tehtäväsi on luoda tästä juuresta kieliopillisesti oikea sana käyttämällä kaikkia annettuja päätteitä. Voit käyttää vain annettuja päätteitä ja kutakin päätettä vain kerran. Vastaa vain luodulla sanalla."

MORPH_GEN_FI_SHOT_TEMPLATE = """Esimerkki {index}:
Sanavartalo: {root}
Päätteet: {suffixes}
Vastaus: {answer}"""

MORPH_DISC_FI_INSTRUCTION_TEMPLATE = "Sinulle annetaan sanavartalo, pilkulla eroteltu luettelo päätteistä sekä annettuja päätteitä käyttämällä vartalosta johdettu sana kielellä {language}. Tehtäväsi on selvittää, onko johdettu sana kieliopillisesti oikein. Vastaa vain Kyllä tai Ei."

MORPH_DISC_FI_SHOT_TEMPLATE = """Esimerkki {index}:
Sanavartalo: {root}
Päätteet: {suffixes}
Johdettu sana: {derived_word}
Vastaus: {answer}"""

MORPH_GEN_NONCE_FI_INSTRUCTION_TEMPLATE = "Sinulle annetaan uusi sanavartalo, sen määritelmä sekä pilkulla eroteltu luettelo päätteitä kielellä {language}. Tehtäväsi on luoda juuresta kieliopillisesti oikea sana käyttämällä kaikkia annettuja päätteitä. Käyttä vain annettuja päätteitä ja kutakin päätettä vain kerran. Vastaa vain luodulla sanalla."

MORPH_GEN_NONCE_FI_SHOT_TEMPLATE = """Esimerkki {index}:
Sanavartalo: {root}
Määritelmä: {root_definition}
Päätteet: {suffixes}
Vastaus: {answer}"""

MORPH_DISC_NONCE_FI_INSTRUCTION_TEMPLATE = "Sinulle annetaan uusi sanavartalo, sen määritelmä sekä pilkulla eroteltu luettelo päätteistä sekä uusi sana kielellä {kieli}, joka on johdettu annetusta sanavartalosta annettujen päätteiden avulla. Tehtäväsi on selvittää, onko johdettu sana kieliopillisesti oikein. Vastaa vain Kyllä tai Ei."

MORPH_DISC_NONCE_EN_SHOT_TEMPLATE = """Esimerkki {index}:
SanaVartalo: {root}
Määritelmä: {root_definition}
Päätteet: {suffixes}
Johdettu sana: {derived_word}
Vastaus: {answer}"""

############################################################################################


##################################### Prompt templates in English for perplexity task #####################################
MORPH_DISC_PP_EN_INSTRUCTION_TEMPLATE = ""

MORPH_DISC_PP_EN_SHOT_TEMPLATE = """{text}"""
############################################################################################
