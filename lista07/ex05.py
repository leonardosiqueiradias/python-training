# 5. Catálogo de Produtos
# Crie um dicionário onde as chaves representem códigos de produtos e os valores
# sejam tuplas contendo o nome do produto e seu preço. Permita que o usuário
# informe um código para buscar o nome e o preço do produto correspondente.

def product_catalog():
    products = {
        101: ("Laptop", 3500.00),
        102: ("Mouse", 50.00),
        103: ("Keyboard", 120.00),
        104: ("Monitor", 800.00),
        105: ("Printer", 600.00)
    }

    code = int(input("Enter the product code: "))

    if code in products:
        name, price = products[code]
        print(f"Product: {name}\nPrice: $ {price:.2f}")
    else:
        print("Product not found.")


product_catalog()