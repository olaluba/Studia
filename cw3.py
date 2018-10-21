def ciag_fibonacciego_1():
    """
    Ciąg Fibonacciego metoda iteracyjna
    """
    while True:
        try:
            n = int(input("Proszę podać liczbę dziesiętną większą od 1: "))
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
    if n == 0 or n == 1:
        print("Wynik to 1")
    a = 0
    b = 1
    i = 0
    for i in range(n):
        b += a
        a = b - a
        i += 1
    print ("Wynik to:%d" % (a))
    return a, b

print (ciag_fibonacciego_1.__doc__)
ciag_fibonacciego_1()


