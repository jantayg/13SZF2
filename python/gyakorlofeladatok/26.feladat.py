szöveg = open("temp.txt", encoding= "utf-8")
szövegstring = szöveg.read()
szöveg.close()
szavaklista = []
szavaklista = szövegstring.split(" ")
for i in range(1,len(szavaklista),2):
    print(szavaklista[i])
