 # Calculadora simples 
print("Bem-vindo a calculadora!")

def soma():
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    r = n1 + n2
    print(f"O resultado é: {r}\n")

def subtracao():
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    r = n1 - n2
    print(f"O resultado é: {r}\n")

def multiplicacao():
    n1 = int(input("Digite um número "))
    n2 = int(input("Digite outro número: "))
    r = n1 * n2
    print(f"O resultado é: {r}\n")

def divisao():
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))

    if n2 != 0:
        r = n1 / n2
        print(f"O resultado é: {r}\n")
    else:
        print("Erro: Divisão por 0.\n")

def caclular_media():
    lista = input("Digite uma lista de números: ")
    numeros = [float(x) for x in lista.split()]
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    print(f"A média dos números é: {media}\n")

def fatorial():
    num = int(input("Digite um número para fatorar: "))
    if num == 0 or num == 1:
        print(f"O fatorial de {num} é: 1\n")
    else:
        resultado = 1
        for i in range(2, num + 1):
            resultado *= i
        print(f"O fatorial de {num} é: {resultado}\n")

def menuPrincipal():
    try:
        while True:
            print("1. Para somar. ")
            print("2. Para subtrair.")
            print("3. Para multiplicar.")
            print("4. Para dividir.")
            print("5. Para calcular a média.")
            print("6. Para fatorar.")
            print("Qualquer outro valor para encerrar o programa.")
            escolha = input("Escolha uma opção: ")

            if (escolha == '1'):
                soma()

            elif (escolha == '2'):
                subtracao()

            elif (escolha == '3'):
                multiplicacao()

            elif (escolha == '4'):
                divisao()

            elif (escolha == '5'):
                caclular_media()

            elif (escolha == '6'):
                fatorial()

            else:
                print("Programa encerrado.")
                break
    
    except Exception as e:
        print(f'Erro: {e}!\n')

menuPrincipal()


    


