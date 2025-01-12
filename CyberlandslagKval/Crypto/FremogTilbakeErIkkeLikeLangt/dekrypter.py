# Denne filen er hvor du må gjøre endringer for å dekryptere riktig
import math

from konverter import konverter_ascii_tall_til_bokstaver

# <----------- HER MÅ DU GJØRE NOE
def dekrypter_addisjon(talliste: list[int], nøkkel: int, modulus: int) -> list[int]:
    """
    Fyll inn hvordan man skal dekryptere
    """
    for i in range(len(talliste)):
        talliste[i] = (talliste[i]-nøkkel)
    return talliste

# HER MÅ DU GJØRE NOE ------------>

# <----------- HER MÅ DU GJØRE NOE

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def modular_inverse(a, n):
    """Calculate the modular inverse of a modulo n."""
    gcd, x, _ = extended_gcd(a, n)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist.")
    return x % n

def solve_modular_equation(r, e, n):
    """Solve the equation x * r ≡ e (mod n) for x."""
    r_inverse = modular_inverse(r, n)
    x = (e * r_inverse) % n
    return x

# Example usage:
r = 7
e = 3
n = 11
solution = solve_modular_equation(r, e, n)
print("Solution for x:", solution)




def dekrypter_multiplikasjon(talliste: list[int], nøkkel: int, modulus: int) -> list[int]:
    """
    Fyll inn hvordan man skal dekryptere
    """

    divsjoner = nøkkel//modulus
    print(divsjoner)


    for i in range(len(talliste)):
        talliste[i] = (int((solve_modular_equation(nøkkel, talliste[i], modulus)%modulus)))
    print(talliste)
    return talliste
# HER MÅ DU GJØRE NOE ------------>

#Du trenger ikke gjøre noen endringer her
def dekrypter(talliste: list[int], multiplikasjonsnøkkel: int, addisjonsnøkkel: int, modulus: int) -> str:
    kryptert_flagg_del1 = talliste[:len(talliste)//2]
    dekryptert_flagg_del1 = dekrypter_addisjon(kryptert_flagg_del1, addisjonsnøkkel, modulus)
    try:
        print("Del 1 av flagget: ", konverter_ascii_tall_til_bokstaver(dekryptert_flagg_del1))
    except:
        print("Del 1 av kunne ikke konverteres til bokstaver, sjekk hvordan du dekrypterer addisjonen")

    kryptert_flagg_del2 = talliste[len(talliste)//2:]
    dekryptert_flagg_del2 = dekrypter_multiplikasjon(kryptert_flagg_del2, multiplikasjonsnøkkel, modulus)
    try:
        print("Del 2 av flagget: ", konverter_ascii_tall_til_bokstaver(dekryptert_flagg_del2))
    except:
        print("Del 2 av kunne ikke konverteres til bokstaver, sjekk hvordan du dekrypterer multiplikasjonen")
    return dekryptert_flagg_del1 + dekryptert_flagg_del2

kryptert_flagg=[114842969321479669055974550468009989921, 114842969321479669055974550468009989927, 114842969321479669055974550468009989916, 114842969321479669055974550468009989922, 114842969321479669055974550468009989942, 114842969321479669055974550468009989901, 114842969321479669055974550468009989870, 114842969321479669055974550468009989876, 114842969321479669055974550468009989929, 114842969321479669055974550468009989868, 114842969321479669055974550468009989929, 114842969321479669055974550468009989876, 114842969321479669055974550468009989914, 114842969321479669055974550468009989928, 114842969321479669055974550468009989870, 114842969321479669055974550468009989919, 114842969321479669055974550468009989914, 114842969321479669055974550468009989896, 114842969321479669055974550468009989898, 114842969321479669055974550468009989887, 114842969321479669055974550468009989936, 114842969321479669055974550468009989927, 114842969321479669055974550468009989898, 114842969321479669055974550468009989914, 322722213567633186734298470466028854335, 324345140885510986345191829722050012390, 157628373952697654262094508944165763641, 74432283218078768181635184480825755072, 242122806541618780031268520812322698654, 319476358931877587512511751953986538225, 78002723317409927325600574844072302793, 242122806541618780031268520812322698654, 242447392005194339953447192663526930265, 78002723317409927325600574844072302793, 322397628104057626812119798614824622724, 319800944395453147434690423805190769836, 78002723317409927325600574844072302793, 74432283218078768181635184480825755072, 78002723317409927325600574844072302793, 241798221078043220109089848961118467043, 78002723317409927325600574844072302793, 155356275707668734806843805985736142364, 242122806541618780031268520812322698654, 76055210535956567792528543736846913127, 324345140885510986345191829722050012390, 319476358931877587512511751953986538225, 78002723317409927325600574844072302793, 155031690244093174884665134134531910753, 236280268197258701432052427490646529656]
modulus=328564751911993265333514563787705023333
multiplikasjonsnøkkel=53536293479237403136771386452840793549851257165175414513426616529791977472819
addisjonsnøkkel= 114842969321479669055974550468009989921-ord('f')

flagg_talliste = dekrypter(kryptert_flagg, multiplikasjonsnøkkel, addisjonsnøkkel, modulus)
try:
    flagg = konverter_ascii_tall_til_bokstaver(flagg_talliste)
    print("Gratulerer her er flagget ditt:", flagg)
except:
    print("Ser ut som det ikke er helt rett")