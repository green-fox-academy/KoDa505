"""kiirja a primszamokat egytol szazig"""

szam = 0


while szam < 100:
    oszto = 2
    while oszto < szam:
        if szam % oszto == 0:
            break
        oszto += 1
    else:
        print(szam)
    szam += 1
