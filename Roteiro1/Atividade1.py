# Realização da entrada de dados, para saída de dados personalizada

# Solicitação do nome do usuário
name = input("What's your name? ")

# Solicitação da idade do usuário, com a realização do casting para inteiro
age = int(input("How old are you? "))

# Solicitação da altura do usuário, com a realização do casting para float
height = float(input("How tall are you? "))

# Solicitação da cidade do usuário
city = input("What is your city? ")

# Solicitação da profissão do usuário
profession = input("What is your profession? ")

# Exibição dos dados utilizndo print(f-string) e realizando a formatação dos números inteiros para 3 decimais e dos
# numeros reais (floats) para 2 casas após a virgula e utilização do lower para a profissão sempre ser imprimida em
# caixa baixa
print(f"Hello, your name is {name}, your are {age:03d} years, your height is {height:.2f}, you live in {city},"
      f" your profession is {profession.lower()}\n")

# Exibição do nome e da cidade com a separação por um traço utilizando o sep
print(f"Your name and city is {name}", f"{city}", sep="-")

