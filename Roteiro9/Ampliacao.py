# Variável da agenda
agenda = {}

# Função para criar um item
def criaItem():
    nome = input("Digite o nome do contato: ")
    endereco_lido = input("Digite o Endereço: ")
    while True:
        try:
            telefone = int(input("Digite o número de telefone: "))
            break
        except ValueError:
            print("Digite apenas números")

    dado = {"Endereço": endereco_lido, "Telefone": telefone}
    return nome, dado

# Função para remoção do item
def removeItem(chave):
    dado_remover = agenda.get(chave)
    if dado_remover:
        agenda.pop(chave)
        print(f"{chave} foi removido da agenda com sucesso\n")
    else:
        print("Contato não localizado!!\n")
# Menu interativo
while True:
    print("  Escolha uma opção  ")
    print(" 1. Criar agenda")
    print(" 2. Mostrar item")
    print(" 3. Criar item")
    print(" 4. Remover item")
    print(" 5. Mostrar todos os itens")
    print(" 6.  Sair")

    opcao = int(input("Opção: "))
# Criação da Agenda
    if opcao == 1:
        agenda.copy()
        print("Agenda Criada\n")
# Visualização de um contato específico
    if opcao == 2:
        if len(agenda) == 0:
            print("A agenda está vazia, adicione contatos para visualizar\n")
        else:
            item = input("Digite o contato que deseja visualizar: ")
            registro = agenda.get(item)
            if registro:
                print(f"\n✅ Dados do contato {item}")
                print(f"    Endereço {registro["Endereço"]}")
                print(f"    Telefone {registro["Telefone"]}\n")
            else:
                print(f"❌ Contato {item} não localizado\n")
# Criação de um contato
    if opcao == 3:
        nome, dados = criaItem()
        agenda[nome] = dados
# Remoção de contato
    if opcao == 4:
        if len(agenda) == 0:
            print("A agenda está vazia, adicione contatos para visualizar\n")
        else:
            remover_agenda = input("Digite o contato que deseja remover: ")
            removeItem(remover_agenda)
# Visualização de todos os elementos da agenda
    if opcao == 5:
        if len(agenda) == 0:
            print("A agenda está vazia, adicione contatos para visualizar\n")
        else:
            print(agenda)
    if opcao == 6:
        print("Finalizando o programa!!!!!\n")
        break