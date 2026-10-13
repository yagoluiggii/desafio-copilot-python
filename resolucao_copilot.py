def concatenar_dados():
    """1 - Receber dois dados do usuário e concatená-los"""
    print("\n--- 1. Concatenando Dados ---")
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    resultado = dado1 + " " + dado2
    print(f"Resultado da concatenação: {resultado}")

def repetir_texto():
    """2 - Repetir uma string um determinado número de vezes"""
    print("\n--- 2. Repetindo Texto ---")
    texto = input("Digite o texto que deseja repetir: ")
    vezes = int(input("Digite a quantidade de vezes: "))
    resultado = (texto + " ") * vezes
    print(f"Resultado da repetição: {resultado.strip()}")

def operacoes_matematicas():
    """3 - Realizar operações matemáticas simples entre dois números"""
    print("\n--- 3. Operações Matemáticas Simples ---")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2 if num2 != 0 else "Divisão por zero não permitida"

    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")

if __name__ == "__main__":
    print("=== PROJETO PYTHON COM GITHUB COPILOT ===")
    concatenar_dados()
    repetir_texto()
    operacoes_matematicas()