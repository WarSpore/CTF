with open('IsisCTF\\Rev\\the','rb') as file:
    string = file.read().strip()
string = string.decode('utf-8')
#string = 'iÛÛÜÖ×ÚáäÈÑ¥gebªØÔÍãâ£i¥§²ËÅÒÍÈä'
flag = ''
rune = 0
for i,x in enumerate(string):
    flag += chr(ord(x)-rune)
    print(i,chr(ord(x)-rune)) 
    rune = ord(chr(ord(x)-rune))
print()
print(flag,end="")