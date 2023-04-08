import random #a random szám miatt kötelező, nélküle nem működik a második sor
randomszam=random.randint(1,100) #generál random számot 1 és 100 között
while True: #while ciklus
    tipp=int(input("Tippelj a számra: ")) #felhasználó által bekért szám
    if tipp == randomszam: #ha megegyezik a két szám
        print("Eltaláltad")
        break #program megszakítása
    if tipp > randomszam: #ha a tippelt szám nagyobb
        print("Kisebb")
    else: #ha a (tipplet szám nagyobb) ellentéte, tehát a tippelt szám kisebb
        print("Nagyobb")
    