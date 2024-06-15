print("Bem-vindo à lista de produtos.")

def adicionarProduto(lista):
    produto = input("Digite o produto que deseja adicionar: ").title()
    quantidade = int(input("Qual a quantidade desse produto?: "))
    lista[produto] = quantidade
    print("Produto adicionado.")

def removerProduto(lista):
    try:
        produto = input('Digite o nome do produto que deseja excluir: ').title()
        if produto in lista:
            lista.pop(produto)
            print("O produto foi excluido!\n")
        else:
            print("Produto não encontrado!\n")

    except Exception as e:
        print(f"Erro: {e}\n")

def visualizarProduto(lista):
    if lista:
        print("Lista de produtos")
        for produto, quantidade in lista.items():
            print(f"{produto}: {quantidade}")

    else:
        print("A lista de produtos está vazia.\n")

def salvarProduto(lista, dia06_2):
    try:
        with open(dia06_2, 'w') as arquivo:
            for produto in sorted(lista.keys()):
                quantidade = lista[produto]
                arquivo.write(f"{produto}: {quantidade}\n") 
            print("Produtos salvos.")
    except IOError:
        print("Erro ao salvar produtos no arquivo.\n")
         
 
def menuPrincipal():
    try: 
        lista = {}

        while True:
            print("1. Adicionar produto.")
            print("2. Remover produto.")
            print("3. Visualizar produtos.")
            print("4. Salvar e sair.")
            escolha = input("Digite sua escolha: ")

            if (escolha == '1'):
                adicionarProduto(lista)

            elif (escolha == '2'):
                removerProduto(lista)

            elif (escolha == '3'):
                visualizarProduto(lista)

            elif (escolha == '4'):
                opcao = input("Você deseja salvar seus contatos em um arquivo? (s|N): ").lower()
                if (opcao == 's'):
                    dia06_2 = 'dia06_2.txt'
                    salvarProduto(lista, dia06_2)
                    print("Finalizando programa, seu produto foi adicionado no arquivo!\n")
                else: 
                    print("Programa encerrado.")
                break
    except Exception as e:
        print(f'Erro: {e}!\n')

menuPrincipal()
        
                
        
                
            
    