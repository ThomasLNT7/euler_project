
### Trouver la plus petit nombre divisible par tous les nombres entre 1 et 20

init = 2520
running = True
divList = list(range(1,21))
count = 0

while running:
    count = 0
    for element in divList:
        if init%element!=0:
            break
        else:
            count  += 1
    if count > 19:
        print(f"FINIIIIIIIISSSSS -------- {init}")
        running = False
    init += 10
