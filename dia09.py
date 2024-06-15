nome = input("Qual seu nome completo?: ").title()
posicao = nome.find(" ")
primeiro_nome = nome[:posicao]
print(f"Olá, {primeiro_nome}! Vamos começar o processamento de confirmação de email.")

email = input("Digite seu email: ").lower()
posicao = email.find("@")

if posicao != -1:
    servidor = email[posicao:]
    primeira = email[:1]
    ultimas = email[4:posicao]
    print(f"Seu email {primeira}****{ultimas}{servidor} foi cadastrado com sucesso.")

else:
    print("Erro: email incorreto.")

