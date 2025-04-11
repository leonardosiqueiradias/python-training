def contar_pares(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Digite o valor limite: "))
for num in contar_pares(n):
    print(num)