import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

reviews = [
    "the product is good",
    "the product is bad",
    "the product is very good",
    "the product is very bad"
]

sentiments = np.array([1, 0, 1, 0])

cv = CountVectorizer()
X = cv.fit_transform(reviews)

classifier = MultinomialNB()
classifier.fit(X, sentiments)


def predict_sentiment(review: str):
    review_vectorized = cv.transform([review])
    prediction = classifier.predict(review_vectorized)[0]

    if prediction == 1:
        return "Positive Review"
    else:
        return "Negative Review"