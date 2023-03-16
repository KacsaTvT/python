#Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!
# + 1.2

valasz = input("Jó napod van? igen/nem")
if valasz == ("igen"):
    print("Szuper, nekem is jó napom van")
if valasz == ("nem"):
    print ("Szar lehet")
if valasz != "nem" or "igen":
    print("Nem értem mit mondasz..")
print("A program vége")
