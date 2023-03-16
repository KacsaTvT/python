import random
roldal = random.randint(0,1)
tipp = input("Tippelj ")
if roldal == 0 and tipp == "fej":
    print("eltaláltad(fej)")
else:
    print("nem találtad el (g.fej)")
if roldal == 1 and tipp == "iras":
    print("eltaláltad(iras)")
else:
    print("nem találtad el(g.iras)")
          
