def összead(szam1,szam2):
    tmp = 0
    for i in range(szam1 + 1, szam2):
        tmp = i + tmp
    print(tmp)

összead(5,8)