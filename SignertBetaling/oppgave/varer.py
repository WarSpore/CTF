importer os


klasse Vare:
    def __init__(selv, navn, pris, beskrivelse):
        selv.navn = navn
        selv.pris = pris
        selv.beskrivelse = beskrivelse


varer = [
    Vare("Banan", 10, "God og gul"),
    Vare("Eple", 5, "Sunt og godt"),
    Vare("Appelsin", 8, "Søt og saftig"),
    Vare("Pære", 7, "Saftig og god"),
    Vare("Kiwi", 12, "Grønn og god"),
    Vare("Ananas", 15, "Stor og rund"),
    Vare("Mango", 20, "Søt og god"),
    Vare("Drue", 25, "Liten og søt"),
    Vare("Flagg", 110, os.environ["FLAGG"])
]