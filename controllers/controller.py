from modules.calculator import *
from app import app

@app.route('/add/<number1>/<number2>')
def add_numbers(number1, number2):
    return add(number1, number2)

@app.route('/substract/<number1>/<number2>')
def substract_numbers(number1, number2):
    return substract(number1, number2)

@app.route('/multiply/<number1>/<number2>')
def multiply_numbers(number1, number2):
    return multiply(number1, number2)

@app.route('/divide/<number1>/<number2>')
def divide_numbers(number1, number2):
    return divide(number1, number2)