dic = {"b":"l", "k":"a", "v":"c","i":"t","m":"f","q":"d","c":"p","x":"h","j":"u","f":"n","e":"i","w":"s","E":"I","u":"b","a":"y","z":"e","d":"k","I":"T","s":"g"}

with open ("LACTF\Crypto\indo.txt","r") as file:
    lis = file.read()
    for i in lis:
        if i in dic:
            print(dic[i],end="")
        else:
            print(i,end="")