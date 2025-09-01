print("=============Verificação de número primo=============")
# Solicitação de dado para o usuário
n = int(input("Digite um número para verificação: "))

# Verificação se "n" é o número 1 ou 2
if n == 1:
    print(f"O número {n}, não é primo")
elif n == 2:
    print(f"O número {n} e par")
else:

# For para verifição, caso o número for divisivel por um número o for para automaticamente
    for a in range(1, n):
    # Caso o a seja diferente de 2 ele continua o for
        if a != 2:
            continue
    # Caso o resto de "n" dividido por "a" seja 0 mas que a seja diferente de 1 ele retorna essa mensagem
        elif n % a == 0:
            print(f"O número {n}, não é primo")
    # Caso ele não entre na condicional acima o número seja ímpar
        else:
            print(f"O numero {n} é primo, é divisível apenas por 1 e ele mesmo")