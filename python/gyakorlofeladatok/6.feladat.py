szam1 = int(input("első szám: "))
szam2 = int(input("második szám: "))
szam3 = int(input("harmadik szám: "))

if szam1 % 2 != 0 or szam2 % 2 != 0 or szam3 % 2 != 0 and szam1 == 1:
    print("nem")
else:print("igen")