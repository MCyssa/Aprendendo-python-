import dia_5_1

print("Bem-vindo a calculadora simples.")
print("1. Para somar.")
print("2. Para subtrair.")
print("3. Para multiplicar.")
print("4. Para dividir.")

escolha = input("Escolha uma das opções: ")

if (escolha == '1'):
    dia_5_1.soma()

elif (escolha == '2'):
    dia_5_1.sub()

elif (escolha == '3'):
    dia_5_1.multi()

elif (escolha == '4'):
    dia_5_1.div()
else:
    print("Ocorreu um erro.")