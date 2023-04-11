mondat=input("Adj meg egy mondatot: ") #bekéri a mondatot
mgh=0 #számláló
for betu in mondat: #loop
    if betu in "aeiouAEIOUáéíóöőúüűÁÉÍÓÖŐÚÜŰ": #keresés a szövegben a megadott betűket
        mgh+=1 #hozzáadás a számlálóhoz
print(mondat)
print(mgh)