print("Conversor de decimal para bínario\n")
# Solicita o número que será convertido
number = int(input("Informe um número decimal de 0 ate 15: "))

# Realiza a validação do número
if number > 15 or number < 0:
# Saída caso esteja incorreto
    print("Valor incorreto, o número precisa ser de 0 ate 15")
# Condicional caso esteja tudo certo
else:
    # Variável utilizada para formar o número binário
    binary = ""

    # Laço de repetição para realizar a conversão até o final
    while number > 0:
        # Pegando o resto dos números para conversão
        rest = number % 2
        # Utilizando o casting na variavel rest para string e concatenando a variável binary no
        # começo da string
        binary = str(rest) + binary
        # Realizando a divisão para conseguir continuar a conversão
        number = number // 2
    print(binary)

