print("Bem-vindo à lista de produtos.")

def adicionarProduto(lista):
    produto = input("Digite o produto que deseja adicionar: ").title()
    quantidade = int(input("Qual a quantidade desse produto?: "))
    lista[produto] = quantidade
    print("Produto adicionado.")

def removerProduto(lista):
    produto = input("Digite o produto que deseja excluir: ").title()
    if produto in lista: 
        lista.pop(produto)
        print("Produto removido.")
    else:
        print("Produto não encontrado.")

def salvarProduto(lista, dia_6_2):
    try:
        with open(dia_6_2, 'w') as arquivo:
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
            print("3. Salvar e sair.")
            escolha = input("Digite sua escolha: ")

            if (escolha == '1'):
                adicionarProduto(lista)

            elif (escolha == '2'):
                removerProduto(lista)

            elif (escolha == '3'):
                opcao = input("Você deseja salvar seus contatos em um arquivo? (s|N): ").lower()
                if (opcao == 's'):
                    dia_6_2 = 'dia_6_2.txt'
                    salvarProduto(lista, dia_6_2)
                    print("Finalizando programa, seu produto foi adicionado no arquivo!\n")
                else: 
                    print("Erro.")
                break
    except Exception as e:
        print(f'Erro: {e}!\n')

menuPrincipal()
        
                
        
                
            
    