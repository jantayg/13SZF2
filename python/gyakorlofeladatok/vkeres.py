f = open("vonalkodok.txt")
keresett = input("ird be a vonalkodot, amit keresunk ")
for line in f:
    if line[:13] == keresett:
       print(keresett)
