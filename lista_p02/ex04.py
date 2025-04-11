frase = input("Digite uma frase: ").lower()

vogais = 'aeiou'
for v in vogais:
    print(f"{v}: {frase.count(v)}")

print("Frase invertida:", frase[::-1])
print("Frase com -:", frase.replace(" ", "-"))