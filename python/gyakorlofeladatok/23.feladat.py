numberslist =[]
while True:
    szam = int(input("írj be egy számot"))
    if szam == 0:
        break
    numberslist.append(szam)
numberslist.reverse()
print(numberslist)
