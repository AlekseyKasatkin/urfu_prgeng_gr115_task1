import streamlit as st
from transformers import pipeline

labels = ['Английский', 'Русский']
titles = ['Англо-русский', 'Русско-английский']

# устанавливаем переменные сессии
if 'direction' not in st.session_state:
    st.session_state.direction = False

# меняем направление перевода
def toggle_direction():
    st.session_state.direction = not st.session_state.direction
    st.session_state.in_text, st.session_state.out_text = st.session_state.out_text, st.session_state.in_text

@st.cache_resource
def load_model(direction):
    models = ['Helsinki-NLP/opus-mt-en-ru', 'Helsinki-NLP/opus-mt-ru-en']
    return pipeline("translation", models[direction])


st.title(titles[st.session_state.direction] + ' переводчик')
st.button(titles[not st.session_state.direction], on_click=toggle_direction)

# получаем текст для перевода
in_text = st.text_area(
    labels[st.session_state.direction],
    placeholder='Enter text here',
    key='in_text'
)
btn = st.button("Translate", type="primary")

out_text = ''
if btn and in_text:
    # вызываем функцию, которая загружает модель
    translator = load_model(st.session_state.direction)
    # переводим текст
    out_text = translator(in_text)[0]['translation_text']

# выводим переведенный текст
st.text_area(
    labels[not st.session_state.direction],
    out_text,
    key='out_text',
    disabled=True
)
