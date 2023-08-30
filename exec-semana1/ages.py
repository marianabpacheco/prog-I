user = input("Digite o nome da pessoa: ")
age = int(input("Digite a idade da pessoa: "))

if(age < 0):
    print("Idade inválida!")
if(age >= 18):
    print("Você é adulto")
if(age > 13 and age < 18):
    print("Você é adolescente")
if(age <= 13 and age >= 0):
    print("Você é criança")