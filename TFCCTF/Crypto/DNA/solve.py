Dic = {'C' : '01', 'A': '00', 'G' :'10','T' : '11'}

with open("TFCCTF\Crypto\DNA\dna.txt","r") as fil:
    text = fil.read()
    li = text.split(" ")
    for i in li:
        temp = ""
        for b in i:
            temp += Dic[b]
        print(temp ,end=" ") 