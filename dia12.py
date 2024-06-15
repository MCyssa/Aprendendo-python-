# Interface de linha de comando para o usuário interagir com o gerenciador de tarefas
import json

tarefas = []

def carregarTarefas(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvarTarefas(filename):
    with open(filename, 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def adicionarTarefa():
    tarefa = input("Digite o nome da tarefa: ").title()
    descricao = input("Descreva a tarefa: ").lower()
    tarefas.append({'Tarefa': tarefa, 'Descrição': descricao, 'completed': False})
    salvarTarefas('tarefas.json')
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def removerTarefa(tarefa_index):
    try:
        tarefa = tarefas.pop(tarefa_index)
        salvarTarefas('tarefas.json')
        print(f"Tarefa '{tarefa['Tarefa']}' removida com sucesso!")
    except IndexError:
        print("Ìndice de tarefa inválido.")

def listarTarefas():
    if not tarefas:
        print("O arquivo está vazio!")
        return
    
    for index, tarefa in enumerate(tarefas):
        status = "Concluída" if tarefa['completed'] else "Pendente"
        print(f"{index}: {tarefa['Tarefa']} - {tarefa['Descrição']} - {status}")

def completarTarefa(tarefa_index):
    try:
        tarefas[tarefa_index]['completed'] = True
        salvarTarefas('tarefas.json')
        print(f"Tarefa '{tarefas[tarefa_index]['Tarefa']}' marcada como concluída.")
    except IndexError:
        print("Ìndice de tarefa inválido.")

def editarTarefa(tarefa_index):
    try:
        edicao = input("1. Editar Tarefa ou 2. Editar Descrição: ")
        if edicao == '1':
            nova_tarefa = input("Digite o novo nome da Tarefa: ")
            tarefas[tarefa_index]['Tarefa'] = nova_tarefa
            salvarTarefas('tarefas.json')
            print(f"Tarefa '{tarefa_index}' editada com sucesso!")

        elif edicao == '2':
            nova_descricao = input("Digite a nova descrição: ")
            tarefas[tarefa_index]['Descrição'] = nova_descricao
            salvarTarefas('tarefas.json')
            print(f"Tarefa '{tarefa_index}' editada com sucesso!")

        else:
            print("Valor inválido.")
    except IndexError:
        print("Ìndice de tarefa inválido.")

def main():
    global tarefas
    tarefas = carregarTarefas('tarefas.json')

    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Listar Tarefas")
        print("4. Marcar Tarefa como Concluída")
        print("5. Editar Tarefa ou Descrição")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionarTarefa()

        elif escolha == '2':
            tarefa_index = int(input("Digite o índice da tarefa a ser removida: "))
            removerTarefa(tarefa_index)

        elif escolha == '3':
            listarTarefas()

        elif escolha == '4':
            tarefa_index = int(input("Digite o índice da tarefa a ser concluída: "))
            completarTarefa(tarefa_index)

        elif escolha == '5':
            tarefa_index = int(input("Digite o índice da tarefa a ser editada: "))
            editarTarefa(tarefa_index)
            
        elif escolha == '6':
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida, tente novamente!")

if __name__ == "__main__":
    main()
