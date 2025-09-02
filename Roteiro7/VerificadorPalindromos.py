def verificacao_palindromos(palavra : str):
    # Verificação da entrada
    if not isinstance(palavra, str):
    # Dispara um erro personalizado
        raise TypeError("O parâmetro 'string' deve ser uma string")
    else:
    # Formantando a palavra para ficar de trás para frente utiliznado slicing e removendo os espaços
    # com replace e transformando a string toda em minúscula
        palavra_formatada = palavra[::-1].replace(" ", "").lower()
    # verificação se a string formata e a string padrão apenas sem os espaços são iguais
        if palavra_formatada == palavra.replace(" ", "").lower():
            return True
        else:
            return False

# Solicitação de dados e execução do programa
print("====================== Verificador de palíndromos ======================\n")

while True:
    print("Caso deseje parar digite 0")
    palavra_informada = input("Digite uma palavra: ")
    if palavra_informada == "0":
        break
    else:
        retorno_verificacao_palidromo = verificacao_palindromos(palavra_informada)
        if not retorno_verificacao_palidromo:
            print(f"A palavra {palavra_informada} não é um palídromo\n")
        else:
            print(f"A palavra {palavra_informada} é um palíndromo\n")

print("\n========================================================================")
