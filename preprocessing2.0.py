import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("wordnet")

def clean_text(text):
    text = re.sub(r"http\S+|@\S+|[^A-Za-z\s]", "", text.lower())
    tokens = text.split()
    tokens = [WordNetLemmatizer().lemmatize(t) for t in tokens if t not in stopwords.words("english")]
    return " ".join(tokens)