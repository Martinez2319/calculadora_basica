import math
from flask import Flask, jsonify, request
from calculadora import add, sub, mul, div

app = Flask(__name__)
OPERATIONS = {"sumar": add, "restar": sub,
              "multiplicar": mul, "dividir": div}

@app.get("/")
def home():
    return jsonify(app="Calculadora basica", operaciones=list(OPERATIONS))

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/calcular")
def calculate():
    try:
        operation = request.args["op"]
        a = float(request.args["a"])
        b = float(request.args["b"])
        if operation not in OPERATIONS or not all(map(math.isfinite, (a, b))):
            raise ValueError("Operacion o numero no valido")
        result = OPERATIONS[operation](a, b)
        if not math.isfinite(result):
            raise ValueError("Resultado fuera de rango")
        return jsonify(resultado=result)
    except (KeyError, ValueError) as error:
        return jsonify(error=str(error)), 400
