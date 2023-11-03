from transformers import pipeline

ru_en = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")
en_ru = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-en-ru")

str = 'проверка пройдена'
en_str = ru_en(str)[0]['translation_text']
ru_str = en_ru(en_str)[0]['translation_text']
print(str, '->', en_str, '->', ru_str)
