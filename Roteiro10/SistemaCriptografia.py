import os


def criptografar_cesar(texto, chave):
    """Criptografa um texto usando a Cifra de César."""
    resultado = ""
    for char in texto:
        # Lidar apenas com letras (maiúsculas e minúsculas)
        if 'a' <= char <= 'z':
            # Aplicar a cifra
            deslocamento = (ord(char) - ord('a') + chave) % 26
            resultado += chr(deslocamento + ord('a'))
        elif 'A' <= char <= 'Z':
            deslocamento = (ord(char) - ord('A') + chave) % 26
            resultado += chr(deslocamento + ord('A'))
        else:
            # Manter caracteres não-alfabéticos (espaços, pontuação, etc.) inalterados
            resultado += char
    return resultado


def descriptografar_cesar(texto, chave):
    """Descriptografa um texto (que é criptografado pela Cifra de César) 
    usando a chave de criptografia.
    """
    # Descriptografar é o mesmo que criptografar com uma chave negativa (26 - chave)
    return criptografar_cesar(texto, -chave)


def criar_arquivo():
    """Cria um novo arquivo de texto vazio."""
    nome_arquivo = input("Digite o nome do novo arquivo (ex: texto.txt): ")
    try:
        with open(nome_arquivo, 'w') as f:
            print(f"✅ Arquivo '{nome_arquivo}' criado com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao criar o arquivo: {e}")


def inserir_texto():
    """Insere/sobrescreve texto em um arquivo existente."""
    nome_arquivo = input("Digite o nome do arquivo para inserir texto: ")
    if not os.path.exists(nome_arquivo):
        print(f"⚠️ Arquivo '{nome_arquivo}' não encontrado.")
        return

    texto = input("Digite o texto a ser inserido no arquivo (O texto atual será **sobrescrito**):\n")
    try:
        with open(nome_arquivo, 'w') as f:
            f.write(texto)
            print(f"📝 Texto inserido com sucesso em '{nome_arquivo}'.")
    except Exception as e:
        print(f"❌ Erro ao escrever no arquivo: {e}")


def ler_arquivo():
    """Lê e exibe o conteúdo de um arquivo de texto."""
    nome_arquivo = input("Digite o nome do arquivo para ler: ")
    if not os.path.exists(nome_arquivo):
        print(f"⚠️ Arquivo '{nome_arquivo}' não encontrado.")
        return

    try:
        with open(nome_arquivo, 'r') as f:
            conteudo = f.read()
            print(f"\n--- Conteúdo de '{nome_arquivo}' ---")
            print(conteudo)
            print("------------------------------------\n")
    except Exception as e:
        print(f"❌ Erro ao ler o arquivo: {e}")


def processar_arquivo_cesar(tipo):
    """Função genérica para criptografar ou descriptografar um arquivo."""
    if tipo == 'criptografar':
        acao_verbo = "Criptografar"
        acao_substantivo = "criptografado"
    else:
        acao_verbo = "Descriptografar"
        acao_substantivo = "descriptografado"

    nome_origem = input(f"Digite o nome do arquivo para {acao_verbo.lower()}: ")
    if not os.path.exists(nome_origem):
        print(f"⚠️ Arquivo '{nome_origem}' não encontrado.")
        return

    while True:
        try:
            chave = int(input("Digite a chave de acesso (um número inteiro, ex: 3): "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a chave.")

    nome_destino = input(f"Digite o nome do novo arquivo {acao_substantivo} (ex: saida_{acao_substantivo}.txt): ")

    try:
        with open(nome_origem, 'r') as f_origem:
            texto_original = f_origem.read()

        if tipo == 'criptografar':
            texto_processado = criptografar_cesar(texto_original, chave)
        else:
            texto_processado = descriptografar_cesar(texto_original, chave)

        with open(nome_destino, 'w') as f_destino:
            f_destino.write(texto_processado)

        print(f"🎉 Arquivo '{nome_origem}' {acao_substantivo} com sucesso para '{nome_destino}'.")
        print(f"🔑 Chave utilizada: {chave}")

    except Exception as e:
        print(f"❌ Erro ao {acao_verbo.lower()} o arquivo: {e}")


def menu():
    """Exibe o menu principal e processa as escolhas do usuário."""
    while True:
        print("\n=== Gerenciador de Criptografia de César ===")
        print("1. Criar um arquivo texto")
        print("2. Inserir/sobrescrever um texto")
        print("3. Ler um arquivo texto")
        print("4. Criptografar um arquivo texto (Cifra de César)")
        print("5. Descriptografar um arquivo texto (Cifra de César)")
        print("0. Sair")
        print("------------------------------------------")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            criar_arquivo()
        elif escolha == '2':
            inserir_texto()
        elif escolha == '3':
            ler_arquivo()
        elif escolha == '4':
            processar_arquivo_cesar('criptografar')
        elif escolha == '5':
            processar_arquivo_cesar('descriptografar')
        elif escolha == '0':
            print("👋 Programa encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    menu()