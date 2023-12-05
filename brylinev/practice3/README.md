# Англо-русский переводчик.

Использованы две готовые модели для разных направлений перевода:
[Helsinki-NLP/opus-mt-en-ru](https://huggingface.co/Helsinki-NLP/opus-mt-en-ru)
и [Helsinki-NLP/opus-mt-ru-en](https://huggingface.co/Helsinki-NLP/opus-mt-ru-en)

Реализованное API можно использвать для перевода текста с английского на русский и с русского на английский. Подерживается 2 метода:<br>
POST /en-ru/<br>
POST /ru-en/<br>
Оба метода принимают на вход строку `text` в формате json и возвращают переведенный текст.

Выполнил: Брылин Е.В.<br>
Написал README: Власов Г.С.

