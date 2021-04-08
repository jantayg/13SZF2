szam1 = int(input("első szám: "))
szam2 = int(input("második szám: "))
szam3 = int(input("harmadik szám: "))

if szam1 == szam2 + szam3 or szam2 == szam1 + szam3 or szam3 == szam1 + szam2:
    print("igen")
else:print("nem")