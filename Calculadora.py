print("\n******* Calculadora em Python - Danieli Fernandes Neves Panão*******")


def soma(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


def cubo(a):
    return a * a * a


print("Selecione o número da operação desejada:")

print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Elevar ao Cubo")

opcao = int(input("Digite sua opção (1/2/3/4/5): "))

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
    a = int(input("Digite o primeiro número para divisão: "))
    b = int(input("Digite o segundo número para divisão: "))
    print(a, '/', b, '=', divisao(a, b))
elif opcao == 5:
    a = int(input("Digite o número para ser elevado ao cubo: "))
    print(a, '*', a, '*', a, '=', cubo(a))
else:
    print('Opção Inválida, tente novamente!')