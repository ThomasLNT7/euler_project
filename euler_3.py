import math
#Ressortir le plus grand nombre premier par lequel un nombre est divisible

def verifPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n % i) == 0:
            return False
    return True


def primeNumberTo(limit):
    listNumber = list(range(1, round(math.sqrt(limit))))
    listPrime = []

    for element in listNumber:
        if verifPrime(element):
            listPrime.append(element)

    return listPrime


firstNumber = 600851475143

listPrime = primeNumberTo(firstNumber)
answer = []

for element in listPrime:
    if firstNumber%element == 0:
        answer.append(element)

print(max(answer))

