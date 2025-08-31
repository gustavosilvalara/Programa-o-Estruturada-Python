# Iterador para conseguirmos utilizar o while ate 5 números pares
iterador = 0

# Lista para adicionar os valores pares
lista_pares = []

print("==============Digite 5 números pares==============")

# Estrutura de repetição com a condição para continuar até a variavel chegar em 5
while iterador != 5:

# Solicitação de número para o usário
    valor = int(input("Digite aqui: "))

# Condicional para verificar se o número é par
    if valor % 2 == 0:

# Adicionando a lista
        lista_pares.append(valor)

# Incrementando o iterador para não ficar no loop infinito
        iterador += 1
print(f"Os números pares digitados foram {lista_pares}")
print("=======================Fim=======================")