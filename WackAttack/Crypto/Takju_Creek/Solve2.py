from pwn import *
from mt19937predictor import MT19937Predictor
from Crypto.Util.number import bytes_to_long, long_to_bytes

# r = remote('ctf.wackattack.eu', 5027)
data = 'A'*2496
predictor = MT19937Predictor()
output = b'7\xe2e\xbdF\xc7\xfb\x16\xb2\xc2\x98\x84q\x0f[\xb5\xd0l\xfc\xbdv\xcc\x01\x11S*!.\x82\xd6\xa1\xd7\xf7K\xdb\x08?T\x92uT\xc2\xc1\xa4\x84\xfc}\x7fP#\'\x07\x11F\x95\xc6\xd95D\x92o\'1TPr\x03\xcf\x19\xf5\xa9\x03X\x86%\xa7\x16Q\x93$LKE\x16*\xe1w\x11\x9b(\x0f\x8c\x8cD-Ruo\x1f\xe9UN\x92\x06\xb0\x16\x9e\x00!\x15\x8e\xb03\x8d\x01p9\x9a\x85\x8d\x1ch5\xb7\x8b\x11\xad\xf4y\x9c\x0f\xe2\xcd\xf9IH\xf9\x95\x96*a\r\xf1\xcf\x1d\x87\xf4\xed\xe8\xa9l^x\x01\x859 \x9f\xb3\xdc\x0ei\x91\xc3\xec\xe6%\x13\x12F4b;\x19%\xb1;|\x19y\x80e\xbe\x91\xfe\xc4\xc7\xef\x16\x1b\xf9\x06:\xc7o\x0c\x97\xc8\xfe\x9c\x93\x86\x7f_?u\xb3\x89\xd5\xd9\x9e@\x99\xa2\xd6\x11k]\xd3\x1dC\xcd5N\xfe\xdd\x8cs\xea\x1b\xe3\xbc\xa9jM\xa6\xfb\xf8\x99\xc4\x87fa\x8f\xe3:1,\xb8\xdeZo|\'\xfb\xcf\xe5\x80\xc0cDl\xeb\x07\x9aB-\xb2\xab\xd3\xad,\xf2\x8e\x1b\xd0\x1a\xf3\'\xf2\xe0\xd2\xb8\x0f\xb8\xb7\x18\xe2\xda7\xe9`Yrw\xa1\xae\xf5\x13;\xcd6Wf\xe0\xca>\xb4;\xbe\xef)\x13\xf2\xeeS\xb3k\xb1\xa0\xc6IE\x1f\xe7B\xa6\xf6\xbc\x90\xea$/8\\\x18\xa7\x1c\xfd\xdc\x07C\x14\xdc\xa8\x05"\x9a\xa9\x8cT@\xa6\x13n\xa6\x18\x8a\xebR\xe7\xda\xaaNZ6\x0b\x10\x10I\xb7\xfe\xe90j\x97\xaa),\xd8\x00*F\xd4\xe5\xd7\xbd(\n\x14\xd9\x89\x19!S\x88\xee\xee#\x9a\xcc\x1aj\xf9\xa1\xfcf\x92%\xaaR\xd7\xc1\x06I\xea\xbf%\xed\x84\xa6\xfc!\x04\xa8\xb2\x13\xc0J\xde\x95}o\'\xc8T\xc3t|\xbbq\x97\xe8\xa10\xeb\xf5Kv\xc9\\\xbcm:FR2\xea\x0e\x9f\xed\x81t\x0e\x87\xcdh3z\xd1\xc0\xc4\x9b\x1b\xa9M\xdb+Lt\x83\xfeM\xde\xf7\xc6TS~Ws~p\xec\x11\xe6\xee\x03\xcdn\xf7S)\xac\x02\xc7z\xa3\xd8\x9a"\x80\xf2}\xc0\x01;Yg\xcd\xc8\xf6\xa4\xff\xcaJ\x04\xb4oH\xc5\xb9\xc7c\x00(\xfbb{"\xfeh \x9a\xdf\x94-\x19N\x92\xfdp\r\xa9\x81\x7f\xe6\x01\x07O\xf2\xf3\'\x8f\xd4U\tF(5\xb7\xf8\xaf\xbc\xc5\x8b\x1fW\x16\xc1me2X\xdf#&\x8a{\x9b6m\xf0?\xd7\r\x84\x97l\xe5\xda!m\xaf\xd2\xfb\xe5\x9d\xa6qeF\x0e\xb0\x1aa\x07\xba\xe0\xee\xc5C^N~\x85\x97\x92 /\x9dCZ\x05m\xb1\xb5\x0fXrD\x82\xa3\xffUQ}\xc8A\xe4\xa0\xc3_\xfd\xa47\xa0+\xeedF\x99\xa8\xcb)\xcb\xc2\x14\xc6*rt\xb9\xdb\xea5\x02^\nq\xd4\x8d\xe4\xe0)\xb8\x18\x0bX\x8f\xa9W\xdc\x9c`\\t\x00\xcf\xa6r\xf4\x18\x08\xd7\xc4\x9aonN\\>\xa9>X\x06\xc2\xe5\x8bY\xa4\xa4:b\xdbI)SI\xf3\x14\xb4\xe3\x1dX\xd8\xa6\xbe\x9bB\x8d6\x1dj\xcb\xbf"\xe0\xadD\x8dYkx\xc0\x90[T\x8a\xb7\xce\x0f\xb8\xcb\x04\xebb\xea\x81\xb2\xe5\xad\xa4^\x83\xd2`\x11\t\xb7\xc8\x14\xe9\xdf /$\x1a\x8a\x9bN\xd5Ol\x98z\x08\x8f\xe1\x8b\xd5\xfc\xc30I\xb3l\xc3\x1d8r\xc8&\xc6\xa3F\xae\xd4 \xb3M\xa6\xa7v\xd8n\x1c\xfa\xe0\x00&V5!5b\x8fQ\x15I\xcd\xcb\xeey\x9b\x9d\x8d\xa5\xfb7\x9f\x93#\xa3-K\xfd\x0b\x12\x8b\x0e$M\x85\x9e\xb8\xeby\xa9\xdb\xa9\xafi[\xb5\xf0\xb2\xf9E\x03\xa6{\x8c6\xd1\xfc\xac\xb7p\x84\x9d\x841\xf1\xb9\xe3\xa1!\xe5\xe3\xabsy\xf0ucVU\x01W\x8a\xa4B\x9aX\x13\xb0\x82\xcc?\x1b1{\xa7\x12>\xccZ\x0f"\xe7\xael\x07Y\xd6I\xf5\x99\xc6\xf8\xa4<V\xf0\xb2a\x17\x80\x8c8\t\xb9S^\xa4\xfe\x9b\x16\xcc\xec\xb7\xc8~\x04\xd3H\xec\xa9za\x07\xe7UU.\xafAX1\x19:\xd3\x1a3r\xeb\xea\x9e\xf7\xab\x1ey\xf0\x10\xa6\xa5\xa1\x7f?2\xdb\xbc\x924-\xef[\xde\x99\x07\xbd/\xb9m\xe4.\x93\x90z\x99\xed>\xea\xc0?0\x02\x9aO;\xfe\xef!\x11\x0c&\xcd\xab\xec\x19[d\xee>Nb&\xaf\x17/\xf9\xca\xf0u\x1dV\xa9\x01cq\x0e\x05=\x0fc\x94$b\x93\xf5\xf1\x04\xd0\xf00~\x12\xb8\x9dD\xbe\x9a\x1d\xe1\xe0R\x89\xe7\x8e\xcf\xe4\x83\xb2G\xd0\xe7s\xbe2\xcb\x15\x94\x96v\xbf\xceX\xdf\x05\xd0\xd1\x95\xba\xd0\x1c\x99,;,`\xec\xec\x97C\xf1eM\x1d\xc1d\xc3\xafl\xc0\xd7S\x0eR[\x05V\xefs\xc6\xa0\xe2h\xb4\xe1\x0c\x08$\x90s\xa8\x89,\x7f7\x0b~\xe0\xa4\x0f\xd3}\x96)M\\\xcc\x8cA\xcc+Y\xff\xff[u\xd97\xdd\nAa\xd9eks\x16\x05|m\xc2\x93R\x8a\xd6\xc4\x16\xd1j\xa1\x0f\x87\xa0i\xe4\xd1)\x08\x8f\x99[\x8d\xef\x94\t$\xd6\x9e\x1f\xa4\xe8\xa5\xd3K\x1e\xee\xdd\x03\xdeO\xb6\xaaB1\x94TO\xa1W\x99\xc6\x89B\xc4}Pp\xac\xf2\xc6\xf9j\x80\xf7\xf7\xb2\xeb\x182\x00\xf7\xd3h\'^\xacU\x13O\xb7\xe5\xca+\xd6\xfbG\xe5\x90\xbec\xe7j!\xc2\xeb\x88\xc6vI\xf0\xe6\xb28\xcc6i\xddtBi\xbf`r\x13\xcc\xb2\x19\xb7d\'\t]\xb5\x01\x9f\x08\x84\xa1\xaf\xe7\x1b`\xeeN\x1fV8\xe94\x94\xae\xbe\xfbB\xe0\xa1m\xc8\xe4\'*\x80\xd5W\xab4\x1f\xcc\x11Q<\x9f\x9am)\xa5\xb7\xb7\xec\x86\xbd\xc4n<\xec\n\xe3\xd5\x01\x04\x86\x91\xcd\xb5\xfc\xd7`\x1a\xd8\xd6\x8d1\x00\xe5\x02%\xd3M\x93[\xe8\xefu\x15\xe3\xd1G\x0c\xd1~\xcf\x85\xe3&Mj{\xd1\x04\xf3sD\xce\rQ\xc8@\x0f\xa1)\xceoG\xde2\x0cnNk\x94\xde\xe2\xe1\x9bw\xa3T\xd3\x7fD\xb7\xb3\x8fSJ\\\xa2\x8a0\x05\x99\xdc\x99/G\x10\x11\x8eX\x93/\x0f\xb9\x8b\\\xa3\xfaK\xb2(\x19\xef\xc5a\xc7\xef\x07)\x114\x88\xf6\xa2kO\xf1+\x9d\x05\xe5\x98q\x1b\xe9I\x18"\x0bo\x92[\xe7V\xb9\xf2F`\xee\x93\xae\x0c\xae\x95\x7f\x04Y\xb3\x9e\xf7)\xb8\xa3\x15\xc2\xdc\x87\xbfq\x1f\x97\x8f\xe5\x04&\t&e&Y\xdb\xc2\xf272J\x91\r$\xfcd\x9cdB%~|\x1e\xdb\xc6\xf8,\xc5\x15\xb4\x0cX\x8eW\xdf\x8bt\xa8;E\x7f\xc7\x04:8Q<\xa5\xe2q\x9bt\xae\xfd\xd2u\xc5k\xdf\xe2\xc6\xc1\xa4\x92\xba\xe2\xfd\xa2\xc5\xf9\x03\x10T\x08j-B\x02K}\xfepK\x14a\xc0\x8c\xe5\x0e\x1dt&\xe4\xeb\xdf\xf3"\xfc]\xc7\xf7\xf1\x9c\x9e\xbb\x04}\x05WL\xc1X\xfe\xa3e@AAyD\xf7\xc9"\xec\xec\x16h\xfe\xe5\xa5\xd3\x14\x83\xc9M\xddL\xfa\xac~\xe3\xcaHL\x92\x9do\xf6\xdd\x12\x18\xcc\xa6\x01\x01\xe4AJ{P\xef4\xbd\x8f3\xaf\xcbA\x8dI\xb4\xaf\xab\xb6\xff\xe2\xb7l0\xc9\xfb\xf3>$\xd6\xdf \xe5\x03\x02J\xbeNw\x1b|/l\xb0\xc6,\x00\xa1O\xaa\x8ef\xbd0\xba\xc8\r\xa6\xf4\xdb\xe3^g\x1b\x1cl\xb3*\xf7\xd5ym\xc3\xedpX\x91\x0e\x12\xda\xd5\xef\x97\xe5\xc42{\x81\xf0\xa7YCeZ\xf7k\xa40\x83\xb0X9\xac\xe7sK\xf2RUrCF\x12|*t8=\x85^\xa9jn\xf9\xdf\x10#A\xd9\xa1\x9d#\x8d}zI5\xbc\xa6\xed\x0f\x02\x0eJ\xf3\xf1\r`\xda\xfb\xc6\x18\xbc20\x80\x97\x9f\xa8\x90\x92,\xcc5\x86\x0bVp\xda\xcc\xeb\xe7\xc0\xab=7\xf8\x19\x1c\xf7-\x80]\xe3\x88\x16g.\xce%C\x8d\xc5\xc3\x03\xad\x1b\xaa"\xb6#\x86\\\xfak\xcf1V\x94s\x07\tL\xff\xc3\x9b\x86`~\x82\xd4)\xafha\xcd\xb9\xfe\xbf\x9f\xcbp\x03\xd6\xbd\xd0\x17z\x92~\xec\xce%\xec\x86\xc3!\x0e\x03"L/\x89\x91M\x8c\xfcdH\xaa\x10ot>\xe8\xe5a\xbb_\xd2\x18\x0bw\xdd\xd4\xdd\xd7\x16\r\x1d\x89\xd8\x14\xb0E\xf8\xa3\xabB\xa7\xb1[\x02\x8e\x80\xc5\x16w\xdfw\xc0\xe0\xbbf\x06\xea\xc6\xa4\xc7[=Up?\x10W\x05\xdb\xf78\x94\x02K*\xf0O\x1e\x16r\x1b+\xb9\xc6\xb9\xf8\x03v(1\xa6K\x08Q\xbc;\x18\xf0\x82\xe7\x94\xb7\xe3\x9a|\xb1\xb6\'~\xbf\xcbF\xbf\xa9\x9beI\x19\x9e\x1a5\xcc\x83\x1a\x91\x7f\x1c\xad,\xe8\x9c+\x8d\xef\x82\xb4a\xba\xda\xb1\x8aJ\xe8h\r.\xc5F\xbb\x8c\x8a\xa3fh\xef\xb3\'U\xe7\xfdn\xca\x96\x15\xe6A\xf3\xc70{\xb4\xbb\x81\x13=`>\x15\x19T\xdcd\xaaW\xcf\xf3\xdes\x87\x90\xb3\xee\x8d\xbc\xb3\xc0\xea@^d&\x9f\x80\x13\x83\xe4\x94}\x15\xa0G\x921E\x90\xf1~\xdb#\xf1v\x18X\xd7\xad}P\xb5}\x05kz\x1cP\xff\xc3&\xec\xa7\x1c\xf3j\x06\x0f\xc5\x19Y1\xad\x10\xdc\t\xeb\'\x1b\x11\xf5\x8eD\xe9C\xe1\xda\xc3{\xec\x08\xce\xd6\x06Q\x14}\xcfQ\xe4\xf1\x1b_\x05\xe1\x96\xa2R\x1dSq\xfd\xa0tU\x0b-\xbd@U\xd6\xac\x8bt\x13\x16J\x8d\x8d\xd4X\xa2\xaf\xdd\xc7\xbce\x82\xb8\xb0\n\'\x02\xcf\xae\xea\xb1\xad\xd3( \x92\xd1A\x19\x03t\xb2\x95G\xa7vw\xa9\xf3\x10Q\xb2g\x8a<\x88\x11\x7f\xe8\xe7\xb0\x15\xc8K\xca\xd2\xf0%\x17\x83\xb5"\xe0\x02F\xe1V\xb1\xd4\xcd\xc8\x9b\xdf\x1f\xee\xab2\x9c:\xb0\xf6\xd2\xb8\xc8HvI\xbb\xfd\'\xd7\xbfB\'x\x94\x11\xa5P\x19\x87@p\xea\xf6x\xc1\xf6A. \xa0\'\xe1+\xb6\x9f\xa3-^\xd2\t\xc3/\x0b]\xc4\xf8l\x03d\xc5\xb3\x1c2\x004\xd9w\xfd\x895\xccQ\xdc\xa8D\x92\xd0\x98\r\xe9(\x17\xdb\xee\x19\xe0jzi\xef\x05\xdc\xa8\x00\xecV\xbe\xf90\xba\x86\xde\xd5\xe7P\xbe\xb2\xb2\x1d\x83\x1b\x94+\x07\x03\xd6\'\xca0f\xba\x16\xa7<\x85\xfc\x9f\x1a\x0fAqz\x15\t\xfa\nta\xea\xf2\x86@i\xfb)\x98\xcd\xabi\x10\xe5\xbc\x8e\x9e\xf7Njto\xe0\xec\xf5d\x87G!\x9b\xebx\x110\xef\x125\x1c5u\xa0\x13'
for i in range(0,2496,4):
    x = output[i:i+4]
    predictor.setrandbits(bytes_to_long(x)^1094795585, 32)
flag = b"\xfd\xff\n\x8c6W'=N\x90Zo\xf2\xe5\xd2\n\x15\xab\xa3oSe5|\xec\xf87\xe4\xed\xcf\x1c\\"

for i in range(0,len(flag),4):
    decflag = xor(long_to_bytes(predictor.getrandbits(32)),flag[i:i+4])
    print(decflag,end="")
