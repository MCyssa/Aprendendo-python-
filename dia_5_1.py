# Teste de pacotes e módulos
def soma():
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))
    r = a + b
    print(r)

def sub():
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))
    r2 = a - b
    print(r2)


def multi():
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))
    r3 = a * b
    print(r3)



def div():
    a = float(input("Digite um número: "))
    b = float(input("Digite outro número: "))

    if b != 0:
        r4 = a / b
        print(r4)
    else:
        print("Erro: divisão por 0.")
    
