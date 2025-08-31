# Função para verificar se é um triângulo
def calcular_lado(lado1, lado2, lado3):
    if lado1 + lado2 < lado3:
        return False
    elif lado1 + lado3 < lado2:
        return False
    elif lado2 + lado3 < lado1:
        return False
    else:
        return True

# Solicita os lados para o usuário
lad1 = int(input("Digite o primeiro lado de um triânglo: "))
lad2 = int(input("Digite o segundo lado de um triânglo: "))
lad3 = int(input("Digite o terceiro lado de um triânglo: "))

# Chamando a função para verificação
verificacao_triangulo = calcular_lado(lad1, lad2, lad3)

# Caso a função retorne false ele imprimi a mensagem do if
if not verificacao_triangulo:
    print("Não e possivel formar um triângulo com o valor dos lados...")
# Caso a função retorne true ele realiza a classificação do triângulo
else:
    # Verificação do equilátero
    if lad1 == lad2 and lad1 == lad3:
        print("O triângulo é equilátero...")
    # Verificação do isósceles
    elif lad1 == lad2 or lad1 == lad3 or lad2 == lad3:
        print("O triângulo é isósceles...")
    # Caso não seja nenhum ele classifica como escaleno
    else:
        print("O triângulo será escaleno")