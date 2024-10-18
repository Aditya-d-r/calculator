from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Calculator App!"}

@app.get("/add/{a}/{b}")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract/{a}/{b}")
def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/multiply/{a}/{b}")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide/{a}/{b}")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"result": a / b}
