import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def plot_sentiment_distribution(df, column="sentiment"):
    sns.countplot(x=column, data=df)
    plt.title("Sentiment Distribution")
    plt.show()

def generate_wordcloud(df, sentiment):
    text = " ".join(df[df["sentiment"] == sentiment]["cleaned"])
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(f"{sentiment} Word Cloud")
    plt.show()