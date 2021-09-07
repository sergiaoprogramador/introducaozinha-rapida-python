
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = True

    while (not enforcou and not acertou):
        chute = input("Escolha uma letra?")
        chute = chute.strip()

        index = 0

        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição ".format(letra, index))
            index+=1
        print("jogando...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
