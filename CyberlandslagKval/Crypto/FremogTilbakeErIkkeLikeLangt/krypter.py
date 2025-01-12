# Denne filen viser hvordan flagget har blitt kryptert
import random
from Crypto.Util.number import getPrime #pip install pycryptodome

from konverter import konverter_bokstaver_til_ascii_tall

def krypter_med_addisjon(talliste: list[int], nøkkel: int, modulo: int) -> list[int]:
    """Krypterer liste med tall ved å legge til nøkkelen til hvert tall med modulo

    >>> krypter_med_addisjon([0, 1, 25, 27, 28], 30, 17)
    [13, 14, 4, 6, 7]
    """
    for i in range(len(talliste)):
        talliste[i] = (talliste[i]+nøkkel)%modulo
    return talliste

def krypter_med_multiplikasjon(talliste: list[int], nøkkel: int, modulo: int) -> list[int]:
    """Krypterer liste med tall ved å gange nøkkelen med hvert tall med modulo

    >>> krypter_med_multiplikasjon([0, 1, 25, 27, 28], 30, 17)
    [0, 13, 2, 11, 7]
    """
    for i in range(len(talliste)):
        talliste[i] = (talliste[i]*nøkkel)%modulo
    return talliste

def krypter(flagg: str, multiplikasjonsnøkkel: int, addisjonsnøkkel: int, modulus: int) -> list[int]:
    """Krypterer først halvdel av flagget med addisjon og den andre delen med multiplikasjon"""
    flagg_talliste = konverter_bokstaver_til_ascii_tall(flagg)
    flagg_del_1_kryptert = krypter_med_addisjon(flagg_talliste[:len(flagg)//2], addisjonsnøkkel, modulus)
    flagg_del_2_kryptert = krypter_med_multiplikasjon(flagg_talliste[len(flagg)//2:], multiplikasjonsnøkkel, modulus)
    return flagg_del_1_kryptert + flagg_del_2_kryptert

flagg = "flag{dette_er_ett_eksempel_flagg}"
multiplikasjonsnøkkel = random.getrandbits(256)
addisjonsnøkkel = random.getrandbits(256)
modulus = getPrime(128)
kryptert_flagg = krypter(flagg, multiplikasjonsnøkkel, addisjonsnøkkel, modulus)

print(f"{kryptert_flagg=}")
print(f"{modulus=}")
print(f"{multiplikasjonsnøkkel=}")
print(f"{addisjonsnøkkel=}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()