inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]
print(pares)

quadrados = [n*n for n in inteiros]
print(quadrados)

frutas = ["maçã", "banana", "laranja", "melancia"]
frutas = [fruta.upper() for fruta in frutas]
print(frutas)