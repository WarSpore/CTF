from Crypto.Util.number import getPrime, isPrime, long_to_bytes, bytes_to_long, getRandomInteger
from secretstuff import FLAG, SECRET_KEY, NEG_EXP, VOTE_COUNT
from base64 import b64encode
import socketserver
from sys import argv, exit
from signal import alarm
import json
from gmpy2 import mpz

RED = 69
BLUE = 420

p = 182112773609303608355593975466414536423004963921761680083153476656234529045191335526017418462168800246033685760661801320931547403079744733551595553126704744634355240077957014642401670961286054790497365930781009051813180340029831077600422718167526189989438138234107880643400096950208751207487056002028035129159

ELECTORAL_BOARD_PK = 143807593692545761134223625147510192593863516300333483789484119029811164964747814233265912849602076760105815225850113495587171209239654319140169463159577483617052908603857412861557536638001046046730650300913653755105381262575510335781839336303423236416686115604580354636988694984561195006032142817459456769403


g = 3

def gen_safe_prime():
    while True:
        q = getPrime(1024)
        p = 2*q+1

        if isPrime(p):
            return p

def f(a, b, c):
    return int(pow(mpz(a), mpz(b), mpz(c)))

def encrypt_vote(vote):
    random = getRandomInteger(128)
    return (f(g, random, p), vote * f(ELECTORAL_BOARD_PK, random, p))


def decrypt_vote(encrypted_vote):
    return (encrypted_vote[1] * f(encrypted_vote[0], NEG_EXP, p)) % p
    

def get_votes(max_votes, red_votes):
    votes = []
    
    for i in range(red_votes):
        votes.append(encrypt_vote(RED))

    for i in range(max_votes - red_votes):
        votes.append(encrypt_vote(BLUE))

    return votes


class ClientHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def setup(self):
        super().setup()
        self.total_votes = VOTE_COUNT
        self.red_count = getRandomInteger(23) % self.total_votes
    
    def handle(self):
        self.send_to(self.client_address, b"Da senaten votes comen soon. Pleasen waiten..\n\n")
        votes = get_votes(self.total_votes, self.red_count)
        self.send_to(self.client_address, b64encode(json.dumps(votes).encode('utf-8')))

        self.send_to(self.client_address, "\n\nAll {} senaters have voted, but dalee  a boopjak, wesa can only decrypt una vote! pleasen find how many votes isa red!\n>".format(self.total_votes).encode("utf-8"))
        
        req = self.request.recv(2048).split(b',')
        x = int(req[0])
        w = int(req[1])

        dec = decrypt_vote((x,w))
        self.send_to(self.client_address, "If wesa decrypt what yousa gave us wesa getsa:\n{}\n\n".format(dec).encode('utf-8'))
        
         
        self.send_to(self.client_address, b"Pleasen tell mesa, how many voted per red??\n>")
        guess = int(self.request.recv(100))

        if guess == self.red_count:
            self.send_to(self.client_address, "Dat  right! thanken yousa so mui, have a flag: {}\n\n".format(FLAG).encode('utf-8'))
        else:
            self.send_to(self.client_address, b"Dat not right, sorry :(!\n\n")

        exit(0)
        

    def send_to(self, recipient, payload):
        self.request.sendto(payload, recipient)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

    def __init__(self, server_addr, request_handler):
        super().__init__(server_addr, request_handler)


if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = int(argv[1])

    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()

