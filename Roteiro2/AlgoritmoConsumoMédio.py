print("==============Calculo de consumo médio de seu veículo==============\n")
# Solicita a quantidade de km percorrido
km = int(input("Informe quantos quilómetros o senhor dirigiu seu veículo: "))

# Solicita a quantidade de combusível abastecido pela última vez
fuel = float(input("Informe quantos lítros de combustível o senhor abasteceu: "))

# Calculo de consumo de gasolina por km
consumption = km / fuel

# Mensagem de saída das informações
print(f"O veículo do senhor(a) está realizando {consumption:.2f} km por litro")

print("\n====================================================================")
