print("==========Soma dos primeiros números inteiros==========")
# Solicita o número para o usuário
n = int(input("Informe o número: "))

# Variavel para somar os números
res = 0

# Estrutura de repetição para iterar de 1 ate n
# O loop vai ate n + 1 para incluir o n
for i in range(1, n + 1):

# Variavel atribuindos os valores e somando com os quais já estão na variável
    res += i

# Saída de dados
print(f"A soma de todos os números de 1 até {n} é: {res}")

