import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    return sentiment

def get_primary_sentiment(sentiment):
    if sentiment['compound'] >= 0.05:
        return "Positive"
    elif sentiment['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

st.title("Sentiment Analysis")

text_input = st.text_area("Enter text for sentiment analysis:")

if st.button("Analyze"):
    if text_input:
        sentiment = analyze_sentiment(text_input)
        primary_sentiment = get_primary_sentiment(sentiment)
        st.write(f"Primary Sentiment: {primary_sentiment}")
    else:
        st.write("Please enter text for analysis.")
