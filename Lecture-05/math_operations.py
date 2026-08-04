#math_operation.py

def add(a, b):
    return a + b

def subtact(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b