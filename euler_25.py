
liste_fibo = [1,1]

def somme(a,b):
    return a+b

running = True
i = 1

while running:
    result = liste_fibo[i]+liste_fibo[i-1]
    liste_fibo.append(result)
    liste_test = list(str(result))
    if len(liste_test) == 1001:
        print(i)
        running = False
    i += 1

print(liste_fibo[-1])






