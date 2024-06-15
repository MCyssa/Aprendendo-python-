# Tipos de Dados e Operações Básicas

lista = [1, 2, 3, 4, 5]

lista.append(6)

lista.remove(3)

sublista = lista[1:4]

print(f"Lista após adicionar: {lista}")
print(f"Sublista: {sublista}")

# manipulação de string
frase = input("Digite uma frase: ")

num = len(frase)
maiuscula = frase.upper()
minuscula = frase.lower()

palavra = "Python"
contem_palavra = palavra in frase

print(f"Número de caracteres: {num}")
print(f"Maiúscula: {maiuscula}")
print(f"Minúscula: {minuscula}")
print(f"A frase contém a palavra '{palavra}'? {contem_palavra}")

# Manupulação de Listas:
 
numeros = input("Digite uma lista de números separados por espaço: ")

# Convertendo para uma lista de inteiros
lista_num = list(map(int, numeros.split()))

soma = sum(lista_num)
media = soma / len(lista_num)

lista_crescente = sorted(lista_num)
lista_decrescente = sorted(lista_num, reverse=True)

print(f"soma: {soma}")
print(f"Média: {media}")
print(f"Lista em ordem crescente: {lista_crescente}")
print(f"Lista em ordem descrescente: {lista_decrescente}")