# Gerenciamento de Estoque 
class ProdutoNaoEncontrado(Exception):
    pass

estoque = {}
print("Bem-vindo(a) ao gerenciamento de estoque.")

def adicionar_produto(nome, quantidade):
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade

def ajustar_estoque(nome, quantidade):
    if nome not in estoque:
        raise ProdutoNaoEncontrado(f"O produto '{nome} não foi encontrado no estoque.")
    if estoque[nome] + quantidade < 0:
        raise ValueError("Quantidade insuficiente em estoque.")
    estoque[nome] += quantidade

def gerenciar_estoque():
    while True:
        acao = input("Digite 'adicionar', 'ajustar' ou 'sair': ").lower()
        if acao == 'sair':
            break
        try:
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade: "))

            if acao == 'adicionar':
                adicionar_produto(nome, quantidade)

            elif acao == 'ajustar':
                ajustar_estoque(nome, quantidade)

            else:
                raise ValueError("Ação inválida.")
            
        except ValueError as ve:
            print(f"Erro: {ve}")

        except ProdutoNaoEncontrado as pne:
            print(f"Erro: {pne}")

        else:
            print(f"Estoque atualizado: {estoque}")

        finally:
            print("Operação de estoque concluída.")

gerenciar_estoque()   