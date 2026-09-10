import re
from collections import Counter

# Sample training data
real_news = [
    "government announces new education policy",
    "scientists publish research on climate change",
    "school opens new computer science department",
    "company announces new technology product"
]

fake_news = [
    "scientists discover miracle cure for all diseases",
    "government gives free money to everyone",
    "aliens secretly control the government",
    "one food can make you live forever"
]

# Convert text into words
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.split()

# Create word frequency
real_words = Counter()
fake_words = Counter()

for news in real_news:
    real_words.update(preprocess(news))

for news in fake_news:
    fake_words.update(preprocess(news))

# Prediction function
def predict_news(news):
    words = preprocess(news)

    real_score = sum(real_words[word] for word in words)
    fake_score = sum(fake_words[word] for word in words)

    if fake_score > real_score:
        return "FAKE NEWS"
    else:
        return "REAL NEWS"

# User input
news = input("Enter news article: ")

result = predict_news(news)

print("\nPrediction:", result)
