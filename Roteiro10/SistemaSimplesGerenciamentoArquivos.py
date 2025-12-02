# Função para criar o arquivo utilizando o modo W e fechando o arquivo
def criar(nome):
    criar_arquivo = open(nome, "w", encoding="utf-8")
    criar_arquivo.close()
    return "Arquivo criado com sucesso!!!"
# Função para ler o arquivo utilizando try e except para não finalizar o arquivo com o modo "r"
def ler(nome_arquivo):
    try:
        texto_lido = ""
        leitura = open(nome_arquivo, "r", encoding="utf-8")
        arquivos = leitura.readlines()
# Verificação se o arquivo está em Branco
        if not arquivos:
            return "Arquivo em branco"
        else:
            for linhas in arquivos:
                linhas.rstrip()
                texto_lido += linhas
            leitura.close()
            return f"Arquivo encontrado, Dados escritos: {texto_lido}"
# Caso o arquivo não tenha sido criado retorna essa exceção
    except FileNotFoundError:
        return "Necessário criar o arquivo"
# Função para adicionar uma escrita no arquivo com o modo "a" para escrever no arquivo
def inserir_conteudo(nome_arquivo, escrita):
    try:
        escrever = open(nome_arquivo, "a", encoding="utf-8")
        escrever.write(escrita)
        escrever.close()
        return f"Escrito {escrita} com sucesso!"
    except FileNotFoundError:
        return "Necessário criar o arquivo"
# Menu Interativo e execução do programa
while True:
    print("   Gerenciador de Arquivo   ")
    print("1. Criar arquivo")
    print("2. Ler arquivo")
    print("3. Adicionar conteúdo")
    print("4. Sair")
    selecionador = int(input("Selecione uma opção: "))
# Encerramento do programa
    if selecionador == 4:
        print("Programa finalizado!!!")
        break
# Criação do arquivo, solicitando o nome do arquivo e chamando a função e retornando o resultado
    elif selecionador == 1:
        nome_arquivo_criado = input("Informe o nome do arquivo a ser criado: ")
        print(f"{criar(nome_arquivo_criado)}\n")
# Leitura do arquivo solicitando o nome do arquivo e retornando o resultado da função
    elif selecionador == 2:
        arquivo_ler = input("Digite o nome do arquivo que deseja ler: ")
        print(f"{ler(arquivo_ler)}\n")
# Escrever no arquivo solicita o nome do arquivo e o que deseja escrever, retornando o resultado da função
    elif selecionador == 3:
        nome_arquivo_adicionar = input("Digite o nome do arquivo que deseja escrever: ")
        adicionar_escrita = input("Digite o que deseja adicionar: ")
        print(f"{inserir_conteudo(nome_arquivo_adicionar, adicionar_escrita)}\n")
