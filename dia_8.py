produtos = [
    {"nome": "Laptop", "preço": 3000.00, "quantidade": 10},
    {"nome": "Mouse", "preço": 50.00, "quantidade": 100},
    {"nome": "Teclado", "preço": 150.00, "quantidade": 150},
    {"nome": "Monitor", "preço": 800.00, "quantidade": 50},
    {"nome": "Headphone", "preço": 200.00, "quantidade": 30},
    ]
    
valor_estoque = sum(map(lambda p: p["preço"] * p["quantidade"], produtos))
print(f"Valor total do estoque: R${valor_estoque:.2f}")

limite = 100.00
valor_acima = list(filter(lambda p: p["preço"] > limite, produtos))
print(f"Produtos com preço acima de R${limite:.2f}:")
for produto in valor_acima:
    print(f"{produto["nome"]} - R${produto["preço"]:.2f}")

relatorio = [f"Produto: {p['nome']}, Preço: R${p['preço']:.2f}, Quantidade: {p['quantidade']}"
             for p in produtos]
print("\nRelatório de Produtos:")
for linha in relatorio:
    print(linha)

aumentar = lambda p: {**p, "preço": p["preço"] * 1.10}
com_aumento = [aumentar(p) for p in produtos]
print("\nProdutos com aumento de 10% no preço.")
for produto in com_aumento:
    print(f"{produto['nome']} - R${produto['preço']:.2f}")

baixo_estoque = [p["nome"] for p in produtos if p["quantidade"] < 50]
print("\nProdutos com estoque baixo (menos de 50 unidades):")
for nome in baixo_estoque:
    print(nome)