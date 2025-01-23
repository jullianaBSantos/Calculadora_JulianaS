def calculadora_v2(num1: float, num2: float, operador: str) -> float:
    operacoes = {
        "**": lambda: num1 ** num2,  # Exponenciação
        "+": lambda: num1 + num2,
        "-": lambda: num1 - num2,
        "/": lambda: num1 / num2,
        "*": lambda: num1 * num2,
        "%": lambda: num1 % num2,
        "^": lambda: num1 ** num2,
    }
    if operador not in operacoes:
        raise ValueError(f"Operador '{operador}' não é suportado.")

    funcao = operacoes.get(operador)
    if funcao:
        return funcao()

    return float("nan")

    def calculadora_v3(num1: float, num2: float, operador: str) -> float:
    if operador in ['+', '-', '*', '/', '%', '^']:
        return eval(f"{num1} {operador} {num2}")
    else:
        raise ValueError(f"Operador '{operador}' não é suportado.")