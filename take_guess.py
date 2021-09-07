import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_tentativas = 3
pontos = 1000

print("Qual nível de dificuldade? ")
print("(1) Fácil (2) Médio (3) Díficil ")
nivel = int(input("Defina o nível: "))

if(nivel == 1):
    total_tentativas = 20
elif(nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5

# range(start, stop, [step])
for rodada in range(1, total_tentativas+1):
# while(rodada <= total_tentativas):
    # String interpolation
    print("Tentativa {} de {}".format(rodada, total_tentativas))

    chute_str = input("Digite um numero entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o numero secreto")
        elif(menor):
            print("Você errou! Seu chute foi menor que o numero secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

print("Fim do jogo")
