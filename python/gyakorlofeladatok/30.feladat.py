import turtle
szinek =["grey","grey","grey","grey","red","green","purple","blue","yellow","orange"]
def rajzolo(szam):
    ablak = turtle.Screen()
    ablak.setup(800, 800)
    ablak.bgcolor('white')
    ablak.title("program_3")
    fred = turtle.Turtle()
    fred.color(szinek[szam])
    for i in range(szam):
        fred.fd(100)
        fred.right(360/szam)
    ablak.exitonclick()
while True:
    szam = int(input("írj be egy számot a poligonokhoz 3-9-ig"))
    if szam < 3 or szam > 9:
        True
    else:
        rajzolo(szam)
        break
