liste_1 = list(range(100, 1000))
liste_2 = list(range(100, 1000))
running = True
answer = []
calcul = []

for i in range(len(liste_1)):
    for a in range(len(liste_1)):
        result = liste_1[i] * liste_2[a]
        test = list(str(result))
        if len(test) == 5:
            if test[0] == test[-1]:
                if test[1] == test[-2]:
                    answer.append(result)
        if len(test) == 6:
            if test[0] == test[-1]:
                if test[1] == test[-2]:
                    if test[2] == test[-3]:
                        answer.append(result)
                        calcul.append(f'{i}*{a}')

answer.sort()
print(answer[-1])
