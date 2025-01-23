def calculadora_v4(num1: float, num2: float, operador: str) -> float:
    if num2 == 0 and operador in ['/', '%']:
        return float("nan")

    operacoes = {
        "+": num1 + num2,
        "-": num1 - num2,
        "/": num1 / num2,
        "*": num1 * num2,
        "%": num1 % num2,
        "^": num1 ** num2,
    }

    return operacoes.get(operador, float("nan"))


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
            numero1: float = float(input('Introduza o primeiro número: '))
            numero2: float = float(input('Introduza o segundo número: '))
            operacao: str = input('Introduza a operação a realizar (+ - / * %) ou (^): ')
            print(f'O resultado: {calculadora(numero1, numero2, operacao)}')  # Usa versão 1 por padrão
            print()
            cont: str = input('Deseja continuar? (s/n): ').lower()
            if cont == 'n':
                break

        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')
        