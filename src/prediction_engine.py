import joblib
import pandas as pd


MODEL_PATH = "models/failure_prediction_model.pkl"


def load_model():
    model = joblib.load(MODEL_PATH)
    return model


def predict_failure(input_data):

    model = load_model()

    df = pd.DataFrame([input_data])

    df = pd.get_dummies(df)

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "failure_probability": float(probability)
    }