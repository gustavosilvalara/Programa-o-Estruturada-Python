# Função para cálculo total dos itens da lista
def calculo_total(lista = ()):
    soma = sum(lista)
    return soma
# Função para achar o maior valor da lista
def venda_maxima(lista = ()):
    maxima = max(lista)
    return maxima
# Função para achar o menor valor da lista
def venda_minima(lista = ()):
    minima = min(lista)
    return minima
# Função para achar a média dos valores da lista utilizando a função do cálculo total
def media_vendas(lista = ()):
    media = (calculo_total(lista)) / len(lista)
    return media


# Inicialização da lista e menu interativo com uma variável para armazenar a opção escolhida
print("==================== Análisador de vendas ====================")
lista_venda = []
while True:
    print("\n1 - Adicionar vendas do dia")
    print("2 - Venda total")
    print("3 - Venda máxima")
    print("4 - Venda mínima")
    print("5 - Média das vendas")
    print("0 - Finalizar")
# Variável das opções com tratamento de exceção caso o usuário digite um texto
    try:
        opcao = int(input("Digite aqui: "))
    except ValueError:
        print("Digite um número de 1 a 0")
        continue
# Condicional para cada opção escolhida
    match opcao:
        case 1:
# Caso a variável seja 1 solicita o valor da venda e adiciona a lista com tratamento de exceção caso o usuário digite
# um texto
            try:
                venda = float(input("Informe o valor da venda: "))
                lista_venda.append(venda)
            except ValueError:
                print("Informe números")
# Caso a variável seja 2 ele chama a função que retorna o cálculo total da lista com tratamento de exceção caso a lista
# esteja vazia
        case 2:
            try:
                print(f"O Total do valor das vendas foram: {calculo_total(lista_venda):.2f}.")
            except IndexError:
                print("Necessario adicionar uma venda")
# Caso a variável seja 3 chama a função que retorna o maior número da lista com tratamento de exceção caso a lista
# esteja vazia
        case 3:
                try:
                    print(f"A venda máxima foi {venda_maxima(lista_venda):.2f}.")
                except IndexError:
                    print("Necessario adicionar uma venda")
# Caso a variável seja 4 chama a função que retorna o menor número da lista com tratamento de exceção caso a lista
# esteja vazia
        case 4:
            try:
                print(f"A venda mínima foi: {venda_minima(lista_venda):.2f}.")
            except IndexError:
                print("Necessario adicionar uma venda")
# Caso a variável seja 5 chama a função que retorna a média dos valores da lista com tratamento de exceção caso a lista
# esteja vazia
        case 5:
            try:
                print(f"A média do valor das vendas foi {media_vendas(lista_venda):.2f}.")
            except IndexError:
                print("Necessario adicionar vendas")
# Caso a variável seja 0 encerra o menu é o programa
        case 0:
            print(f"Encerrado com sucesso.")
            break
# Caso digite um valor que não está nos casos ele retorna essa opção e retorna para o menu
        case _:
            print("Escolha uma das opções")