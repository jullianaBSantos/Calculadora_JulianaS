def calculadora_v3(num1: float, num2: float, operador: str) -> float:
    operadores = {
        "+": operator.add,
        "-": operator.sub,
        "/": operator.truediv,
        "*": operator.mul,
        "%": operator.mod,
        "^": operator.pow,
    }

    if operador in operadores:
        return operadores[operador](num1, num2)

    return float("nan")
