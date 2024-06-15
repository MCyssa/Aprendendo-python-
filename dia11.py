# Utilizando a biblioteca 'requests' para fazer uma requisição HTTP.

import requests

def obter_dados(url):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        print("Requisição bem-sucedida.")
        return resposta.json()  
    else:
        print(f"Erro na requisição: {resposta.status_code}")

url = "https://api.github.com"
dados = obter_dados(url)
print(dados)

# Utilizando a biblioteca para manipular dados.
import pandas as pd

def adicionar_aluno(dataframe):
    nome = input("Digite o nome do aluno: ").title()
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Digite a nota do aluno: "))

    novo_aluno = pd.DataFrame({'Nome': [nome], 'Idade': [idade], 'Nota': [nota]})
    dataframe = pd.concat([dataframe, novo_aluno], ignore_index=True)
    return dataframe

def listar_alunos(dataframe):
    if dataframe.empty:
        print("Lista vazia. Cadastre um aluno.")
    else:
        print(dataframe)

def media_notas(dataframe):
    if dataframe.empty:
        print("Nenhuma há notas para calcular a média.")
    else:
        media = dataframe["Nota"].mean()
        print(f"A média das notas é: {media:.2f}")

def gerenciar_alunos():
    df_alunos = pd.DataFrame(columns=["Nome", 'Idade', 'Nota'])

    while True:
        print("\ngerenciador de Alunos")
        print("1. Adicionar Aluno")
        print("2. Listar Alunos")
        print("3. Calcular média das Notas")
        print("4. Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            df_alunos = adicionar_aluno(df_alunos)
            
        elif escolha == '2':
            listar_alunos(df_alunos)
            
        elif escolha == '3':
            media_notas(df_alunos)

        elif escolha == '4':
            print("Programa encerrado.")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    gerenciar_alunos()




