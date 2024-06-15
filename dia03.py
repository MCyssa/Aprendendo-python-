# Adivinhe o número!
import random

numero_secreto = random.randint(1, 100)
tentativa = None

print("Adivinhe o número entre 1 e 100.")

while tentativa != numero_secreto:
    tentativa = int(input("Digite sua tentativa: "))

    if tentativa < numero_secreto:
        print("Muito baixo!")
    elif tentativa > numero_secreto:
        print("Muito alto!")
    else:
        print("Parabéns! Você acertou o número.")

print("Concluiu o primeiro jogo. Agora começará o Jogo da Forca.")
# Jogo da Forca
import random

palavras = ["python", "programacao", "jogo", "computador", "internet", "arquivos"]

palavra_secreta = random.choice(palavras)
tentativas = 6
letras_adivinhadas = []

print("Bem-vindo ao jogo da Forca!")
print("_ " * len(palavra_secreta))

while tentativas > 0:
    letra = input("Digite uma letra: ").lower()
    
    if letra in letras_adivinhadas:
        print("Você já tentou essa letra. Tente novamente.")
        continue
    
    letras_adivinhadas.append(letra)
    
    if letra in palavra_secreta:
        print("Acertou!")
    else:
        tentativas -= 1
        print(f"Errou! Você tem {tentativas} tentativas restantes.")
    
    palavra_parcial = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_adivinhadas:
            palavra_parcial += letra_secreta + " "
        else:
            palavra_parcial += "_ "
    
    print(palavra_parcial)
    
    if "_" not in palavra_parcial:
        print("Parabéns! Você ganhou!")
        break
else:
    print(f"Game over! A palavra era {palavra_secreta}.")