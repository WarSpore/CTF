from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from random import choices, randint
from string import printable
import sys, os


BANNER = """
Velkommen til Orakeltjenesten!
Du får nå tre valg:
1: Krypter en melding
2: Krypter det hemmelige flagget
?: Avslutt
""".strip( )

KEY = b'' . join( [ os.urandom( 1, ) ] * 16, )

def random_streng( makslengde = 100, ) -> str:
    """Returnerer en tilfeldig streng med lengde {makslengde}"""
    return ''.join( choices( printable, k = makslengde, ) )

def krypter_melding( msg, key = None, ):
    """Krypterer en melding. Hvis {key} ikke er spesifisert, velges en tilfeldig key på en sikker måte"""
    if key == None:
        key = os.urandom( 16, )

    if msg == None:
        msg = input( "Gi meg meldingen som skal krypteres (ascii): ", )
    
    msg = msg.encode( ) 
    # Legger til litt ekstra data bak meldingen for å stoppe slemme hackere
    padding = random_streng( randint( 1, 100, ), ) 
    padding = padding.encode( ) 
    
    msg = b''.join( [ msg, 
                      padding,b"h"*16
                    ], 
                  )  

    msg  = pad( msg, AES.block_size, )
    ciph = AES.new( key, AES.MODE_ECB, )
    enc  = ciph.encrypt( msg, )
    print( f"Din krypterte melding: {enc.hex( )}", )

if __name__ == "__main__":
    FLAG = "a"*16
    while True:
        print( BANNER, )
        
        choice = input( "> ", )

        # Krypter en valgfri melding med en statisk key
        if choice == "1":
            krypter_melding( None, KEY, )
        
        # Hent ut flagget, kryptert med en ny og tilfeldig key hver gang


        elif choice == "2":
            krypter_melding( FLAG,b"h"*16)

        else:
            print( "Snakkes", )
            sys.exit( 0, )

