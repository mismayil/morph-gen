##################################### Prompt templates in English #####################################
MORPH_GEN_COT_EN_INSTRUCTION_TEMPLATE = "You are given a word root and a list of affixes (separated by comma) in {language}. Your task is to construct a grammatically correct word by appending the given affixes to the root. Use each affix exactly once. After forming a word, list each affix used in the construction of that word to verify adherence to the rules. Check the following: Ensure no affix is used more than once, confirm that all provided affixes are used, verify that no extra affixes outside the provided list are included. Think step by step and then provide your final answer within the tags <Answer>correctword</Answer>."

MORPH_GEN_COT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Affixes: {affixes}
Answer: {answer}"""

MORPH_DISC_COT_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of affixes (separated by comma) and a word in {language} that is derived from the given word root using the given affixes. Your task is to determine whether the derived word is grammatically correct. First, analyze how the affixes interact with the word root. Then, assess the order in which the affixes are applied and verify that this order adheres to the language's rules. Think step by step and then provide your final answer within the tags <Answer>Yes/No</Answer>."

MORPH_DISC_COT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Affixes: {affixes}
Derived word: {derived_word}
Answer: {answer}"""

MORPH_GEN_NONCE_COT_EN_INSTRUCTION_TEMPLATE = "You are provided with a novel word root with its definition, and a list of affixes (separated by comma) in {language}. Your task is to construct a grammatically correct word by appending the given affixes to the root. Use each affix exactly once. After forming a word, list each affix used in the construction of that word to verify adherence to the rules. Check the following: Ensure no affix is used more than once, confirm that all provided affixes are used, verify that no extra affixes outside the provided list are included. Think step by step and then provide your final answer within the tags <Answer>correctword</Answer>."

MORPH_GEN_NONCE_COT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Affixes: {affixes}
Answer: {answer}"""

MORPH_DISC_NONCE_COT_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of affixes (separated by comma) and a word in {language} that is derived from the given word root using the given affixes. Your task is to determine whether the derived word is grammatically correct. First, analyze how the affixes interact with the word root. Then, assess the order in which the affixes are applied and verify that this order adheres to the language's rules. Think step by step and then provide your final answer within the tags <Answer>Yes/No</Answer>."

MORPH_DISC_NONCE_COT_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Affixes: {affixes}
Derived word: {derived_word}
Answer: {answer}"""
############################################################################################


#################################################### Prompt templates in Turkish ####################################################
MORPH_GEN_COT_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök ve bir ek listesi (virgülle ayrılmış) verilecek ve sizden bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Bir kelime oluşturduktan sonra, o kelimenin oluşturulmasında kullanılan her eki listeleyin ve kurallara uygunluğunu doğrulayın. Aşağıdakileri kontrol edin: Hiçbir ek birden fazla kullanılmamalı, tüm verilen ekler kullanılmalı, listeye dahil olmayan ekler eklenmemeli. Adım adım düşünün ve sonra cevabınızı açılı parantez içinde sunun <Cevap>doğrukelime</Cevap>."

MORPH_GEN_COT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {affixes}
Cevap: {answer}"""

MORPH_DISC_COT_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Önce, eklerin kök kelimeyle nasıl etkileşime girdiğini analiz edin. Sonra, eklerin uygulandığı sırayı değerlendirin ve bu sıranın dilin kurallarına uygun olup olmadığını doğrulayın. Adım adım düşünün ve sonra cevabınızı açılı parantez içinde sunun <Cevap>Evet/Hayır</Cevap>.​"

MORPH_DISC_COT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {affixes}
Türetilmiş kelime: {derived_word}
Cevap: {answer}"""

MORPH_GEN_NONCE_COT_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması ve bir ek listesi (virgülle ayrılmış) verilecek ve sizden bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Bir kelime oluşturduktan sonra, o kelimenin oluşturulmasında kullanılan her eki listeleyin ve kurallara uygunluğunu doğrulayın. Aşağıdakileri kontrol edin: Hiçbir ek birden fazla kullanılmamalı, tüm verilen ekler kullanılmalı, listeye dahil olmayan ekler eklenmemeli. Adım adım düşünün ve sonra cevabınızı açılı parantez içinde sunun <Cevap>doğrukelime</Cevap>."

MORPH_GEN_NONCE_COT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
Ekler: {affixes}
Cevap: {answer}"""

MORPH_DISC_NONCE_COT_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Önce, eklerin kök kelimeyle nasıl etkileşime girdiğini analiz edin. Sonra, eklerin uygulandığı sırayı değerlendirin ve bu sıranın dilin kurallarına uygun olup olmadığını doğrulayın. Adım adım düşünün ve sonra cevabınızı açılı parantez içinde sunun <Cevap>Evet/Hayır</Cevap>."

MORPH_DISC_NONCE_COT_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
Ekler: {affixes}
Türetilmiş kelime: {derived_word}
Cevap: {answer}"""
####################################################################################################################################

##################################### Prompt templates in Finnish #####################################
MORPH_GEN_COT_FI_INSTRUCTION_TEMPLATE = """
Sinulle annetaan sanavartalo, sen määritelmä sekä pilkulla eroteltu luettelo päätteitä kielellä {language}. Tehtäväsi on luoda juuresta kieliopillisesti oikea sana käyttämällä päätteitä. Käytä vain annettuja päätteitä. Käytä kutakin päätettä vain kerran. Kun olet generoinut uuden sanan, luettele jokainen pääte, jota käytit sanan luomiseen varmistaaksesi, että noudatat sääntöjä. Varmista luettelon perusteella seuraavat asiat: jokaista päätettä käytetään tasan kerran, yhtään päätettä ei jätetä käyttämättä, eikä vastaus sisällä ylimääräisiä päätteitä. Ajattele askel/asia kerrallaan ja anna lopullinen vastauksesi tägeissä <Vastaus>oikea sana</Vastaus>.
"""

MORPH_GEN_COT_FI_SHOT_TEMPLATE = """
Esimerkki {index}:
Sananvartalo: {root}
Päätteet: {affixes}
Vastaus: {answer}
""".strip()

MORPH_DISC_COT_FI_INSTRUCTION_TEMPLATE = """
Sinulle annetaan sanavartalo, pilkulla eroteltu luettelo päätteistä sekä annettuja päätteitä käyttämällä vartalosta johdettu sana kielellä {language}. Tehtäväsi on selvittää, onko johdettu sana kieliopillisesti oikein. Analysoi ensiksi miten päätteet vaikuttavat sananvartaloon. Arvioi sitten, ovatko päätteet kieliopillisesti oikeassa järjestyksessä. Ajattele askel/asia kerrallaan ja anna lopullinen vastauksesi tägeissä <Vastaus>Kyllä/Ei</Vastaus>.
""".strip()

MORPH_DISC_COT_FI_SHOT_TEMPLATE = """
Esimerkki {index}:
Sananvartalo: {root}
Päätteet: {affixes}
Johdettu sana: {derived_word}
Vastaus: {answer}
""".strip()

MORPH_GEN_NONCE_COT_FI_INSTRUCTION_TEMPLATE = """
Sinulle annetaan uusi sanavartalo, sen määritelmä sekä pilkulla eroteltu luettelo päätteitä kielellä {language}. Tehtäväsi on luoda juuresta kieliopillisesti oikea sana käyttämällä päätteitä. Käytä vain annettuja päätteitä. Käytä kutakin päätettä vain kerran. Kun olet generoinut uuden sanan, luettele jokainen pääte, jota käytit sanan luomiseen varmistaaksesi, että noudatat sääntöjä. Varmista luettelon perusteella seuraavat asiat: jokaista päätettä käytetään tasan kerran, yhtään päätettä ei jätetä käyttämättä, eikä vastaus sisällä ylimääräisiä päätteitä. Ajattele askel/asia kerrallaan ja anna lopullinen vastauksesi tägeissä <Vastaus>oikea sana</Vastaus>.
""".strip()

MORPH_GEN_NONCE_COT_FI_SHOT_TEMPLATE = """
Esimerkki {index}:
Sananvartalo: {root}
Määritelmä: {root_definition}
Päätteet: {affixes}
Vastaus: {answer}
""".strip()

MORPH_DISC_NONCE_COT_FI_INSTRUCTION_TEMPLATE = """
Sinulle annetaan uusi sanavartalo, pilkulla eroteltu luettelo päätteistä sekä annettuja päätteitä käyttämällä vartalosta johdettu sana kielellä {language}. Tehtäväsi on selvittää, onko johdettu sana kieliopillisesti oikein. Analysoi ensiksi miten päätteet vaikuttavat sananvartaloon. Arvioi sitten, ovatko päätteet kieliopillisesti oikeassa järjestyksessä. Ajattele askel/asia kerrallaan ja anna lopullinen vastauksesi tägeissä <Vastaus>Kyllä/Ei</Vastaus>.
""".strip()

MORPH_DISC_NONCE_COT_FI_SHOT_TEMPLATE = """
Esimerkki {index}:
Sananvartalo: {root}
Määritelmä: {root_definition}
Päätteet: {affixes}
Johdettu sana: {derived_word}
Vastaus: {answer}
"""
############################################################################################
