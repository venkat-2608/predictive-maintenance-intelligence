import pandas as pd
import joblib

# load trained model
model = joblib.load("models/failure_prediction_model.pkl")


def predict_failure(data):

    # convert API input into dataframe
    df = pd.DataFrame([{
        "Air temperature [K]": data["Air_temperature"],
        "Process temperature [K]": data["Process_temperature"],
        "Rotational speed [rpm]": data["Rotational_speed"],
        "Torque [Nm]": data["Torque"],
        "Tool wear [min]": data["Tool_wear"]
    }])

    # encode machine type
    df["Type_L"] = 1 if data["Type"] == "L" else 0
    df["Type_M"] = 1 if data["Type"] == "M" else 0
    df["Type_H"] = 1 if data["Type"] == "H" else 0

    # prediction
    prediction = model.predict(df)[0]

    return int(prediction)