import math

answer = []
count = 2
stop = 10001

def verif_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n % i) == 0:
            return False
    return True

while len(answer) != stop:
    if verif_prime(count):
        answer.append(count)
    count += 1

print(answer[-1])


