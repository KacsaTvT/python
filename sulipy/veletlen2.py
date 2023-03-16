#A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
#nem működik

import random
roldal = random.randint(0,1)

tipp = input("Fej vagy írás? ")
if roldal == 0 and tipp == "fej":
    print("eltaláltad fej")
if roldal == 1 and tipp == "iras":
    print("eltaláltad iras")

