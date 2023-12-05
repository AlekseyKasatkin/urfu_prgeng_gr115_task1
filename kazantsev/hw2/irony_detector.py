from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import streamlit as st

#available types of task:
# emoji, emotion, hate, irony, offensive, sentiment
# stance/abortion, stance/atheism, stance/climate, stance/feminist, stance/hillary
TASK = "irony"

@st.cache_data
def prepare_model():
    model_id = f"cardiffnlp/twitter-roberta-base-{TASK}"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSequenceClassification.from_pretrained(model_id)
    return tokenizer, model

def detect_irony(text, tokenizer, model):
    labels=["Вполне серьезный комментарий:  ", "(: Вам ответили иронично:  "]
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    rslt = []
    for i in range(scores.shape[0]):
        l = labels[ranking[i]]
        s = scores[ranking[i]]
        message = f"{l} {np.round(float(s), 3) * 100}%"
        rslt.append(message)
    return rslt

st.title("Здесь вы можете определить иронично ли вам ответили или нет))0")
text_to_detect = st.text_area(
    label='Итак, что же вам такого написали? (Желательно на англ)', 
    placeholder='Введите текст', 
    key='text_to_detect')
btn = st.button("Определить", type="primary")

if btn and text_to_detect:
    tokenizer, model = prepare_model()
    result = detect_irony(text_to_detect, tokenizer, model)
    for r in result:
        st.write(r)

