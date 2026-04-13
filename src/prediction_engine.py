import pandas as pd
import joblib

# load trained model once
model = joblib.load("models/failure_prediction_model.pkl")


def preprocess_input(data: dict) -> pd.DataFrame:
    """
    Convert raw API input into model-ready DataFrame
    """

    df = pd.DataFrame([{
        "Air temperature [K]": data["Air_temperature"],
        "Process temperature [K]": data["Process_temperature"],
        "Rotational speed [rpm]": data["Rotational_speed"],
        "Torque [Nm]": data["Torque"],
        "Tool wear [min]": data["Tool_wear"]
    }])

    # encode machine type safely
    machine_type = data.get("Type", "").upper()

    df["Type_L"] = 1 if machine_type == "L" else 0
    df["Type_M"] = 1 if machine_type == "M" else 0
    df["Type_H"] = 1 if machine_type == "H" else 0

    return df


def predict_failure(data: dict) -> int:
    """
    Run prediction on processed input
    """

    df = preprocess_input(data)

    prediction = model.predict(df)[0]

    return int(prediction)