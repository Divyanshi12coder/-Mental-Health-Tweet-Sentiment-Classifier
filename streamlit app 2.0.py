import streamlit as st
from src.preprocess import clean_text
from src.sentiment import classify_vader

st.title("🧠 Mental Health Tweet Sentiment Classifier")

text = st.text_area("Enter a tweet or message:")
if st.button("Analyze"):
    cleaned = clean_text(text)
    sentiment = classify_vader(cleaned)
    st.success(f"Predicted Sentiment: **{sentiment}**")