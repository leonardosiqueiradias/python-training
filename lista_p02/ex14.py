import pickle

numeros = [10, 20, 30, 40]

# Gravando
with open("dados.bin", "wb") as f:
    pickle.dump(numeros, f)

# Lendo
with open("dados.bin", "rb") as f:
    dados = pickle.load(f)
    print("Dados lidos:", dados)