import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("StudentsPerformance.csv")

df["average"] = (
    df["math score"] +
    df["reading score"] +
    df["writing score"]
) / 3

df["result"] = df["average"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

label_encoder = LabelEncoder()

df["result"] = label_encoder.fit_transform(df["result"])

X = df[[
    "math score",
    "reading score",
    "writing score"
]]

y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

st.title("Random Forest Classifier")
st.subheader("Student Pass/Fail Prediction")

math_score = st.number_input(
    "Math Score",
    min_value=0,
    max_value=100,
    value=20
)

reading_score = st.number_input(
    "Reading Score",
    min_value=0,
    max_value=100,
    value=25
)

writing_score = st.number_input(
    "Writing Score",
    min_value=0,
    max_value=100,
    value=18
)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "math score": [math_score],
        "reading score": [reading_score],
        "writing score": [writing_score]
    })

    prediction = model.predict(input_data)

    result = label_encoder.inverse_transform(prediction)

    st.success(f"Prediction: {result[0]}")