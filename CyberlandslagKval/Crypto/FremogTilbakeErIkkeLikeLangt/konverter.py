# Du trenger ikke se på denne filen, den bare konverterer tekst til liste med tall og motsatt

def konverter_bokstaver_til_ascii_tall(bokstaver: str) -> list[int]:
    """
    Konverterer tekst til en liste av tall basert på ascii verdier.
    Se asciitable.com for detaljer.
    Hver bokstav blir gjort om til et tall.

    >>> konverter_bokstaver_til_ascii_tall("Ab 1!")
    [65, 98, 32, 49, 33]
    >>> konverter_bokstaver_til_ascii_tall("flagg{lykke_til}")
    [102, 108, 97, 103, 103, 123, 108, 121, 107, 107, 101, 95, 116, 105, 108, 125]
    """
    output_list = []
    for bokstav in bokstaver:
        # Slår opp og finner riktig tall for hver bokstav
        konvertert_tall = ord(bokstav)
        print(konvertert_tall)
        output_list.append(konvertert_tall)
    return output_list


def konverter_ascii_tall_til_bokstaver(talliste: list[int]) -> str:
    """
    Konverterer en liste av ascii verdier til tekst.
    Se asciitable.com for detaljer.

    >>> konverter_ascii_tall_til_bokstaver([65, 98, 32, 49, 33])
    'Ab 1!'
    >>> konverter_ascii_tall_til_bokstaver([102, 108, 97, 103, 103, 123, 108, 121, 107, 107, 101, 95, 116, 105, 108, 125])
    'flagg{lykke_til}'
    """
    liste_av_bokstaver = []
    for tall in talliste:
        # Slår opp og finner riktig bokstav for hvert tall
        konvertert_bokstav = chr(tall)
        liste_av_bokstaver.append(konvertert_bokstav)
    # Slår sammen bokstavene i listen til en streng
    return "".join(liste_av_bokstaver)

if __name__ == "__main__":
    import doctest
    doctest.testmod()