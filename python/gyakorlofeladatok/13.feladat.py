nullakarakter = True
number = int(input("Adj meg egy szamot: "))
for i in range(number):
    if nullakarakter:
        print("0", end="")
        nullakarakter = False
    else:
        print("1", end="")
        nullakarakter = True
