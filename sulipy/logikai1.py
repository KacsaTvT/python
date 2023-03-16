#Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
#- pozitív páros vagy
#- negatív páratlan.
#Az eredményről tájékoztatja a felhasználót.

szam = int(input("Adj meg egy egész számot"))
if szam > 0 and szam % 2 == 0:
    print("A szám pozitív és páros")
elif szam < 0 and szam % 2 != 0:
    print("A szám negatív és páratlan")
else:
    print("A szám nem; pozitív és páros, vagy nem; negatív és páratlan")
