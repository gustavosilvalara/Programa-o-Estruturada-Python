tarefas = []

while True:
# Menu para escolha
    print("\nDigite uma opção")
    print("1 - Adicionar uma tarefa")
    print("2 - Visualizar todas as tarefas")
    print("3 - Marcar uma tarefa como concluída")
    print("4 - Sair do programa")
# Variável para coleta da opção
    opcao = int(input("\nDigite: "))
# Condição para encerramento do programa
    if opcao == 4:
        break
# Condição para adicionar tarefas
    elif opcao == 1:
        adicionar = input("Qual tarefa deseja adicionar: ")
        tarefas.append(adicionar)
# Visualização caso a lista tenha tarefas
    elif opcao == 2 and len(tarefas) > 0:
        print(tarefas)
# Visualização caso a lista não tenha tarefas
    elif opcao == 2 and len(tarefas) <= 0:
        print("É necessario adicionar tarefas para visualiza-las")
# Marcação de concluída caso a tenha tarefas na lista
    elif opcao == 3 and len(tarefas) > 0:
        remover = input("Qual tarefa deseja marcar como concluída: ")
# Verificação se a palavra digita pela usuário foi adicionada antes de remover
        if not tarefas.__contains__(remover):
            print("A tarefa não foi adicionada")
        else:
            tarefas.remove(remover)
# Marcação caso não tenha tarefas na lista
    elif opcao == 3 and len(tarefas) <= 0:
        print("É necessario adicionar tarefas para concluí-la")
