"""
# Passo 1
dados = {"Endereço" : "Rua Sarim, 0", "Telefone" : 11996660000}
print(dados)
"""
"""
# Passo 2
endereco = input("Digite seu endereço: ")
numero = int(input("Digite seu número: "))
dados = {"Endereço" : endereco, "Telefone" : numero}
"""

# Passo 3
def ledados():
    endereco_lido = input("Digite o Endereço: ")
    while True:
        try:
            telefone = int(input("Digite o número de telefone: "))
            break
        except ValueError:
            print("Digite apenas números")

    registro = {"Endereço" : endereco_lido, "Telefone" : telefone}
    return registro

# Passo 4
agenda = {"Paulo" : ledados()}
#print(agenda)


"""
# Passo 5
print(agenda["Paulo"]["Telefone"])
"""

# Passo 6
def mostraItem(chave):
       registro = agenda.get(chave)
       if registro:
           print(f"\n✅ Dados do Contato: {chave}")
           print(f"   Endereço: {registro['Endereço']}")
           print(f"   Telefone: {registro['Telefone']}")
       else:
               print(f"\n❌ Contato '{chave}' Não Localizado.")

mostraItem("Paulo")
mostraItem("Maria")
