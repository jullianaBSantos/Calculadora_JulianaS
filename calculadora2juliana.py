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

# Teste

print(calculadora_v2(2, 3, "**"))  # 8
print(calculadora_v2(2, 3, "+"))  # 5
print(calculadora_v2(2, 3, "-"))  # -1
print(calculadora_v2(2, 3, "/"))  # 0.6666666666666666
print(calculadora_v2(2, 3, "*"))  # 6


    