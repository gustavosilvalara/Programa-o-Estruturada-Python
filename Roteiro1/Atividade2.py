
# Realização da entrada de dados, para saída de dados personalizada

# Solicitação do nome do usuário
name = input("What's your name? ")

# Solicitação da idade do usuário, com a realização do casting para inteiro
age = int(input("How old are you? "))

# Solicitação da cor favorita do usuário
color = input("What is your favorite color? ")

# Saídas com os dados informados

# Exibição dos dados informados pelo usuário com os caracteres de escape com o prinf(f-string)
print(f"=======DATA======= \n Name: {name} \t\n Age: {age} \t\n Favorite Color: {color}\n")

# Exibição dos dados informados pelo usuário com uma frase utilizando sep para separação e end para personalizar o final
# do print
print(f"Very nice", f"your name is {name}", f"you are {age} years old", f"and your favorite color is {color.lower()}",
      end=".\n", sep=", ")



