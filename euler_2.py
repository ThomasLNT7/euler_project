
def somme_liste(a):
    somme = 0
    for x in range(len(a)):
        somme += a[x]
    return somme

def fibonacci():
    result = [1,2]
    list_even = []
    suite = 0
    while suite <= 4000000:
        suite = result[-1] + result[-2]
        result.append(suite)
    for element in result:
        if element % 2 == 0:
            list_even.append(element)
    return list_even

print(somme_liste(fibonacci()))