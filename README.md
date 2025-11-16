# 🧠 Mental Health Tweet Sentiment Classifier

This project analyzes tweets related to mental health using Natural Language Processing (NLP) to classify sentiment as **positive**, **negative**, or **neutral**. It helps visualize emotional trends and raise awareness around mental health issues in digital spaces.

---

## 🎯 Objectives

- Collect and preprocess mental health-related tweets  
- Perform sentiment classification using NLP techniques  
- Visualize sentiment trends over time  
- Build an interactive dashboard for real-time analysis  

---

## 🛠️ Tech Stack

| Category         | Tools & Libraries                          |
|------------------|--------------------------------------------|
| Language         | Python                                     |
| NLP              | VADER                                      |
| Data Collection  | Twitter API (Tweepy)                       |
| Visualization    | Matplotlib                                 |
| Deployment       | Streamlit                                  |

---

## 📁 Project Structure

```
mental-health-sentiment/
│
├── data/                  # Raw and cleaned tweet datasets
├── notebooks/             # EDA and model training
├── src/                   # Preprocessing, modeling, and utils
├── app/                   # Streamlit app for live predictions
├── models/                # Saved sentiment models
├── README.md              # Project documentation
└── requirements.txt       # Dependencies
```

---

## 🔍 Workflow

1. **Data Collection**  
   - Use Twitter API to scrape tweets with keywords like “depression”, “anxiety”, “mental health”

2. **Preprocessing**  
   - Remove stopwords, punctuation, emojis  
   - Apply lemmatization and tokenization  

3. **Sentiment Classification**  
   - Use VADER for rule-based sentiment  
   - Optionally train ML models (Logistic Regression, SVM)  

4. **Visualization**  
   - Plot sentiment distribution, word clouds, and time-series trends  

5. **Deployment**  
   - Build a web app for real-time tweet sentiment analysis  

---

## 📊 Sample Results

- Achieved 85–90% accuracy on labeled sentiment data  
- Visualized spikes in negative sentiment during global events  
- Dashboard allows keyword-based sentiment tracking  

---


## 🌱 Future Enhancements

- Integrate LSTM or BERT for deeper sentiment modeling  
- Add geolocation-based sentiment mapping  
- Expand to multilingual tweet analysis  

---


## 📌 Dataset Sources

- Twitter API (live scraping)  
- [Kaggle Mental Health Tweets Dataset](https://www.kaggle.com/datasets)

---

Would you like a matching logo, badges, or deployment instructions for Hugging Face or Heroku? I can also help you add model interpretability or real-time sentiment alerts.
