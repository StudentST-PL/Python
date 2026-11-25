'''
class DodajWykrzyknik:
    def __init__(self, funkcja):
        self.funkcja = funkcja

    def __call__(self, *args, **kwargs):
        wynik = self.funkcja(*args, **kwargs)
        return wynik + "!"

@DodajWykrzyknik
def przywitaj(imie):
    return f"Cześć, {imie}"

print(przywitaj("Jan"))
'''

class duze_litery:
    def __init__(self, funkcja):
        self.funkcja = funkcja

    def __call__(self, *args, **kwargs):
        wynik = self.funkcja(*args, **kwargs)
        return wynik.upper()


@duze_litery
def cyfry(tekst):
    cyfry = {
        '0': 'zero', '1': 'jeden', '2': 'dwa', '3': 'trzy', '4': 'cztery',
        '5': 'pięć', '6': 'sześć', '7': 'siedem', '8': 'osiem', '9': 'dziewięć'
    }
    wynik = ""
    
    for znak in tekst:
        if znak in cyfry:
            wynik = wynik + cyfry[znak] + " "

    return wynik.strip()
    

def zwroc_napis(*dane, sep=" ", end="\n"):
    tekst = ""
    for x in dane:
        tekst += str(x) + sep
    tekst = tekst[:-len(sep)]
    tekst += end
    return tekst
    
zwroc_napis = duze_litery(zwroc_napis)
    
def main():
    print(cyfry("1410"))
    print(zwroc_napis("Ala", "ma", "kota", sep="-"))

main()

