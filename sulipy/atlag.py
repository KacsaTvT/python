darab = 0
osszeg = 0

erdemjegy = int(input("Add meg a jegyed: "))
while erdemjegy != 0:
    darab = darab + 1
    osszeg = osszeg + erdemjegy
    erdemjegy = int(input("Add meg a következő jegyed: "))

if darab != 0:
    print("A jegyed átlaga: ", osszeg/darab)
else:
    print("Nem adtál meg egy jegyet sem!")
