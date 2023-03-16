#Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.

import random

gg = random.randint(1, 5)

szam = int(input("Adj meg egy számot"))
if gg == szam:
    print("A gondolt szám megegyezik a tiéddel")
elif gg > szam:
    print("A gondolt szám nagyobb a tiédnél")
elif gg < szam:
    print("A gondolt szám kisebb a tiédnél")
print("Program vége")
