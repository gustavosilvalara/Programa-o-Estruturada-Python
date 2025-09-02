def fat(n):
    if n == 0:
        return 1
    elif n < 0:
        return ValueError
    else:
        res = 1
        for x in range(1, n):
             res *= x + 1
    return res

def combination(n, k):
# Verificação caso os números forem negativos
    if n < 0 or k < 0:
        return "Informe apenas números positivos"
# Verificação caso "k" seja menor que n
    elif n < k:
        return ("O número total de itens no conjunto,"
                " necessario ser menor do que os itens que você irá escolher para o subconjunto.")
# Formula da combinação, chamando a função fatorial e realizando a divisão
    else:
        res = fat(n) / ((fat(k)) * (fat((n - k))))
        return res

# Solicitação dos dados e chamada das funções para realização do resultado e mostrando o resultado
print("=========================== Cálculador de combinções ===========================\n")
number1 = int(input("Informe o número total de itens no conjunto: "))
number2 = int(input("Informe o número de itens que você quer escolher para o subconjunto: "))
result = combination(number1, number2)
print(f"O total de combinações será de {result}\n")
print("=================================================================================")


