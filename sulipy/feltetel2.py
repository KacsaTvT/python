#Készíts egy programot, ami bekér egy számot a felhasználótól, majd kiírja, hogy a megadott szám páros-e vagy páratlan!

szam = int(input("Adj meg egy számot "))
if szam % 2 == 0:
    print("A szám páros")
else:
    print("A szám páratlan")
print("A program vége.")
