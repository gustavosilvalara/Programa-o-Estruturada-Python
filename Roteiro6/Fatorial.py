def fat(n):
# Validação caso o número for 0
    if n == 0:
        return 1
# Validação caso o número for negativo
    elif n < 0:
        return ValueError
# Validação caso o número seja maior que 0
    else:
# Variável que armazena o resultado
        res = 1
# Realização da fatoração
        for x in range(1, n):
             res *= x + 1
    return res

print("======================== Fatorização ========================\n")
number = int(input("Informe um valor para realizar a fatorização: "))
result = fat(number)
print(f"O resultado é {result}\n")
print("=============================================================")

