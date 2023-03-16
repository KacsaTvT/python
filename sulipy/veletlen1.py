#Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!

import random
rszam=random.randint(1,3)

szam = int(input("Adj meg egy számot 1 és 3 között"))
if rszam == szam:
    print("Az általad megadott szám és a gép által generált szám megegyezik")
elif rszam > szam:
    print("A gép által megadott szám nagyobb a tiédnél")
elif rszam < szam:
    print("A gép által megadott szám kisebb a tiédnél")
