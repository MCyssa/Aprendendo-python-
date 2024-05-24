"""Fundamentos em python
Variáveis, prints e scripts simples"""

#script simples
print ("Hello, world!")

# Variáveis
mensagem = "Esta é a primeira aula em python!"
numero = 1000
pi = 3,14159

# Imprimindo variáveis

print (mensagem)
print (numero)
print (pi)

#exercício

nome = "Julia"
idade = 30
cidade = "Florianópolis"

print (f"Nome: {nome}")
print (f"Idade: {idade}")
print (f"Cidade: {cidade}")

# operações básicas
num1 = int(input("digite um número: "))
num2 = int(input("digite outro numero: "))

soma = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2

print (soma)
print (sub)
print (multi)
print (div)

# concatenando strings
str1 = "Olá"
str2 = "Mundo"

resultado = str1 + " " + str2
print (resultado)

# programa extra para treinar: analisador de texto

texto = input("Digite uma frase ou texto: ")

palavras = texto.split()

num_palavras = len(palavras)

palavra_mais_longa = max(palavras, key=len)

texto_invertido = ' '.join(palavras[::-1])

print(f"Número de palavras: {num_palavras}")
print(f"Palavras mais longa: {palavra_mais_longa}")
print(f"Texto com palavras em ordem invertida: {texto_invertido}")