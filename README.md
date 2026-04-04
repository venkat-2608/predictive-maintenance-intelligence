# Predictive Maintenance Intelligence System

This project builds a machine learning system that predicts industrial machine failure using telemetry sensor data.

## Project Goal

Industrial machines generate multiple sensor signals such as vibration, temperature, torque, and rotational speed.  
The goal of this system is to analyze these signals and detect early warning signs of machine failure.

## Planned Machine Learning Pipeline

- Data exploration
- Data preprocessing
- Feature engineering
- Model training
- Model evaluation
- Failure prediction engine

Predictive Maintenance Intelligence System

The system predicts machine failure based on sensor telemetry data.

Pipeline:

Sensor Data
    ↓
Feature Engineering
    ↓
Machine Learning Model (Random Forest)
    ↓
Prediction Engine
    ↓
FastAPI API
    ↓
User Input → Failure Prediction

## How to Run the Project

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the FastAPI Server
```bash
uvicorn src.api:app --reload
```

### 3. Open API Documentation
Open your browser and go to:

http://127.0.0.1:8000/docs

### 4. Example Prediction Input
Use the following JSON payload to test the prediction API:

```json
{
  "Type": "L",
  "Air_temperature": 300,
  "Process_temperature": 310,
  "Rotational_speed": 1500,
  "Torque": 40,
  "Tool_wear": 50
}
```