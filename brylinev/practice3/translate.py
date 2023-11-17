from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()

@app.post("/en-ru/")
async def en_ru(item: Item):
    """Переводит текст с английского на русский."""
    model = pipeline("translation", 'Helsinki-NLP/opus-mt-en-ru')
    return model(item.text)[0]['translation_text']

@app.post("/ru-en/")
async def ru_en(item: Item):
    """Переводит текст с русского на английский."""
    model = pipeline("translation", 'Helsinki-NLP/opus-mt-ru-en')
    return model(item.text)[0]['translation_text']
