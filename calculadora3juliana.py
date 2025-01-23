def calculadora_v3(num1: float, num2: float, operador: str) -> float:
   
    operadores = {
        "+": operator.add,
        "-": operator.sub,
        "/": operator.truediv,
        "*": operator.mul,
        "%": operator.mod,
        "^": operator.pow,
    }

    try:
        if operador in operadores:
            return operadores[operador](num1, num2)
        else:
            print("Operador inválido. Use um dos seguintes: +, -, *, /, %, ^")
            return float("nan")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
        return float("nan")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return float("nan")


resultado = calculadora_v3(10, 0, "/")
print(resultado)

