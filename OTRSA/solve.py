with open("OTRSA\handout.txt") as fil:
    for i in fil.readlines():
        for n in range(30, 150):
            param = i.split(" ")
            if pow(n,65537,int(param[2].strip())) == int(param[0].strip()):
                print(chr(n),end="")
