# Zad1
# Stwórz 3 klasy: Material, Ubrania, Sweter.
# Klasa: Material
# Atrybuty:
# - rodzaj,
# - długość
# - szerokość
# Metody:
# - konstruktor
# - wyświetl_nazwę
# Klasa: Ubrania
# Atrybuty:
# - rozmiar
# - kolor
# - dla_kogo
# Metody:
# - wyświetl_dane – do wyświetlania informacji o ubraniu
# klasa: Sweter
# Atrybuty:
# - rodzaj_swetra – np. Rozpinany, z golfem itd.
# Metody:
# - wyświetl_dane
# Ubrania dziedziczą po klasie Materiał, a Swetry po klasie Ubrania.
# Stwórz kilka instancji obiektów i sprawdź, które metody można wykorzystać.

class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print(f"Rodzaj materialu: {self.rodzaj}")


class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo, rodzaj, dlugosc, szerokosc):
        super().__init__(rodzaj, dlugosc, szerokosc)
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        print(f"Rozmiar: {self.rozmiar}, Kolor: {self.kolor}, Dla kogo: {self.dla_kogo}")


class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra, rozmiar, kolor, dla_kogo, rodzaj, dlugosc, szerokosc):
        super().__init__(rozmiar, kolor, dla_kogo, rodzaj, dlugosc, szerokosc)
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_info(self):
        print(f"Rodzaj swetra: {self.rodzaj_swetra}")


print("Zad1")
bawelna = Material("naturalne", 20, 40)
ubranie = Ubrania("M", "niebieski", "ja", "cieply", 50, 40)
sweterek = Sweter("kardigan", "XL", "czerwony", "ciebie", "wygodny", 20, 30)
print("Bawelna")
bawelna.wyswietl_nazwe()
print("\nUbranie")
ubranie.wyswietl_nazwe()
ubranie.wyswietl_dane()
print("\nSweterek")
sweterek.wyswietl_nazwe()
sweterek.wyswietl_dane()
sweterek.wyswietl_info()


# Zad2
# Przeciąż metodę ``__add__()`` dla klasy Kwadrat, która będzie zwracała instancje klasy Kwadrat o nowym boku,
# będącym sumą długości boku kwadratu oraz obwodu kwadratu


class Kwadrat:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Kwadrat(self.x + (4 * other.x))

    def __str__(self):
        return f"Kwadrat o boku {self.x}"


print("\nZad2")
kwadracik = Kwadrat(4)
kwadratek = Kwadrat(5)
kwadratki = kwadracik + kwadratek
print(kwadratki)


# Zad3 Poczytaj o metodach `__ge__, __gt__, __le__, __lt__,` przeciąż je i spróbuj wykorzystać w instrukcji
# warunkowej do porównania dwóch instancji obiektów klasy Kwadrat.


class Kwadrat2:
    def __init__(self, x):
        self.x = x

    def __ge__(self, other):
        return self.x >= other.x

    def __gt__(self, other):
        return self.x > other.x

    def __lt__(self, other):
        return self.x < other.x

    def __le__(self, other):
        return self.x <= other.x

    def __str__(self):
        return f"Kwadrat o boku {self.x}"


print("\nZad3")
kw1 = Kwadrat2(5)
kw2 = Kwadrat2(10)
if kw1 >= kw2:
    print("ex1 = tak")
else:
    print("ex1 = nie")
if kw2 <= kw2:
    print("ex2 = tak")
else:
    print("ex2 = nie")

# Zad4
# Korzystając z powyższego kodu stwórz kilka instancji klasy Point i spróbuj odwołać się do zmiennej counter z
# poziomu różnych instancji, porównując jej wartość dla każdej z nich oraz spróbuj zmienić jej wartość.


class Point:
    counter = []

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)


print("\nZad4")
p1 = Point(2, 4)
p2 = Point(3, 1)
print(p1.counter)
print(p2.counter)
p1.update(2)
p2.update(4)
print(p1.counter)
print(p2.counter)

# Zad5
# Za pomocą funkcji `isinstance()` oraz `issubclass()` sprawdź wynik dla instancji obiektu `Pracownik` oraz
# `Menadzer` dla klas `Osoba, Pracownik i Manadzer`.


class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return f"{self.imie, self.nazwisko}"


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, pensja):
        self.pensja = pensja
        super().__init__(imie, nazwisko)

    def przedstaw_sie(self):
        return f"{self.imie} {self.nazwisko} i zarabiam {self.pensja}"


class Menadzer(Pracownik):
    def __init__(self, imie, nazwisko, pensja):
        super().__init__(imie, nazwisko, pensja)

    def przedstaw_sie(self):
        return f"{self.imie} {self.nazwisko} jestem menadzerem i zarabiam {self.pensja}"


print("\nZad5")
prac = Pracownik("a", "b", 2000)
mene = Menadzer("a", "b", 2000)
print("Pracownik issubclass:", issubclass(Pracownik, (Osoba, Pracownik, Menadzer)))
print("Pracownik isinstance:", isinstance(prac, (Osoba, Pracownik, Menadzer)))
print("Menadzer issubclass:", issubclass(Menadzer, (Osoba, Pracownik, Menadzer)))
print("Menadzer isinstance:", isinstance(prac, (Osoba, Pracownik, Menadzer)))

# Zad6
# Przetestuj powyższy iterator na kilku różnych kolekcjach.
#
# Gdzie jest ten iterator ????
#
# Zad7
# Napisz własny iterator, który będzie zwracał tylko elementy z parzystych indeksów przekazanej kolekcji.


class Parzyste:
    def __init__(self, kolekcja):
        self.kolekcja = kolekcja
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.kolekcja):
            raise StopIteration
        wynik = self.kolekcja[self.index]
        self.index += 2
        return wynik


print("\nZad7")
kolekcja1 = "bagno"
para = Parzyste(kolekcja1)
iteracja = iter(para)

for i in iteracja:
    print(i)

# Zad8 Napisz własny iterator, który będzie zwracał tylko samogłoski z przekazanego ciągu tekstowego. Zaimplementuj
# sprawdzanie czy przekazany został string jako argument konstruktora tego iteratora (sprawdź funkcję `isinstance()`).


class Samogloski:
    def __init__(self, tekst):
        self.tekst = tekst
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not isinstance(self.tekst, str):
            print(f"Tekst nie jest typu string")
            raise StopIteration

        if self.i == len(self.tekst):
            raise StopIteration
        litera = self.tekst[self.i]
        self.i += 1
        if litera in "aeiouy":
            return litera
        else:
            return self.__next__()


print("\nZad8")
alfabet = "abcdefghijklmnopqrstuvwxyz"
alfa = Samogloski(alfabet)
iteracja2 = iter(alfa)
liczby = 1234
l1 = Samogloski(liczby)
iteracja3 = iter(l1)

for i in iteracja2:
    print(i)

for i in iteracja3:
    print(i)

# Zad9
# Przepisz jeden z napisanych przez siebie iteratorow na generator


def parzyste1(kolekcja):
    for index in range(len(kolekcja)):
        if index % 2 == 0:
            yield kolekcja[index]


print("\nZad9")
tekst2 = "balalaika"
kolekcja2 = parzyste1(tekst2)

while 1:
    try:
        print(next(kolekcja2))
    except StopIteration:
        break

# Zad10
# Napisz generator, ktory bedzie zwracal kolejne wartosci ciagu arytmetycznego


def ciagaryt(n, a1, r):
    for n in range(1, n + 1):
        yield f"a{n} = {a1 + (n - 1) * r}"


print("\nZad10")
ciag1 = ciagaryt(5, 3, 1.5)

while 1:
    try:
        print(next(ciag1))
    except StopIteration:
        break
