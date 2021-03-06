from math import *

# Rozkład liczby na czynniki pierwsze

def rozklad_na_czynniki_pierwsze():
    """
    Funkcja ta na podstawie liczby całkowitej podanej przez użytkownika obliczy jej rozkład na czynniki pierwsze
    """
    while True:
        try:
            n = int(input("Proszę podać liczbę do rozkładu na czynniki pierwsze: "))
            if n >= 0:
                break
            else:
                print("Wartość nie może być mniejsza od zero")
                continue
        except ValueError:
            print("Podana wartość nie jest liczbą stała")
            continue #omijamy pozostały kod i pytamy jeszcze raz użytkownika o wpisanie liczby
        else:
            print("Podana wartość jest prawidłowa")
            break
    a = 2
    r = []# zdefiniownie tablicy do przetrzymywania wyniku rozkladu
    while n % a == 0:
        n /= a
        r.append(a)
    b = 3
    while n > 1 & b <= sqrt(n):
        if n % b == 0:
            n = n/b
            r.append(b)
            b += 2
        else:
            print("Podana liczba jest liczbą pierwszą")
            break
    print("Rozkład podanej liczby na czynniki pierwsze %s" % ( r ))
    return r
    #end

print(rozklad_na_czynniki_pierwsze.__doc__)
rozklad_na_czynniki_pierwsze()





