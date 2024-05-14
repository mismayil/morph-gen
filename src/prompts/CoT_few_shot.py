#suffux len 1 
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


#suffux len 2
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

#suffux len 3 
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


#suffux len 4 
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

#suffux len 5 
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



#suffux len 6 
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



#suffux len 7 
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


#suffux len 8 
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


#suffux len 9 
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