import sys
import random
import math
import os
from faker import Faker

# 1. Informações do sistema (Opcional, mas recomendado)
print("\n--- Informações do Sistema ---")
print(f"Caminho do executável Python: {sys.executable}")
print("Diretórios de busca de módulos (sys.path):")
for i, p in enumerate(sys.path):
    print(f"  {i + 1}. {p}")
print("------------------------------\n")

# 2. Gerador de dados fictícios
# Cria uma instância da classe Faker com localidade 'pt_BR'
faker = Faker('pt_BR')

# 3. Criação da agenda fictícia
agenda_ficticia = []
NUM_REGISTROS = 10

print(f"--- Gerando {NUM_REGISTROS} Registros ---")

for i in range(NUM_REGISTROS):
    # a. Gera dados fictícios
    nome = faker.name()
    endereco = faker.address()
    email = faker.email()

    # b. Gera duas notas aleatórias (entre 0 e 10, inclusivo)
    nota1 = random.uniform(0.0, 10.0)
    nota2 = random.uniform(0.0, 10.0)

    # c. Calcula a média geométrica
    # Média Geométrica = sqrt(x * y)
    # Lógica para garantir que a média seja 0 se alguma nota for 0
    if nota1 == 0.0 or nota2 == 0.0:
        media_geometrica = 0.0
    else:
        # A média geométrica de dois números positivos é sqrt(produto)
        produto = nota1 * nota2
        media_geometrica = math.sqrt(produto)

    # d. Cria o dicionário para o registro
    registro = {
        "Nome": nome,
        "Endereço": endereco,
        "Email": email,
        "Notas": (nota1, nota2),
        "Média Geométrica": media_geometrica
    }

    # e. Adiciona o dicionário à lista
    agenda_ficticia.append(registro)

    # f. Imprime mensagem de confirmação
    print(f"Registro {i + 1} gerado: {nome}")

# 5. Exibição dos registros
print("\n\n=== AGENDA FICTÍCIA COMPLETA ===")

for i, registro in enumerate(agenda_ficticia):
    # Usa um separador para organizar a exibição de cada registro
    print(f"\n################## REGISTRO {i + 1} ##################")

    # Exibe as informações
    print(f"Nome: {registro['Nome']}")
    print(f"Endereço: {registro['Endereço']}")
    print(f"Email: {registro['Email']}")

    # Formata as notas e a média geométrica com duas casas decimais
    nota_a = registro['Notas'][0]
    nota_b = registro['Notas'][1]
    media = registro['Média Geométrica']

    print(f"Notas: ({nota_a:.2f}, {nota_b:.2f})")
    print(f"Média Geométrica: {media:.2f}")

print("\n================ FIM DA AGENDA ================\n")