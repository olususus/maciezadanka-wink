# Klasa KontoBankowe:
# Dodaj klasę KontoBankowe, która będzie symulować działanie konta bankowego.
# Klasa powinna mieć atrybuty takie jak numer_konta, saldo oraz wlasciciel.
# Metoda __init__ powinna inicjalizować nowe konto bankowe.
# Metoda klasowa zaloz_konto(cls, numer, wlasciciel, saldo_poczatkowe) może być wykorzystana do założenia nowego konta.
# Metoda przelew pozwala na przelanie określonej kwoty z jednego konta na drugie.
class KontoBankowe:
    liczba_kont = 0

    def __init__(self, numer_konta, wlasciciel, saldo=0):
        self.numer_konta = numer_konta
        self.wlasciciel = wlasciciel
        self.saldo = saldo
        KontoBankowe.liczba_kont += 1

    @classmethod
    def zaloz_konto(cls, numer, wlasciciel, saldo_poczatkowe=0):
        return cls(numer, wlasciciel, saldo_poczatkowe)

    def przelew(self, inne_konto, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota
            inne_konto.saldo += kwota
            print(f'Wykonano przelew na kwotę {kwota} zł z konta {self.numer_konta} na konto {inne_konto.numer_konta}.')
        else:
            print('Brak wystarczających środków na koncie.')

# Przykładowe użycie:
konto1 = KontoBankowe.zaloz_konto('123456789', 'Jan Kowalski', 1000)
konto2 = KontoBankowe.zaloz_konto('987654321', 'Anna Nowak', 500)

konto1.przelew(konto2, 300)


# Klasa Osoba i dekorator @staticmethod:
# Stwórz klasę Osoba, która będzie reprezentować dane osobowe.
# Dodaj statyczną metodę sprawdz_pesel, która będzie służyć do walidacji numeru PESEL.
# Weryfikacja numeru PESEL powinna sprawdzać jego poprawność według algorytmu kontrolnego.
# python

class Osoba:
    def __init__(self, imie, nazwisko, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel

    @staticmethod
    def sprawdz_pesel(pesel):
        if len(pesel) != 11:
            return False
        if not pesel.isdigit():
            return False
        weights = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
        checksum = sum(int(pesel[i]) * weights[i] for i in range(10))
        checksum = (10 - (checksum % 10)) % 10
        return checksum == int(pesel[10])

# Przykładowe użycie:
pesel = '12345678901'
if Osoba.sprawdz_pesel(pesel):
    print(f'Numer PESEL {pesel} jest poprawny.')
else:
    print(f'Numer PESEL {pesel} jest niepoprawny.')

# Klasa Samochod z metodami klasowymi:
# Stwórz klasę Samochod, która będzie reprezentować różne modele samochodów.
# Dodaj metodę klasową srednia_cena(cls, *ceny), która obliczy średnią cenę samochodów na podstawie przekazanych cen.
# Metoda najdrozszy_samochod(cls, **samochody) powinna zwracać model najdroższego samochodu na podstawie przekazanych argumentów nazwa_ceny.

class Samochod:
    def __init__(self, model, cena):
        self.model = model
        self.cena = cena

    @classmethod
    def srednia_cena(cls, *ceny):
        return sum(ceny) / len(ceny)

    @staticmethod
    def najdrozszy_samochod(**samochody):
        najdrozszy_model = None
        najwyzsza_cena = 0
        for model, cena in samochody.items():
            if cena > najwyzsza_cena:
                najdrozszy_model = model
                najwyzsza_cena = cena
        return najdrozszy_model

# Przykładowe użycie:
ceny_samochodow = [25000, 30000, 35000, 40000]
srednia_cena = Samochod.srednia_cena(*ceny_samochodow)
print(f'Średnia cena samochodów wynosi: {srednia_cena}')

najdrozszy_model = Samochod.najdrozszy_samochod(BMW=45000, Audi=42000, Mercedes=48000)
print(f'Najdroższy model samochodu to: {najdrozszy_model}')

# Klasa Kalkulator z metodą klasową:
# Stwórz klasę Kalkulator, która będzie zawierać różne operacje matematyczne.
# Dodaj metodę klasową dodaj(cls, x, y), która zwróci sumę dwóch liczb.
# Metoda odejmij(cls, x, y) powinna zwrócić różnicę między dwoma liczbami.

class Kalkulator:
    @classmethod
    def dodaj(cls, x, y):
        return x + y

    @classmethod
    def odejmij(cls, x, y):
        return x - y

# Przykładowe użycie:
suma = Kalkulator.dodaj(10, 5)
print(f'Wynik dodawania: {suma}')

roznica = Kalkulator.odejmij(20, 8)
print(f'Wynik odejmowania: {roznica}')

