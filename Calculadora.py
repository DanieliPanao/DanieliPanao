print("\n******* Calculadora em Python *******")


def soma(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


print("Selecione o número da operação desejada:")

print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")

opcao = int(input("Digite sua opção (1/2/3/4): "))

if opcao == 1:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print(a, '+', b, '=', soma(a, b))
elif opcao == 2:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print(a, '-', b, '=', subtrair(a, b))
elif opcao == 3:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print(a, '*', b, '=', multiplicacao(a, b))
elif opcao == 4:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print(a, '/', b, '=', divisao(a, b))
else:
    print('Opção Inválida!')