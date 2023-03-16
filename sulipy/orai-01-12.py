import random
szamok = []
pozitiv = []

for i in range(100):
    szam = random.randint(-1000, 1000)
    szamok.append(szam)
    if szam > 0:
        pozitiv.append(szam)

#print(szamok)
print(round(sum(pozitiv)/len(pozitiv), 4))