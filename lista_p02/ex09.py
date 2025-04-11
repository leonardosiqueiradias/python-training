class Animal:
    def fazer_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

animais = [Cachorro(), Gato()]
for a in animais:
    a.fazer_som()