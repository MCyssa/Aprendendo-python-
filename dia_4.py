# Gerador de senhas
print("Gerador de senhas")
import random 
import string 

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

tamanho = int(input("Digite o tamanho da senha: "))

senha = gerar_senha(tamanho)
print(f"A senha gerada é: {senha}")

# Calculador de fatorial
print("Iniciando fatoração")
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fatorial = 1 
        for i in range(2, n + 1):
            fatorial *= i
        return fatorial 

num = int(input('Digite um número:'))
print(f"O fatorial de {num} é {fatorial(num)}")

# Para calcular a média dos números
print("Programa de fatoração concluído! Iniciando o cálculo de média.")
def calcular_media(numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media

lista = input("Digite uma lista de números: ")
numeros = [int(x) for x in lista.split()]

media = calcular_media(numeros)

print(f"Média dos numeros: {media}")