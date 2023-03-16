#Készíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi, hogy az ikrek (Henrik és Hanna) jönnek-e ma kosrazni! Például így: Jön Henrik ma kosarazni? (igen/nem). A program írja ki, hogy melyik állítás igaz az alábbiak közül:
#- egyikük sem jön kosarazni,
#- mind a ketten jönnek kosarazni,
#- csak az egyikük jön kosarazni.

he = input("Henrik jön ma kosarazni?")
ha = input("Hanna jön ma kosarazni?")
if he == "igen" and ha == "igen":
    print("Mindenki megy kosarazni")
elif he != "igen" and ha != "igen":
    print("Nem mennek kosarazni")
elif he == "igen" or ha == "igen":
    print("Egyikük megy kosarazni")
