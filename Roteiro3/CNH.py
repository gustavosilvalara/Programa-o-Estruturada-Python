# Solicita a data de hoje ao usuário
print("Digite a data de hoje:")
dia_hoje = int(input("Dia: "))
mes_hoje = int(input("Mês: "))
ano_hoje = int(input("Ano: "))

# Solicita a data de nascimento ao usuário
print("\nDigite a sua data de nascimento:")
dia_nasc = int(input("Dia: "))
mes_nasc = int(input("Mês: "))
ano_nasc = int(input("Ano: "))

# Calcula a idade
# A idade é a diferença entre o ano atual e o ano de nascimento
idade = ano_hoje - ano_nasc

# Verifica se a pessoa pode tirar a CNH
if idade >= 18:
    print(f"\nVocê tem {idade} anos. Parabéns, você já tem idade suficiente para tirar a CNH!")
else:
    print(f"\nVocê tem {idade} anos. Infelizmente, você ainda não tem idade para tirar a CNH.")
