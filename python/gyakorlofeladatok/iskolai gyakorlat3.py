szoveg = open("varosok.txt", "r")
p=[]
maxtav=0
for sor in szoveg:
    s=sor.split()
    tavolsag=int(s[1])
    if tavolsag > maxtav:
        maxtav = tavolsag
        varos=s[0]
print(varos,maxtav)

