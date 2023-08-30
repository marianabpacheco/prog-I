sum = 0


for i in range(4):
    number = int(input("Digite um número: "))
    sum += number


if(sum % 2 == 0):
    print("A soma é um número par")
else:
    print("A soma é um número ímpar")