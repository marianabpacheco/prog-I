total = int(input("Quantos produtos deseja adicionar?"))
i = 1
products = []

while(total >= i):
    product = input("Digite seu item: ")
    products.append(product)
    i += 1

for product in products:
    print(product)