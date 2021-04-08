import random
gondoltszam = random.randrange(1, 90)
print(gondoltszam)
while True:
    szam = int(input("írj be egy számot 1 és 90 között"))
    if szam < gondoltszam:
        print ("A gondolt szám nagyobb")
    elif szam > gondoltszam:
        print ("A gondolt szám kisebb")
    else:
        print ("Jó számra gondoltál")
        break
