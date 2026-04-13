from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.prediction_engine import predict_failure

app = FastAPI()


class MachineData(BaseModel):
    Type: str = Field(..., example="M")
    Air_temperature: float = Field(..., gt=0)
    Process_temperature: float = Field(..., gt=0)
    Rotational_speed: float = Field(..., gt=0)
    Torque: float = Field(..., gt=0)
    Tool_wear: float = Field(..., ge=0)


@app.get("/")
def root():
    return {"message": "Predictive Maintenance API running"}


@app.post("/predict")
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