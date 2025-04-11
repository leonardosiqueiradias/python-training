class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f"{self.marca} {self.modelo}, Ano: {self.ano}")

c1 = Carro("Toyota", "Corolla", 2020)
c2 = Carro("Honda", "Civic", 2022)

c1.exibir_detalhes()
c2.exibir_detalhes()