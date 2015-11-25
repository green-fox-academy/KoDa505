"""megmondja egy szamrol,hogy prim-e    """

szam = 133

is_prime = False

oszto = 2

while oszto < int(szam ** 0.5):
    if szam % oszto == 0:
        is_prime = True
        break
    oszto +=1

print(szam, "is a prime")
