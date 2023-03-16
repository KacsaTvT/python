import random

ro = random.randint(1,2)
tipp = input("Tippelj (fej, iras): ")

if ro == 1:
    eredmeny="fej"
elif ro == 2:
    eredmeny="iras"

if tipp==eredmeny:
    print("Nyertél!", eredmeny)
else:
    print("Vesztettél!", "Eredmény: ", eredmeny, "Tipped: ", tipp)
