def karakterkereso(mondat, karakter):
#   mondat = input("írj be egy mondatot!")
#  karakter = input("adj meg egy karaktert")
    darabszam = 0
    for i in range(len(mondat)):
        if karakter == mondat[i]:
            darabszam = darabszam + 1
    return darabszam


print(karakterkereso("mondat","a"))
