from flask import render_template
from modules import calculator
from app import app

@app.route('/<operator>/<x>/<y>')
def function(operator, x, y):
    x = int(x)
    y = int(y)
    if operator == "add":
        return f"{calculator.add(x, y)}"
    if operator == "subtract":
        sum = calculator.subtract(x, y)
        return str(sum)
    if operator == "multiply":
        return calculator.multiply(x, y)
    if operator == "divide":
        return calculator.divide(x, y)
    else:
        return none

