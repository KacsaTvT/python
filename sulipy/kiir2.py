#Írj egy programot, amely a felhasználótól kér be egész számokat [-5;5] intervallumban. A bekérés akkor fejeződjön be, amikor a felhasználó intervallumon kívüli értéket ad meg! A program írja ki a megadott intervallumba eső számokat és az összegüket.
"""
szamok = 0
while -5 <= szamok <= 5:
    szamok = int(input("Írj be egy számot 5 és -5 között: "))
    if -5 <= szamok <= 5:
        print(szamok)
"""
szamok_ossz = 0
szamok = 0
while -5 <= szamok <= 5:
    szamok = int(input("Írj be számot 5 és -5 között: "))
    if -5 <= szamok <= 5:
        print(szamok)
        szamok_ossz += szamok
print("Összeg:", szamok_ossz)

