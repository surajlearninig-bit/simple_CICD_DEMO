from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .calculator import Calculator

app = FastAPI()
calculator = Calculator()

class CalculationRequest(BaseModel):
    x: float
    y: float

@app.post("/add")
def add(request: CalculationRequest):
    return {"result": calculator.add(request.x, request.y)}

@app.post("/subtract")
def subtract(request: CalculationRequest):
    return {"result": calculator.subtract(request.x, request.y)}

@app.post("/multiply")
def multiply(request: CalculationRequest):
    return {"result": calculator.multiply(request.x, request.y)}

@app.post("/divide")
def divide(request: CalculationRequest):
    try:
        return {"result": calculator.divide(request.x, request.y)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
