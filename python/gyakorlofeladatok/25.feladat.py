
szamok = open("szamok.txt","w")
for i in range(301):
    if i % 3 == 0:
        szamok.write(str(i) + " ")
