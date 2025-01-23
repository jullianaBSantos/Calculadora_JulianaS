import os
import time
import operator


def calculadora(num1: float, num2: float, operador: str) -> float:
    resultado = float("nan")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            raise ValueError("Não é possível dividir por zero.")
    elif operador == '%':
        resultado = num1 % num2
    elif operador == '^':
        resultado = num1 ** num2
    else:
        raise ValueError(f"Operador '{operador}' não é suportado.")
    return resultado