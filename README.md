# Customer Review Sentiment Analysis using FastAPI

## Overview

This project is a simple Sentiment Analysis web application built using FastAPI and Scikit-learn. It predicts whether a customer review is positive or negative using the Multinomial Naive Bayes algorithm and a CountVectorizer.

The application provides:

* FastAPI REST API
* Interactive HTML User Interface
* CSS Styling
* Sentiment Prediction Endpoint

---

## Technologies Used

* Python 3.x
* FastAPI
* Scikit-learn
* NumPy
* Jinja2 Templates
* HTML
* CSS
* Uvicorn

---

## Project Structure

```
p5/
│
├── main.py
├── model.py
├── schema.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── index.css
```

---

## Dataset

Training Reviews:

* the product is good → Positive
* the product is bad → Negative
* the product is very good → Positive
* the product is very bad → Negative

Labels:

* 1 = Positive
* 0 = Negative

---

## Features

* Predict customer review sentiment.
* Simple and responsive web interface.
* REST API support.
* Easy to extend with larger datasets.

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd p5
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## API Endpoint

### Predict Sentiment

**Endpoint**

```
POST /predict
```

**Request Body**

```json
{
  "review": "the product is very good"
}
```

**Response**

```json
{
  "review": "the product is very good",
  "prediction": "Positive Review"
}
```

---

## Web Interface

Open:

```
http://127.0.0.1:8000
```

Enter a customer review and click the **Predict Sentiment** button to get the prediction.

---

## Example Predictions

Input:

```
the product is very good
```

Output:

```
Positive Review
```

Input:

```
the product is bad
```

Output:

```
Negative Review
```

---

## Future Improvements

* Train on larger datasets.
* Add more sentiment categories.
* Store prediction history in a database.
* Deploy on cloud platforms such as Render or Railway.

---

## Author

Aditya Kumar
