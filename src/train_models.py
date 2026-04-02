import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib


def train_model(data_path):

    df = pd.read_csv(data_path)

    df = df.drop(columns=[
        "UDI",
        "Product ID",
        "TWF",
        "HDF",
        "PWF",
        "OSF",
        "RNF"
    ])

    X = df.drop("Machine failure", axis=1)
    y = df["Machine failure"]

    X = pd.get_dummies(X, columns=["Type"])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    joblib.dump(model, "models/failure_prediction_model.pkl")