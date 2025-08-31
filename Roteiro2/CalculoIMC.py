#Função que calcula o IMC e retorna o valor
def calculo_imc(weight_param, height_param):
    return weight_param / height_param ** 2

print("======================Cálculo de IMC======================\n")
# Solicita o peso
weight = float(input("Infome o seu peso: "))
# Solicita a altura
height = float(input("Informe sua altura: "))
# Chama a função para calcular o IMC
imc = calculo_imc(weight, height)
# Verificação de como está o peso e a saída de dados para o usuário
if imc < 18.5:
    print(f"IMC: {imc:.2f}, está a baixo do peso saudável")
elif imc < 25:
    print(f"IMC: {imc:.2f}, está com o peso saudável")
elif imc < 30:
    print(f"IMC: {imc:.2f}, está com excesso de peso")
elif imc < 35:
    print(f"IMC: {imc:.2f}, está com obesidade")
else:
    print(f"IMC: {imc:.2f}, está com obesidade extrema")
print("\n==========================================================")