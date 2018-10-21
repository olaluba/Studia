def dziesietna_na_binarna():
    """
    Algorytm przekształcenia liczby z postaci dziesiętnej na binarną
    """
    while True:
        try:
            n = int(input("Proszę podać liczbę dziesiętną większą od 0: "))
            if n >= 0:
                break
            else:
                print("Wartość nie może być mniejsza od zero")
                continue
        except ValueError:
            print("Podana wartość nie jest liczbą stała")
            continue #omijamy pozostały kod i pytamy jeszcze raz użytkownika o wpisanie liczby
        if n == 0:
            print("Proszę podać liczbę większą od zera")
            continue
        else:
            print("Podana wartość jest prawidłowa")
            break
    a = 2
    r = []
    while n >= 1:
        c = int(n % a)
        n /= a
        r.append(c)
    print("Wynik przekształcenia %s" % r)
    return r

print(dziesietna_na_binarna.__doc__)
dziesietna_na_binarna()




