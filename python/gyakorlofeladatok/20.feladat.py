def harmadikplussz(number):
    for i in range(1,number+1):
        if i % 3 == 0:
            print("+", end="")
        else:
            print("-", end="")

harmadikplussz(20)