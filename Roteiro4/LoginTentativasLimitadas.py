# Iterador para contar as tentivas
iterador = 1

# Senha correta
senha_correta = "positivo50"

# Estrutura de repetição para o usuário ter as tentivas sem encerrar o código
while True:

# Solicitação ao usuario para digitar a senha
    senha_digitada = input("Digite a senha: ")

# Condição caso o usuário acerte a senha
    if senha_digitada == senha_correta:
        print("Senha correta! Acesso concedido.")
        break # Sai do loop quando a senha está correto

# Condição para verificação das tentivas, caso tenha excedido a quantidade ele sai do loop
    elif iterador == 3:
        break

# Caso ele erre, o loop retorna par a origem e incrementa o iterador
    else:
        print("Senha incorreta. Tente novamente.")
        iterador += 1