from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.prediction_engine import predict_failure

app = FastAPI(
    title="Predictive Maintenance API",
    description="API for predicting machine failure based on sensor data",
    version="1.0.0"
)


class MachineData(BaseModel):
    Type: str = Field(..., example="M")
    Air_temperature: float = Field(..., gt=0)
    Process_temperature: float = Field(..., gt=0)
    Rotational_speed: float = Field(..., gt=0)
    Torque: float = Field(..., gt=0)
    Tool_wear: float = Field(..., ge=0)


class PredictionResponse(BaseModel):
    prediction: int
    status: str


@app.get("/", tags=["Health"])
def root():
    return {"message": "Predictive Maintenance API running"}


@app.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
def predict(input_data: MachineData):
    try:
        data = input_data.dict()

        result = predict_failure(data)

        return {
            "prediction": int(result),
            "status": "failure" if result == 1 else "normal"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))