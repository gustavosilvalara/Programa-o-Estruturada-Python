def count_(frase : str, palavra : str):
    if not isinstance(frase, str) and not isinstance(palavra, str):
        raise TypeError("O tipo informado deve ser string")
    else:
        # 1. Converte tudo para minúsculas para uma busca que não diferencia maiúsculas de minúsculas
        frase_minuscula = frase.lower()
        palavra_minuscula = palavra.lower()

        # 2. Inicia o contador e a posição de busca
        contador = 0
        posicao = 0

        # 3. Laço de repetição para buscar ocorrências
        while True:
            posicao = frase_minuscula.find(palavra_minuscula, posicao)

            # Se a palavra não for encontrada
            if posicao == -1:
                break  # Sai do loop

            # Se a palavra for encontrada
            else:
                contador += 1
                # Avança a posição de busca para o próximo caractere, para evitar um loop infinito
                posicao += 1
        return contador

print("====================== Contador de palavra na frase ======================\n")

while True:
    print("Caso deseje parar digite 0")
    frase_informada = input("Digite uma frase: ")
    palavra_informada = input("Digite uma palavra: ")
    if palavra_informada == "0" or palavra_informada == "0":
        break
    else:
        retorno_contador_palavras = count_(frase_informada, palavra_informada)
        print(f"A quantidade de vezes que {palavra_informada} se repete é {retorno_contador_palavras}. ")

print("\n========================================================================")