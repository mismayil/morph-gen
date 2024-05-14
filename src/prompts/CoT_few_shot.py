#suffux len 1 
#################################################### Prompt templates in Turkish ####################################################
MORPH_GEN_EN_INSTRUCTION_TEMPLATE = "You are provided with a word root and a list of suffixes (separated by commas) in {language}. Your task is to construct a grammatically correct word by appending the given suffixes to the root. Use each suffix exactly once. After forming a word, list each suffix used in the construction of that word to verify adherence to the rules. Check the following: Ensure no suffix is used more than once, confirm that all provided suffixes are used, verify that no extra suffixes outside the provided list are included. If the word violates any of the above criteria: adjust the formation of the word and repeat the verification until a word is formed that complies with all rules. Present the correctly formed word enclosed in angle brackets. Example: <correctword>."

MORPH_GEN_EN_SHOT_TEMPLATE = """Example {index}:
Word root: devam
Suffixes: ı
Thought: The suffix given is ı. By appending ı to the word root devam, we get devamı. The suffix ı is used only once. The provided suffix ı is used. No extra suffixes are included. The word devamı is grammatically correct. The word devamı complies with all the rules.
Answer: <devamı>"""

MORPH_DISC_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of suffixes (separated by comma) and a word in {language} that is derived from the given word root using the given suffixes. Your task is to determine whether the derived word is grammatically correct. First, analyze how the suffixes interact with the word root. Then, assess the order in which the suffixes are applied and verify that this order adheres to the language's rules. Examine any modifications that occur to the root or the suffixes during word formation (e.g., phonetic changes, alterations in the root structure). Answer with Yes or No, placing your response within angle brackets. Example: <Yes> or <No>."

MORPH_DISC_EN_SHOT_TEMPLATE = """Example {index}:
Word root: devam
Suffixes: ı
Derived word: devamı
Thought: The suffix given is ı. The suffix ı is added directly to the word root devam. Since there is only one suffix, the order of application is straightforward. There are no phonetic changes or alterations in the root structure when ı is appended to devam. The derived word devamı is grammatically correct.
Answer: <Yes>"""

MORPH_GEN_NONCE_EN_INSTRUCTION_TEMPLATE = "You are provided with a novel word root and a list of suffixes (separated by commas) in {language}. Your task is to construct a grammatically correct word by appending the given suffixes to the root. Use each suffix exactly once. After forming a word, list each suffix used in the construction of that word to verify adherence to the rules. Check the following: Ensure no suffix is used more than once, confirm that all provided suffixes are used, verify that no extra suffixes outside the provided list are included. If the word violates any of the above criteria: adjust the formation of the word and repeat the verification until a word is formed that complies with all rules. Present the correctly formed word enclosed in angle brackets. Example: <correctword>."

MORPH_GEN_NONCE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: lidam
Definition: {root_definition}
Suffixes: ı
Thought: The suffix given is ı. By appending ı to the word root lidam, we get lidamı. The suffix ı is used only once. The provided suffix ı is used. No extra suffixes are included. The word devamı is grammatically correct. The word lidam complies with all the rules.
Answer: <lindamı>"""

MORPH_DISC_NONCE_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of suffixes (separated by comma) and a word in {language} that is derived from the given word root using the given suffixes. Your task is to determine whether the derived word is grammatically correct. First, analyze how the suffixes interact with the word root. Then, assess the order in which the suffixes are applied and verify that this order adheres to the language's rules. Examine any modifications that occur to the root or the suffixes during word formation (e.g., phonetic changes, alterations in the root structure). Answer with Yes or No, placing your response within angle brackets. Example: <Yes> or <No>.​"

MORPH_DISC_NONCE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: lidam
Definition: {root_definition}
Suffixes: ı
Derived word: lidamı
Thought: The suffix given is ı. The suffix ı is added directly to the word root lidam. Since there is only one suffix, the order of application is straightforward. There are no phonetic changes or alterations in the root structure when ı is appended to lidam. The derived word lidamı is grammatically correct.
Answer: <Yes>"""
############################################################################################


MORPH_GEN_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök ve bir ek listesi (virgülle ayrılmış) verilecek ve sizden bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Bir kelime oluşturduktan sonra, o kelimenin oluşturulmasında kullanılan her eki listeyin ve kurallara uygunluğunu doğrulayın. Aşağıdakileri kontrol edin: Hiçbir ek birden fazla kullanılmamalı, tüm verilen ekler kullanılmalı, listeye dahil olmayan ekler eklenmemeli. Eğer kelime yukarıdaki kriterleri ihlal ederse: kelimenin oluşumunu düzeltin ve tüm kurallara uygun bir kelime oluşturulana kadar doğrulamayı tekrarlayın. Doğru şekilde oluşturulmuş kelimeyi açılı parantezler içinde sunun. Örnek: <doğrukelime>."

MORPH_GEN_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: devam
Ekler: ı
Düşünce: Verilen ek ı ekidir. Devam köküne ı ekini ekleyerek devamı kelimesini elde ederiz. ı eki yalnızca bir kez kullanılmıştır. Verilen ı eki kullanılmıştır. Ekstra ekler dahil edilmemiştir. Devamı kelimesi dil bilgisi kurallarına uygundur. Bundan dolayi Devamı kelimesi tüm kurallara uygundur.
Cevap: <devamı>"""

MORPH_DISC_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Önce, eklerin kök kelimeyle nasıl etkileşime girdiğini analiz edin. Sonra, eklerin uygulandığı sırayı değerlendirin ve bu sıranın dilin kurallarına uygun olup olmadığını doğrulayın. Kelime oluşumu sırasında kök veya eklerde meydana gelen değişiklikleri (örn., fonetik değişiklikler, kök yapısında değişiklikler) inceleyin. Cevabınızı Evet veya Hayır olarak verin, yanıtınızı açılı parantez içine alın. Örnek: <Evet> veya <Hayır>.​"

MORPH_DISC_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: devam
Ekler: ı
Türetilmiş kelime: devamı
Düşünce: Verilen ek ı ekidir. Devam köküne ı ekini doğrudan ekleriz. Tek bir ek olduğundan, uygulama sırası açıktır. Devam kelimesine ı eklenirken kök yapısında veya eklerde ses değişiklikleri veya değişiklikler olmaz. Elde edilen devamı kelimesi dilbilgisi kurallarına uygundur.
Cevap: <Evet>"""

MORPH_GEN_NONCE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması ve bir ek listesi (virgülle ayrılmış) verilecek ve sizden bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Bir kelime oluşturduktan sonra, o kelimenin oluşturulmasında kullanılan her eki listeyin ve kurallara uygunluğunu doğrulayın. Aşağıdakileri kontrol edin: Hiçbir ek birden fazla kullanılmamalı, tüm verilen ekler kullanılmalı, listeye dahil olmayan ekler eklenmemeli. Eğer kelime yukarıdaki kriterleri ihlal ederse: kelimenin oluşumunu düzeltin ve tüm kurallara uygun bir kelime oluşturulana kadar doğrulamayı tekrarlayın. Doğru şekilde oluşturulmuş kelimeyi açılı parantezler içinde sunun. Örnek: <doğrukelime>"

MORPH_GEN_NONCE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: lidam
Tanım: {root_definition}
Ekler: ı
Düşünce: Verilen ek ı ekidir. Lidam köküne ı ekini ekleyerek lidamı kelimesini elde ederiz. ı eki yalnızca bir kez kullanılmıştır. Verilen ı eki kullanılmıştır. Ekstra ekler dahil edilmemiştir. Lidamı kelimesi dilbilgisi kurallarına uygundur. Lidamı kelimesi tüm kurallara uygundur.
Cevap: <lidamı>"""

MORPH_DISC_NONCE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Önce, eklerin kök kelimeyle nasıl etkileşime girdiğini analiz edin. Sonra, eklerin uygulandığı sırayı değerlendirin ve bu sıranın dilin kurallarına uygun olup olmadığını doğrulayın. Kelime oluşumu sırasında kök veya eklerde meydana gelen değişiklikleri (örn., fonetik değişiklikler, kök yapısında değişiklikler) inceleyin. Cevabınızı Evet veya Hayır olarak verin, yanıtınızı açılı parantez içine alın. Örnek: <Evet> veya <Hayır>"

MORPH_DISC_NONCE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: lidam
Tanım: {root_definition}
Ekler: ı
Türetilmiş kelime: lidamı
Düşünce: Verilen ek ı ekidir. Lidam köküne ı ekini doğrudan ekleriz. Tek bir ek olduğundan, uygulama sırası açıktır. Lidam kelimesine ı eklenirken kök yapısında veya eklerde ses değişiklikleri veya değişiklikler olmaz. Elde edilen lidamı kelimesi dilbilgisi kurallarına uygundur.
Cevap: <Evet>"""
####################################################################################################################################


#suffix len 2
#################################################### Prompt templates in Turkish ####################################################

MORPH_GEN_EN_INSTRUCTION_TEMPLATE = "You are provided with a word root and a list of suffixes (separated by commas) in {language}. Your task is to construct a grammatically correct word by appending the given suffixes to the root. Use each suffix exactly once. After forming a word, list each suffix used in the construction of that word to verify adherence to the rules. Check the following: Ensure no suffix is used more than once, confirm that all provided suffixes are used, verify that no extra suffixes outside the provided list are included. If the word violates any of the above criteria: adjust the formation of the word and repeat the verification until a word is formed that complies with all rules. Present the correctly formed word enclosed in angle brackets. Example: <correctword>."

MORPH_GEN_EN_SHOT_TEMPLATE = """Example {index}:
Word root: birlikte
Suffixes:  liğ, imiz
Thought: The suffix given are liğ and imiz. By appending liğ and imiz to the word root birlikte, we get birlikteliğimiz. The provided suffixes liğ and imiz are used only once. No extra suffixes are included. The word birlikteliğimiz is grammatically correct. The word devamı complies with all the rules.

Answer: <birlikteliğimiz>"""

MORPH_DISC_EN_INSTRUCTION_TEMPLATE = "You are given a word root, a list of suffixes (separated by comma) and a word in {language} that is derived from the given word root using the given suffixes. Your task is to determine whether the derived word is grammatically correct. First, analyze how the suffixes interact with the word root. Then, assess the order in which the suffixes are applied and verify that this order adheres to the language's rules. Examine any modifications that occur to the root or the suffixes during word formation (e.g., phonetic changes, alterations in the root structure). Answer with Yes or No, placing your response within angle brackets. Example: <Yes> or <No>."

MORPH_DISC_EN_SHOT_TEMPLATE = """Example {index}:
Word root: birlikte
Suffixes: liğ, imiz
Derived word: birlikteimizliğ
Thought:  First, imiz then liğ is applied to the root birlikte. According to Turkish grammar rules, this order of suffixes is not permissible, leading to the conclusion that the derived word is grammatically incorrect.
Answer: <No>"""

MORPH_GEN_NONCE_EN_INSTRUCTION_TEMPLATE = "You are provided with a novel word root and a list of suffixes (separated by commas) in {language}. Your task is to construct a grammatically correct word by appending the given suffixes to the root. Use each suffix exactly once. After forming a word, list each suffix used in the construction of that word to verify adherence to the rules. Check the following: Ensure no suffix is used more than once, confirm that all provided suffixes are used, verify that no extra suffixes outside the provided list are included. If the word violates any of the above criteria: adjust the formation of the word and repeat the verification until a word is formed that complies with all rules. Present the correctly formed word enclosed in angle brackets. Example: <correctword>."

MORPH_GEN_NONCE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: hüdin
Definition: {root_definition}
Suffixes: ken, ir
Thought: The suffix given are ken and ir. By appending ir and ken to the word root hüdin, we get hüdinkenir. The provided suffixes ken and ir are used only once. No extra suffixes are included but the word is not grammatically correct. Let's try another order. By appending ken and ir to the word root hüdin, we get hüdinirken. The provided suffixes ken and ir are used only once. No extra suffixes are included. The word hüdinirken is grammatically correct and complies with all the rules.

Answer: <hüdinirken>"""

MORPH_DISC_NONCE_EN_INSTRUCTION_TEMPLATE = "You are given a novel word root with its definition, a list of suffixes (separated by comma) and a word in {language} that is derived from the given word root using the given suffixes. Your task is to determine whether the derived word is grammatically correct. First, analyze how the suffixes interact with the word root. Then, assess the order in which the suffixes are applied and verify that this order adheres to the language's rules. Examine any modifications that occur to the root or the suffixes during word formation (e.g., phonetic changes, alterations in the root structure). Answer with Yes or No, placing your response within angle brackets. Example: <Yes> or <No>.​"

MORPH_DISC_NONCE_EN_SHOT_TEMPLATE = """Example {index}:
Word root: hüdin
Definition: {root_definition}
Suffixes: ken, ir
Derived word: hüdinirken
Thought:  First, ir then ken is applied to the root birlikte. According to Turkish grammar rules, this order of suffixes is allowed, leading to the conclusion that the derived word is grammatically incorrect.

Answer: <Yes>"""
############################################################################################


MORPH_GEN_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök ve bir ek listesi (virgülle ayrılmış) verilecek ve sizden bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Bir kelime oluşturduktan sonra, o kelimenin oluşturulmasında kullanılan her eki listeyin ve kurallara uygunluğunu doğrulayın. Aşağıdakileri kontrol edin: Hiçbir ek birden fazla kullanılmamalı, tüm verilen ekler kullanılmalı, listeye dahil olmayan ekler eklenmemeli. Eğer kelime yukarıdaki kriterleri ihlal ederse: kelimenin oluşumunu düzeltin ve tüm kurallara uygun bir kelime oluşturulana kadar doğrulamayı tekrarlayın. Doğru şekilde oluşturulmuş kelimeyi açılı parantezler içinde sunun. Örnek: <doğrukelime>."

MORPH_GEN_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: birlikte
Ekler: liğ, imiz
Düşünce: {düşūnce}
Cevap: <birlikteliğimiz>"""

MORPH_DISC_TR_INSTRUCTION_TEMPLATE = "Size {language} bir kök, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Önce, eklerin kök kelimeyle nasıl etkileşime girdiğini analiz edin. Sonra, eklerin uygulandığı sırayı değerlendirin ve bu sıranın dilin kurallarına uygun olup olmadığını doğrulayın. Kelime oluşumu sırasında kök veya eklerde meydana gelen değişiklikleri (örn., fonetik değişiklikler, kök yapısında değişiklikler) inceleyin. Cevabınızı Evet veya Hayır olarak verin, yanıtınızı açılı parantez içine alın. Örnek: <Evet> veya <Hayır>.​"

MORPH_DISC_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: birlikte
Ekler: liğ, imiz
Türetilmiş kelime: birlikteimizliğ
Düşünce: {düşūnce}
Cevap: <Hayir>"""

MORPH_GEN_NONCE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması ve bir ek listesi (virgülle ayrılmış) verilecek ve sizden bu kökten verilen tüm ekleri kullanarak dilbilgisel olarak doğru bir kelime üretmeniz istenecek. Sadece verilen ekleri kullanabilirsiniz ve her bir ek sadece bir kez kullanılabilir. Bir kelime oluşturduktan sonra, o kelimenin oluşturulmasında kullanılan her eki listeyin ve kurallara uygunluğunu doğrulayın. Aşağıdakileri kontrol edin: Hiçbir ek birden fazla kullanılmamalı, tüm verilen ekler kullanılmalı, listeye dahil olmayan ekler eklenmemeli. Eğer kelime yukarıdaki kriterleri ihlal ederse: kelimenin oluşumunu düzeltin ve tüm kurallara uygun bir kelime oluşturulana kadar doğrulamayı tekrarlayın. Doğru şekilde oluşturulmuş kelimeyi açılı parantezler içinde sunun. Örnek: <doğrukelime>"

MORPH_GEN_NONCE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: hüdin
Tanım: {root_definition}
Ekler:  ken, ir
Düşünce: {düşūnce}
Cevap: <hüdinirken>"""

MORPH_DISC_NONCE_TR_INSTRUCTION_TEMPLATE = "Size {language} yeni bir kök, onun tanımlaması, bir ek listesi (virgülle ayrılmış) ve bu ekleri kullanarak türetilmiş bir kelime verilecek. Sizden bu kelimenin dilbilgisel olarak doğru olup olmadığını belirlemeniz istenecek. Önce, eklerin kök kelimeyle nasıl etkileşime girdiğini analiz edin. Sonra, eklerin uygulandığı sırayı değerlendirin ve bu sıranın dilin kurallarına uygun olup olmadığını doğrulayın. Kelime oluşumu sırasında kök veya eklerde meydana gelen değişiklikleri (örn., fonetik değişiklikler, kök yapısında değişiklikler) inceleyin. Cevabınızı Evet veya Hayır olarak verin, yanıtınızı açılı parantez içine alın. Örnek: <Evet> veya <Hayır>"

MORPH_DISC_NONCE_TR_SHOT_TEMPLATE = """Örnek {index}:
Kök: hüdin
Tanım: {root_definition}
Ekler:  ken, ir
Türetilmiş kelime: hüdinirken
Düşünce: {düşūnce}
Cevap: <Evet>"""
####################################################################################################################################

#suffux len 3 
#################################################### Prompt templates in Turkish ####################################################

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


#suffux len 4 
#################################################### Prompt templates in Turkish ####################################################
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

#suffux len 5 
#################################################### Prompt templates in Turkish ####################################################

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



#suffux len 6 
#################################################### Prompt templates in Turkish ####################################################
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



#suffux len 7 
#################################################### Prompt templates in Turkish ####################################################
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


#suffux len 8 
#################################################### Prompt templates in Turkish ####################################################
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


#suffux len 9 
#################################################### Prompt templates in Turkish ####################################################
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