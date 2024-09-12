
def somme(a,b,c):
    return a+b+c

ranged = 1000

for a in range(100,ranged):
    for b in range(100,ranged):
        for c in range(100,ranged):
            if a<b and b<c and a<c:
                if somme(a,b,c) == 1000:
                    if a**2+b**2 == c**2:
                        print(a*b*c)
