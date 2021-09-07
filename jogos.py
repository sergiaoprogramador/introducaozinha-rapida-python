import forca
import take_guess

def escolha():
    print("*********************************")
    print("********Escolha o seu jogo*******")
    print("*********************************")

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual é o jogo? "))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Advinhação")
        take_guess.jogar()

if(__name__ == "__main__"):
    escolha()
