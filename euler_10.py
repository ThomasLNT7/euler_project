import math

result = 0

def verif_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n % i) == 0:
            return False
    return True

for i in range(2, 2000001):
    if verif_prime(i):
        result += i

print(result)
