from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def classify_textblob(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1: return "Positive"
    elif polarity < -0.1: return "Negative"
    else: return "Neutral"

def classify_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)["compound"]
    if score > 0.1: return "Positive"
    elif score < -0.1: return "Negative"
    else: return "Neutral"