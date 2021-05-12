import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Select an Option",
    [
        "Classify Text",
        "Translation"
    ]
)

if option == "Classify Text":
    text = st.text_area(label="Enter text")
    if text:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)
elif option == "Translation":
    translator = pipeline("translation_en_to_de")
    text = st.text_area(label="Enter text")
    if text:
        translation = translator(text)
        st.write(translation)
