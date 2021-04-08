from random import randint
szam=randint(1,100)
print("gondoltam egy számra 1 és 100 között")
tipp=0
while szam!=tipp:
    tipp=int(input("melyik számra gondoltam?"))
    if tipp>szam:
        print("nem, ennél kisbbre gondoltam")
    else:
        if tipp<szam:
            print("nem, ennél nagyobbra gondoltam")
        else:
            print("igen, eltaláltad")
