szöveg = open("temp.txt", encoding= "utf-8")
szövegstring = szöveg.read()
szöveg.close()
if "Debrecen" in szövegstring:
    print("van")
else:
    print("nincs")

