#Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel alapján eldönti milyen fajtájú! (kijelentő, kérdő, felkiáltó / felszólító / óhatjtó)
folyt=True
vizsgal=None
while folyt:
    while vizsgal!="":
        vizsgal=input("Írj egy mondatot! ")
        for jel in vizsgal:
            if jel=="?":
                print("Ez egy kérdés")
            if jel==".":
                print("Ez egy kijelentés")
            if jel=="!":
                print("Ez egy felkiáltó / felszólító / óhatjtó")
    while vizsgal!="":
        folyt=False