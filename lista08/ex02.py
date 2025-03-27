# 2. Abertura Segura de Arquivo
# Escreva um programa que solicite ao usuário o nome de um arquivo para leitura. O
# programa deve tentar abrir o arquivo e exibir seu conteúdo. Utilize tratamento de
# exceções para lidar com a ausência do arquivo e outros possíveis erros.
def abertura_segura_arquivo():
    nome_arquivo = input("Digite o nome do arquivo para leitura: ")
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except IOError:
        print(f"Erro: Não foi possível ler o arquivo '{nome_arquivo}'.")

abertura_segura_arquivo()