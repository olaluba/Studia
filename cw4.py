"""Korzystając z odpowiedniego typu danych stwórz sekwencję samogłosek.
Napisz funkcję, która wypisze podstawowe parametry tego zbioru: ilość elementów,
ilość powtórzeń dla każdego elementu i same elementy"""

def licznik_samoglosek():
    while True:
        try:
            n = str(input("Wpisz dowolne zdanie lub pojedyńczy wyraz: "))
            if len(n) == 0:
                print("Nie wpisano nic")
                continue
        except ValueError:
            print("Podana wartość nie jest liczbą stała")
            continue #omijamy pozostały kod i pytamy jeszcze raz użytkownika o wpisanie liczby
        else:
            print("Podana wartość jest prawidłowa")
            break
    wyraz = n.lower()
    samogloski = ('a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y')
    i = 0
    j = 0
    licznik = 0
    wynik = []
    wyraz = tuple(n)
    print(wyraz)
    for i in wyraz:
        for j in samogloski:
            if wyraz[i] == samogloski[j]:
                licznik += 1
                wynik.append(samogloski(j))
    print("Liczba wystapien samoglosek %d" % licznik)
    print("Lista samogłosek, który wystąpiły %s " % wynik)

licznik_samoglosek()


