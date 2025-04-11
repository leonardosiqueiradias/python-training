def multiplicador(fator):
    def interna(x):
        return x * fator
    return interna

dobro = multiplicador(2)
triplo = multiplicador(3)

print("5 x 2 =", dobro(5))
print("5 x 3 =", triplo(5))
