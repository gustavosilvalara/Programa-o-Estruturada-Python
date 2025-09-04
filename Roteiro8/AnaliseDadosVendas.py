def calculo_total(lista = ()):
    soma = sum(lista)
    return soma
def venda_maxima(lista = ()):
    maxima = max(lista)
    return maxima
def venda_minima(lista = ()):
    minima = min(lista)
    return minima
def media_vendas(lista = ()):
    media = (calculo_total(lista)) / len(lista)
    return media

print("==================== Análisador de vendas ====================")
lista_venda = []
while True:
    print("\n1 - Adicionar vendas do dia")
    print("2 - Venda total")
    print("3 - Venda máxima")
    print("4 - Venda mínima")
    print("5 - Média das vendas")
    print("0 - Finalizar")
    try:
        opcao = int(input("Digite aqui: "))
    except:
        print("Escolha uma opcão valida")
        continue
    match opcao:
        case 1:
            try:
                venda = float(input("Informe o valor da venda: "))
                lista_venda.append(venda)
            except ValueError:
                print("Informe números")
        case 2:
            try:
                print(f"O Total do valor das vendas foram: {calculo_total(lista_venda):.2f}.")
            except IndexError:
                print("Necessario adicionar uma venda")
        case 3:
                try:
                    print(f"A venda máxima foi {venda_maxima(lista_venda)}.")
                except IndexError:
                    print("Necessario adicionar uma venda")
        case 4:
            try:
                print(f"A venda mínima foi: {venda_minima(lista_venda)}.")
            except IndexError:
                print("Necessario adicionar uma venda")
        case 5:
            try:
                print(f"A média do valor das vendas foi {media_vendas(lista_venda):.2f}.")
            except IndexError:
                print("Necessario adicionar vendas")
        case 0:
            print(f"Encerrado com sucesso.")
            break