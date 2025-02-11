##################################### Prompt templates in English #####################################
MORPH_GEN_EN_INSTRUCTION_TEMPLATE = "You are given a word root and a list of affixes (separated by comma) in {language} and your task is to generate a grammatically correct word from this root using all the given affixes. You are allowed to use only the given affixes and each affix only once. Answer with only the generated word."

MORPH_GEN_ALT_EN_INSTRUCTION_TEMPLATE = "You are provided with a word root and a set of affixes (comma-separated) in {language}. Your task is to create a grammatically correct word using this root and all the provided affixes. You must use only the given affixes, and each affix can be used only once. Respond with the final word only."

MORPH_GEN_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Affixes: {affixes}
Answer: {answer}"""

MORPH_DISC_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of affixes (separated by comma) and a word in {language} that is derived from the given word root using the given affixes. Your task is to determine whether the derived word is grammatically correct. Answer only with Yes or No."

MORPH_DISC_ALT_EN_INSTRUCTION_TEMPLATE = "You are provided with a word root, a set of affixes (comma-separated), and a word in {language} that is derived from the given root using the provided affixes. Your task is to verify whether the derived word is grammatically correct. Respond with only Yes or No."

MORPH_DISC_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Affixes: {affixes}
Derived word: {derived_word}
Answer: {answer}"""

MORPH_GEN_NONCE_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition and a list of affixes (separated by comma) in {language} and your task is to generate a grammatically correct word from this root using all the given affixes. You are allowed to use only the given affixes and each affix only once. Answer with only the generated word."

MORPH_GEN_NONCE_ALT_EN_INSTRUCTION_TEMPLATE = "You are given a new word root along with its definition, and a set of affixes (comma-separated) in {language}. Assuming that the new word root is a valid {language} word, your task is to form a grammatically correct word using this root and all the provided affixes. You must use only the given affixes, and each one can be used just once. Provide only the generated word as your answer."

MORPH_GEN_NONCE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Affixes: {affixes}
Answer: {answer}"""

MORPH_DISC_NONCE_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of affixes (separated by comma) and a word in {language} that is derived from the given word root using the given affixes. Your task is to determine whether the derived word is grammatically correct. Answer only with Yes or No."

MORPH_DISC_NONCE_ALT_EN_INSTRUCTION_TEMPLATE = "You are provided with a new word root along with its definition, a set of affixes (comma-separated), and a word in {language} that is derived from the given root using the provided affixes. Assuming that the new word root is a valid {language} word, your task is to verify whether the derived word is grammatically correct. Respond with only Yes or No."

MORPH_DISC_NONCE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Affixes: {affixes}
Derived word: {derived_word}
Answer: {answer}"""
############################################################################################


#################################################### Prompt templates in Turkish ####################################################
MORPH_GEN_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök ve bir ek listesi (virgülle ayrılmış) verilecek ve sizden bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {affixes}
Cevap: {answer}"""

MORPH_DISC_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Sadece Evet veya Hayır ile cevap verin."

MORPH_DISC_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {affixes}
Türetilmiş kelime: {derived_word}
Cevap: {answer}"""

MORPH_GEN_NONCE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması ve bir ek listesi (virgülle ayrılmış) verilecek ve sizden bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_NONCE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
Ekler: {affixes}
Cevap: {answer}"""

MORPH_DISC_NONCE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Sadece Evet veya Hayır ile cevap verin."

MORPH_DISC_NONCE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
Ekler: {affixes}
Türetilmiş kelime: {derived_word}
Cevap: {answer}"""
####################################################################################################################################

##################################### Prompt templates in Finnish #####################################
MORPH_GEN_FI_INSTRUCTION_TEMPLATE = "Sinulle annetaan sanan sananvartalo ja luettelo pilkulla erotettuja päätteitä kielellä {language}. Tehtäväsi on luoda tästä juuresta kieliopillisesti oikea sana käyttämällä kaikkia annettuja päätteitä. Voit käyttää vain annettuja päätteitä ja kutakin päätettä vain kerran. Vastaa vain luodulla sanalla."

MORPH_GEN_FI_SHOT_TEMPLATE = """Esimerkki {index}:
Sananvartalo: {root}
Päätteet: {affixes}
Vastaus: {answer}"""

MORPH_DISC_FI_INSTRUCTION_TEMPLATE = "Sinulle annetaan sananvartalo, pilkulla eroteltu luettelo päätteistä sekä annettuja päätteitä käyttämällä vartalosta johdettu sana kielellä {language}. Tehtäväsi on selvittää, onko johdettu sana kieliopillisesti oikein. Vastaa vain Kyllä tai Ei."

MORPH_DISC_FI_SHOT_TEMPLATE = """Esimerkki {index}:
Sananvartalo: {root}
Päätteet: {affixes}
Johdettu sana: {derived_word}
Vastaus: {answer}"""

MORPH_GEN_NONCE_FI_INSTRUCTION_TEMPLATE = "Sinulle annetaan uusi sananvartalo, sen määritelmä sekä pilkulla eroteltu luettelo päätteitä kielellä {language}. Tehtäväsi on luoda juuresta kieliopillisesti oikea sana käyttämällä kaikkia annettuja päätteitä. Käyttä vain annettuja päätteitä ja kutakin päätettä vain kerran. Vastaa vain luodulla sanalla."

MORPH_GEN_NONCE_FI_SHOT_TEMPLATE = """Esimerkki {index}:
Sananvartalo: {root}
Määritelmä: {root_definition}
Päätteet: {affixes}
Vastaus: {answer}"""

MORPH_DISC_NONCE_FI_INSTRUCTION_TEMPLATE = "Sinulle annetaan uusi sananvartalo, sen määritelmä sekä pilkulla eroteltu luettelo päätteistä sekä uusi sana kielellä {language}, joka on johdettu annetusta sananvartalosta annettujen päätteiden avulla. Tehtäväsi on selvittää, onko johdettu sana kieliopillisesti oikein. Vastaa vain Kyllä tai Ei."

MORPH_DISC_NONCE_FI_SHOT_TEMPLATE = """Esimerkki {index}:
Sananvartalo: {root}
Määritelmä: {root_definition}
Päätteet: {affixes}
Johdettu sana: {derived_word}
Vastaus: {answer}"""

############################################################################################


##################################### Prompt templates in English for perplexity task #####################################
MORPH_DISC_PP_EN_INSTRUCTION_TEMPLATE = ""

MORPH_DISC_PP_EN_SHOT_TEMPLATE = """{text}"""
############################################################################################
