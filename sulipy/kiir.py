#Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot, és ezeket tárolja el egy listában! A program adja össze a lista elemeit, írja ki a képernyőre az összegüket és a lista elemeit!
import random
asz=1
azs=[]
while asz<=5:
    szamok=random.randint(1,10)
    asz=asz+1
    azs.append(szamok)
print(azs)
osszeg=0
for szam in azs:
    osszeg+=szam
print(osszeg)
