############################### Prompt templates in English ###############################
MORPH_GEN_SENT_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of affixes (separated by comma) and a sentence with a blank (___) in {language} and your task is to fill in the blank by generating a grammatically correct word from this root using all the given affixes. You are allowed to use only the given affixes and each affix only once. Answer with only the generated word."

MORPH_GEN_SENT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Affixes: {affixes}
Sentence: {sentence}
Answer: {answer}"""

MORPH_DISC_SENT_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of affixes (separated by comma), a sentence with a blank (___) and a word in {language} that is derived from the given word root using the given affixes. Your task is to determine whether the derived word is the correct option to fill in the blank. Answer only with Yes or No."

MORPH_DISC_SENT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Affixes: {affixes}
Sentence: {sentence}
Derived word: {derived_word}
Answer: {answer}"""

MORPH_GEN_NONCE_SENT_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of affixes (separated by comma) and a sentence with a blank (___) in {language} and your task is to fill in the blank by generating a grammatically correct word from this root using all the given affixes. You are allowed to use only the given affixes and each affix only once. Answer with only the generated word."

MORPH_GEN_NONCE_SENT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Affixes: {affixes}
Sentence: {sentence}
Answer: {answer}"""

MORPH_DISC_NONCE_SENT_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of affixes (separated by comma), a sentence with a blank (___) and a word in {language} that is derived from the given word root using the given affixes. Your task is to determine whether the derived word is the correct option to fill in the blank. Answer only with Yes or No."

MORPH_DISC_NONCE_SENT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Affixes: {affixes}
Sentence: {sentence}
Derived word: {derived_word}
Answer: {answer}"""
##############################################################################################

############################### Prompt templates in Turkish #################################################
MORPH_GEN_SENT_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış) ve boşluklu (___) bir cümle verilecek ve sizden boşluğu doldurmak için bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_SENT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {affixes}
Cümle: {sentence}
Cevap: {answer}"""

MORPH_DISC_SENT_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış), boşluklu (___) bir cümle ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden boşluğu doldurmak için bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Sadece Evet veya Hayır ile cevap verin."

MORPH_DISC_SENT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {affixes}
Cümle: {sentence}
Türetilmiş kelime: {derived_word}
Cevap: {answer}"""

MORPH_GEN_NONCE_SENT_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış) ve boşluklu (___) bir cümle verilecek ve sizden boşluğu doldurmak için bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Sadece üretilen kelimeyi çıktı olarak verin."

MORPH_GEN_NONCE_SENT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
Ekler: {affixes}
Cümle: {sentence}
Cevap: {answer}"""

MORPH_DISC_NONCE_SENT_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış), boşluklu (___) bir cümle ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden boşluğu doldurmak için bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Sadece Evet veya Hayır ile cevap verin."

MORPH_DISC_NONCE_SENT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
Ekler: {affixes}
Cümle: {sentence}
Türetilmiş kelime: {derived_word}
Cevap: {answer}"""
#############################################################################################

############################### Prompt templates in Finnish #################################################
MORPH_DISC_NONCE_SENT_FI_INSTRUCTION_TEMPLATE = "Allaolevassa lauseessa on tyhjä kohta (___) joka tulee täyttää kieliopillisesti oikealla sanalla. Alla on myös sananvartalo, sen määritelmä, pilkulla eroteltu luettelo päätteistä sekä niitä käyttäen annetusta vartalosta johdettu sana kielellä {kieli}. Tehtäväsi on päätellä, onko johdettu sana kieliopillisesti oikein, jos sen asettaa lauseen tyhjään kohtaan eli onko sana kieliopillisesti oikein taivutetu asiayhteys/konteksti huomioonottaen. Vastaa joko Kyllä tai Ei."

MORPH_DISC_NONCE_SENT_FI_SHOT_TEMPLATE = \
"""
Esimerkki {index}:
Sananvartalo: {root}
Määritelmä: {root_definition}
Päätteet: {affixes}
Lause: {sentence}
Johdettu sana: {derived_word}
Vastaus: {answer}
""".strip()

MORPH_DISC_SENT_FI_INSTRUCTION_TEMPLATE = "Allaolevassa lauseessa on tyhjä kohta (___) joka tulee täyttää kieliopillisesti oikealla sanalla. Alla on myös sananvartalo, pilkulla eroteltu luettelo päätteistä sekä niitä käyttäen annetusta vartalosta johdettu sana kielellä {kieli}. Tehtäväsi on päätellä, onko johdettu sana kieliopillisesti oikein, jos sen asettaa lauseen tyhjään kohtaan eli onko sana kieliopillisesti oikein taivutetu asiayhteys/konteksti huomioonottaen. Vastaa joko Kyllä tai Ei."

MORPH_DISC_SENT_FI_SHOT_TEMPLATE: = \
"""
Esimerkki {index}:
Sananvartalo: {root}
Päätteet: {affixes}
Lause: {sentence}
Johdettu sana: {derived_word}
Vastaus: {answer}
""".strip()

MORPH_GEN_NONCE_SENT_FI_INSTRUCTION_TEMPLATE = "Allaolevassa lauseessa (kirjoitettu kielellä {language}) on tyhjä kohta (___) joka tulee täyttää kieliopillisesti oikealla sanalla. Alla on myös uusi sananvartalo, sen määritelmä sekä pilkulla eroteltu luettelo päätteistä. Tehtäväsi on käyttää vartaloa sekä päätteitä ja johtaa niistä kieliopillisesti oikein taivutetu sana joka sopii tyhjään kohtaan lausessaa asiayhteys/konteksti huomioonottaen. Käytä jokaista päätettä vain kerran. Vastaa vain generoidulla sanalla, älä sano mitään muuta."

MORPH_GEN_NONCE_SENT_FI_SHOT_TEMPLATE = \
"""
Esimerkki {index}:
Sananvartalo: {root}
Määritelmä: {root_definition}
Päätteet: {affixes}
Lause: {sentence}
Vastaus: {answer}
""".strip()

MORPH_GEN_SENT_FI_INSTRUCTION_TEMPLATE = "Allaolevassa lauseessa (kirjoitettu kielellä {language}) on tyhjä kohta (___) joka tulee täyttää kieliopillisesti oikealla sanalla. Alla on myös sananvartalo sekä pilkulla eroteltu luettelo päätteistä. Tehtäväsi on käyttää vartaloa sekä päätteitä ja johtaa niistä kieliopillisesti oikein taivutetu sana joka sopii tyhjään kohtaan lausessaa asiayhteys/konteksti huomioonottaen. Käytä jokaista päätettä vain kerran. Vastaa vain generoidulla sanalla, älä sano mitään muuta."

MORPH_GEN_SENT_FI_SHOT_TEMPLATE = \
"""
Esimerkki {index}:
Sananvartalo: {root}
Päätteet: {affixes}
Lause: {sentence}
Vastaus: {answer}
""".strip()
#############################################################################################
