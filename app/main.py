from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    """
    Root endpoint for the calculator app.
    
    Returns a welcome message.
    """
    return {"message": "Welcome to the Calculator App!"}

@app.get("/add/{a}/{b}")
def add(a: float, b: float):
    """
    Adds two numbers and returns the result.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        dict: The result of the addition.
    """
    return {"result": a + b}

@app.get("/subtract/{a}/{b}")
def subtract(a: float, b: float):
    """
    Subtracts the second number from the first and returns the result.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        dict: The result of the subtraction.
    """
    return {"result": a - b}

@app.get("/multiply/{a}/{b}")
def multiply(a: float, b: float):
    """
    Multiplies two numbers and returns the result.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        dict: The result of the multiplication.
    """
    return {"result": a * b}

@app.get("/divide/{a}/{b}")
def divide(a: float, b: float):
    """
    Divides the first number by the second and returns the result.

    Args:
        a (float): The first number.
        b (float): The second number. Must not be zero.

    Raises:
        HTTPException: If division by zero is attempted.

    Returns:
        dict: The result of the division.
    """
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"result": a / b}
