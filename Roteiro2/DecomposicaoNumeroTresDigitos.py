print("==========Decompor um número de três dígitos============\n")

# Solicitação do número para decomposição
number = int(input("Informe um número de três dígitos: "))

# Pegando a centena do número informado, utilzando o // para pegar o quociente inteiro da divisão
hundred = number // 100

# Pegando a dezena do número informado, utilzando o // para pegar o quociente inteiro da divisão e
# removendo a centena, multiplicando o valor pego na variavel hundred por 10 para remover.
dozen = (number // 10) - (hundred * 10)

# Pega a unidade pegando o resto do número dividido por 10
unit = number % 10


print(f"A centena do número é {hundred}, a dezena é {dozen}, a unidade é {unit}")
print("\n========================================================")