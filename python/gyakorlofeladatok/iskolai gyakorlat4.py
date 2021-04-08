szoveg = open("varosok.txt", "r")
p=[]
sor1=szoveg.readline()
bontottsor=sor1.split()
print(bontottsor)
maxtav=int(bontottsor[1])
varos=bontottsor[0]
for sor in szoveg:
    s=sor.split()
    tavolsag=int(s[1])
    if tavolsag > maxtav:
        maxtav = tavolsag
        varos=s[0]
print(varos,maxtav)
eredmeny = varos + " " + str(maxtav)
szoveg.close()
f = open("eredmeny.txt","w")
f.write(eredmeny)