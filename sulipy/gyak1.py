szamok=[]
file=open('beolvas1.txt')
for sor in file:
    szamok.append(int(sor.strip()))
print(sum(szamok)/len(szamok))