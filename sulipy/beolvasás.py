adatok=[]
file=open('beolvas1.txt')
for sor in file:
    adatok.append(sor.strip())
#print(adatok)
#osszeg=0
#for adat in adatok:
   # osszeg+=float(adat)
#print('az összeg', round(osszeg,3))

szorzat=1
for adat in adatok:
    szorzat*=float(adat)
print(szorzat)
