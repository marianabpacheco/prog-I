
player1 = input("Digite o nome do jogador 1: ")
age1 = int(input("PDigite a idade do jogador 1: "))

player2 = input("Digite o nome do jogador 2: ")
age2 = int(input("Digite a idade do jogador 2: "))

if(age1 > age2):
    print("O jogador mais velho é " + player1)
else:
    print("O jogador mais velho é " + player2)