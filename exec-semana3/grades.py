a_grade = float(input("Digite nota do Grau A: "))
b_grade = float(input("Digite nota do Grau B: "))

if(b_grade < 0 or b_grade < 0):
    print("Por favor informe uma nota válida")
else:
    total = (a_grade * 0.3) + (b_grade * 0.7)

    if(total < 7):
        print("Você deve realizar o Grau C")
    else:
        print("Você passou!")