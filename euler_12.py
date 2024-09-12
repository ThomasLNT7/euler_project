# Comportement :
# Return d'un dictionnaire avec toutes les valeurs pour après trouver le nombre de diviseur

def isDivisible(a, b):
    if a % b == 0:
        return True
    return False


def triNumber(input):
    resultset = []
    i = 1
    result = 0
    while True:
        result += i
        resultset.append(i)

        if result > input:
            return False
            break

        if result == input:
            return resultset

        i += 1


print(triNumber(1))

dicoSet = {}
for i in range(1, 30):
    result = triNumber(i)
    if result != False:
        dicoSet[i] = result

resultset = {}

for cle, values in dicoSet.items():
    resultTemp = []
    for value in values:
        if isDivisible(cle, value):
            resultTemp.append(value)

    resultset[cle] = resultTemp

print(resultset)