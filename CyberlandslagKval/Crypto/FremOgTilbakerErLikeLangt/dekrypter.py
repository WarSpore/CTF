# Denne filen er hvor du må gjøre endringer for å dekryptere riktig

from konverter import konverter_ascii_tall_til_bokstaver

# <----------- HER MÅ DU GJØRE NOE
def dekrypter_addisjon(talliste: list[int], nøkkel: int) -> list[int]:
    """
    Fyll inn hvordan man skal dekryptere
    """
    for i in range(len(talliste)):
        talliste[i] = (talliste[i]-nøkkel)
    return talliste
# HER MÅ DU GJØRE NOE ------------>

# <----------- HER MÅ DU GJØRE NOE
def dekrypter_multiplikasjon(talliste: list[int], nøkkel: int) -> list[int]:
    """
    Fyll inn hvordan man skal dekryptere
    """
    for i in range(len(talliste)):
        talliste[i] = (int(talliste[i]/nøkkel))
    return talliste
# HER MÅ DU GJØRE NOE ------------>

#Du trenger ikke gjøre noen endringer her
def dekrypter(talliste: list[int], multiplikasjonsnøkkel: int, addisjonsnøkkel: int) -> str:
    kryptert_flagg_del1 = talliste[:len(talliste)//2]
    dekryptert_flagg_del1 = dekrypter_addisjon(kryptert_flagg_del1, addisjonsnøkkel)
    try:
        print("Del 1 av flagget: ", konverter_ascii_tall_til_bokstaver(dekryptert_flagg_del1))
    except:
        print("Del 1 av kunne ikke konverteres til bokstaver, sjekk hvordan du dekrypterer addisjonen")

    kryptert_flagg_del2 = talliste[len(talliste)//2:]
    dekryptert_flagg_del2 = dekrypter_multiplikasjon(kryptert_flagg_del2, multiplikasjonsnøkkel)
    try:
        print("Del 2 av flagget: ", konverter_ascii_tall_til_bokstaver(dekryptert_flagg_del2))
    except:
        print("Del 2 av kunne ikke konverteres til bokstaver, sjekk hvordan du dekrypterer multiplikasjonen")
    return dekryptert_flagg_del1 + dekryptert_flagg_del2

"""Dette er det krypterte flagget, som er resultatet av å kjøre krypter.py"""
kryptert_flagg=[2727, 2733, 2722, 2728, 2748, 2674, 2735, 2711, 2676, 2739, 2678, 2676, 2707, 2720, 2680, 4940, 10830, 9025, 9500, 4845, 6745, 9025, 5225, 4655, 7220, 5320, 4940, 10165, 4845, 11875]
multiplikasjonsnøkkel=95
addisjonsnøkkel=2625

flagg_talliste = dekrypter(kryptert_flagg, multiplikasjonsnøkkel, addisjonsnøkkel)
try:
    flagg = konverter_ascii_tall_til_bokstaver(flagg_talliste)
    print("Gratulerer her er flagget ditt:", flagg)
except:
    print("Ser ut som det ikke er helt rett")