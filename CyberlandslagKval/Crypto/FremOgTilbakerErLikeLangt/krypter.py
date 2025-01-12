# Denne filen viser hvordan flagget har blitt kryptert
import random

from konverter import konverter_bokstaver_til_ascii_tall

def krypter_med_addisjon(talliste: list[int], nøkkel: int) -> list[int]:
    """Krypterer liste med tall ved å legge til nøkkelen til hvert tall

    >>> krypter_med_addisjon([0, 1, 25, 27, 28], 1000)
    [1000, 1001, 1025, 1027, 1028]
    """
    for i in range(len(talliste)):
        talliste[i] += nøkkel
    return talliste

def krypter_med_multiplikasjon(talliste: list[int], nøkkel: int) -> list[int]:
    """Krypterer liste med tall ved å gange nøkkelen med hvert tall

    >>> krypter_med_multiplikasjon([0, 1, 25, 27, 28], 1000)
    [0, 1000, 25000, 27000, 28000]
    """
    for i in range(len(talliste)):
        talliste[i] *= nøkkel
    return talliste

def krypter(flagg: str, multiplikasjonsnøkkel: int, addisjonsnøkkel: int) -> list[int]:
    """Krypterer først halvdel av flagget med addisjon og den andre delen med multiplikasjon"""
    flagg_talliste = konverter_bokstaver_til_ascii_tall(flagg)
    flagg_del_1_kryptert = krypter_med_addisjon(flagg_talliste[:len(flagg)//2], addisjonsnøkkel)
    flagg_del_2_kryptert = krypter_med_multiplikasjon(flagg_talliste[len(flagg)//2:], multiplikasjonsnøkkel)
    return flagg_del_1_kryptert + flagg_del_2_kryptert

flagg = "flag{dette_er_ett_eksempel_flagg}"
multiplikasjonsnøkkel = random.randint(10,100)
addisjonsnøkkel = random.randint(100,10000)
kryptert_flagg = krypter(flagg, multiplikasjonsnøkkel, addisjonsnøkkel)

print(f"{kryptert_flagg=}")
print(f"{multiplikasjonsnøkkel=}")
print(f"{addisjonsnøkkel=}")