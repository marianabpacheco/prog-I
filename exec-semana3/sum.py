i = 0
numbers = []
sum = 0
while(i != 10):
    n = int(input("Digite um número: "))
    numbers.append(n)
    i += 1


for n in numbers:
    sum += n


print(sum)