def calculadora_v2(num1: float, num2: float, operador: str) -> float:
    operacoes = {
        "**": lambda: num1 ** num2,  
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


    