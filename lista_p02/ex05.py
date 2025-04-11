entrada = input("Digite palavras separadas por espaço: ")
palavras = entrada.split()

print("Ordenadas:", sorted(palavras))
print("Total de palavras:", len(palavras))
print("Maiúsculas:", [palavra.upper() for palavra in palavras])