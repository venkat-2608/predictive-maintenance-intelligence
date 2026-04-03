from fastapi import FastAPI
from pydantic import BaseModel

from src.prediction_engine import predict_failure

app = FastAPI()


class MachineData(BaseModel):

    Type: str
    Air_temperature: float
    Process_temperature: float
    Rotational_speed: float
    Torque: float
    Tool_wear: float


@app.get("/")
def root():
    return {"message": "Predictive Maintenance API running"}


@app.post("/predict")
def predict(input_data: MachineData):

    # convert pydantic model → dictionary
    data = input_data.dict()

    result = predict_failure(data)

    return {
        "prediction": result
    }