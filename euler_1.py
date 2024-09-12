range_total = 1000
result = []

def somme_liste(a):
    somme = 0
    for x in range(len(a)-1):
        somme += a[x]
    return somme


for i in range(range_total + 1):
    if i % 3 == 0 or i % 5 == 0:
        result.append(i)

print(somme_liste(result))


