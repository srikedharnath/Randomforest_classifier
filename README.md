

# Random Forest Classifier - Student Pass/Fail Prediction

## Project Overview

This project predicts whether a student will Pass or Fail using a Random Forest Classifier Machine Learning model.

The prediction is based on:

- Math Score
- Reading Score
- Writing Score

The project is built using:

- Python
- Streamlit
- Scikit-learn
- Pandas

---

## Features

- Simple Streamlit User Interface
- Random Forest Classification
- Predicts Pass or Fail instantly
- Easy to understand and beginner friendly

---

## Dataset

Dataset used:

StudentsPerformance.csv

The dataset contains student marks and performance details.

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- NumPy

---

## Installation

Install required libraries using:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Use the following command:

```bash
streamlit run app.py
```

---

## Test Cases

### Fail Prediction

| Math | Reading | Writing |
|------|----------|----------|
| 20 | 25 | 18 |

### Pass Prediction

| Math | Reading | Writing |
|------|----------|----------|
| 85 | 90 | 88 |

---

## Project Structure

```text
project folder
│
├── app.py
├── StudentsPerformance.csv
├── requirements.txt
├── README.md
```

---

## Output

The application predicts:

- Pass
- Fail

based on student marks.

---

## Author

Machine Learning Mini Project
