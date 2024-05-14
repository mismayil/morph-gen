##################################### Prompt templates in English #####################################
MORPH_GEN_EN_INSTRUCTION_TEMPLATE = "You are provided with a word root and a list of suffixes (separated by commas) in {language}. Your task is to construct a grammatically correct word by appending the given suffixes to the root. Use each suffix exactly once. After forming a word, list each suffix used in the construction of that word to verify adherence to the rules. Check the following: Ensure no suffix is used more than once, confirm that all provided suffixes are used, verify that no extra suffixes outside the provided list are included. If the word violates any of the above criteria: adjust the formation of the word and repeat the verification until a word is formed that complies with all rules. Present the correctly formed word enclosed in angle brackets. Example: <correctword>."

MORPH_GEN_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Suffixes: {suffixes}
Thought: {thought}
Answer: {answer}"""

MORPH_DISC_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of suffixes (separated by comma) and a word in {language} that is derived from the given word root using the given suffixes. Your task is to determine whether the derived word is grammatically correct. First, analyze how the suffixes interact with the word root. Then, assess the order in which the suffixes are applied and verify that this order adheres to the language's rules. Examine any modifications that occur to the root or the suffixes during word formation (e.g., phonetic changes, alterations in the root structure). Answer with Yes or No, placing your response within angle brackets. Example: <Yes> or <No>."

MORPH_DISC_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Suffixes: {suffixes}
Derived word: {derived_word}
Thought: {thought}
Answer: {answer}"""

MORPH_GEN_NONCE_EN_INSTRUCTION_TEMPLATE = "You are provided with a novel word root and a list of suffixes (separated by commas) in {language}. Your task is to construct a grammatically correct word by appending the given suffixes to the root. Use each suffix exactly once. After forming a word, list each suffix used in the construction of that word to verify adherence to the rules. Check the following: Ensure no suffix is used more than once, confirm that all provided suffixes are used, verify that no extra suffixes outside the provided list are included. If the word violates any of the above criteria: adjust the formation of the word and repeat the verification until a word is formed that complies with all rules. Present the correctly formed word enclosed in angle brackets. Example: <correctword>."

MORPH_GEN_NONCE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Suffixes: {suffixes}
Thought: {thought}
Answer: {answer}"""

MORPH_DISC_NONCE_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of suffixes (separated by comma) and a word in {language} that is derived from the given word root using the given suffixes. Your task is to determine whether the derived word is grammatically correct. First, analyze how the suffixes interact with the word root. Then, assess the order in which the suffixes are applied and verify that this order adheres to the language's rules. Examine any modifications that occur to the root or the suffixes during word formation (e.g., phonetic changes, alterations in the root structure). Answer with Yes or No, placing your response within angle brackets. Example: <Yes> or <No>.​"

MORPH_DISC_NONCE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: {root}
Definition: {root_definition}
Suffixes: {suffixes}
Derived word: {derived_word}
Thought: {thought}
Answer: {answer}"""
############################################################################################


#################################################### Prompt templates in Turkish ####################################################
MORPH_GEN_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök ve bir ek listesi (virgülle ayrılmış) verilecek ve sizden bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Bir kelime oluşturduktan sonra, o kelimenin oluşturulmasında kullanılan her eki listeyin ve kurallara uygunluğunu doğrulayın. Aşağıdakileri kontrol edin: Hiçbir ek birden fazla kullanılmamalı, tüm verilen ekler kullanılmalı, listeye dahil olmayan ekler eklenmemeli. Eğer kelime yukarıdaki kriterleri ihlal ederse: kelimenin oluşumunu düzeltin ve tüm kurallara uygun bir kelime oluşturulana kadar doğrulamayı tekrarlayın. Doğru şekilde oluşturulmuş kelimeyi açılı parantezler içinde sunun. Örnek: <doğrukelime>."

MORPH_GEN_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {suffixes}
Düşünce: {düşūnce}
Cevap: {answer}"""

MORPH_DISC_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Önce, eklerin kök kelimeyle nasıl etkileşime girdiğini analiz edin. Sonra, eklerin uygulandığı sırayı değerlendirin ve bu sıranın dilin kurallarına uygun olup olmadığını doğrulayın. Kelime oluşumu sırasında kök veya eklerde meydana gelen değişiklikleri (örn., fonetik değişiklikler, kök yapısında değişiklikler) inceleyin. Cevabınızı Evet veya Hayır olarak verin, yanıtınızı açılı parantez içine alın. Örnek: <Evet> veya <Hayır>.​"

MORPH_DISC_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Ekler: {suffixes}
Türetilmiş kelime: {derived_word}
Düşünce: {düşūnce}
Cevap: {answer}"""

MORPH_GEN_NONCE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması ve bir ek listesi (virgülle ayrılmış) verilecek ve sizden bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Bir kelime oluşturduktan sonra, o kelimenin oluşturulmasında kullanılan her eki listeyin ve kurallara uygunluğunu doğrulayın. Aşağıdakileri kontrol edin: Hiçbir ek birden fazla kullanılmamalı, tüm verilen ekler kullanılmalı, listeye dahil olmayan ekler eklenmemeli. Eğer kelime yukarıdaki kriterleri ihlal ederse: kelimenin oluşumunu düzeltin ve tüm kurallara uygun bir kelime oluşturulana kadar doğrulamayı tekrarlayın. Doğru şekilde oluşturulmuş kelimeyi açılı parantezler içinde sunun. Örnek: <doğrukelime>"

MORPH_GEN_NONCE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
Ekler: {suffixes}
Düşünce: {düşūnce}
Cevap: {answer}"""

MORPH_DISC_NONCE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Önce, eklerin kök kelimeyle nasıl etkileşime girdiğini analiz edin. Sonra, eklerin uygulandığı sırayı değerlendirin ve bu sıranın dilin kurallarına uygun olup olmadığını doğrulayın. Kelime oluşumu sırasında kök veya eklerde meydana gelen değişiklikleri (örn., fonetik değişiklikler, kök yapısında değişiklikler) inceleyin. Cevabınızı Evet veya Hayır olarak verin, yanıtınızı açılı parantez içine alın. Örnek: <Evet> veya <Hayır>"

MORPH_DISC_NONCE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: {root}
Tanım: {root_definition}
Ekler: {suffixes}
Türetilmiş kelime: {derived_word}
Düşünce: {düşūnce}
Cevap: {answer}"""
####################################################################################################################################