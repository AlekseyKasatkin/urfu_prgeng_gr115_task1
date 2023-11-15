from transformers import pipeline

# load model
en_ru = pipeline("translation", "Helsinki-NLP/opus-mt-en-ru")

en_str = input('Введите текст на английском: ')

#translate
res = en_ru(en_str)[0]['translation_text']

print('Перевод:', res)
