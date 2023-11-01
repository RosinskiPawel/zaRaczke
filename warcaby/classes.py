# a, b, c, d, e, f, g, h = [], [], [], [], [], [], [], []


# for x in range(9):
#     d.append(0)
#     e.append(0)
#     if x % 2:
#         a.append(0)
#         b.append(1)
#         c.append(0)
#         f.append(1)
#         g.append(0)
#         h.append(1)
#     else:
#         a.append(1)
#         b.append(0)
#         c.append(1)
#         f.append(0)
#         g.append(1)
#         h.append(0)
# z = [a, b, c, d, e, f, g, h]
# for row in z:
#     print(row)
class Warcaby:
    def __init__(self):
        pass

    def crator(self):
        a, b, c = [[0 if (i + j) % 2 else 1 for i in range(8)] for j in range(3)]
        f, g, h = [[2 if (i + j) % 2 else 0 for i in range(8)] for j in range(3)]
        d, e = [[0 for x in range(8)] for x in range(2)]
        pool = [a, b, c, d, e, f, g, h]
        k = ["1", "2", "3", "4", "5", "6", "7", "8"]
        print("   " + "  ".join(k))
        print("   " + "-----------------------")
        z = [
            ("A", a),
            ("B", b),
            ("C", c),
            ("D", d),
            ("E", e),
            ("F", f),
            ("G", g),
            ("H", h),
        ]
        for variable, value in z:
            print(variable, value)
        return pool

        # z = [a, b, c, d, e, f, g, h]
        # for row in z:
        #     print("a", row)

    def get_coordinats(self):
        print("Podaj wspolrzedne pionka!")
        horizontal = input("rząd: ")
        vertical = int(input("kolumna: "))
        return horizontal, vertical

    def set_coordinats(self):
        pass

        # tak określona wartość w list zmienia sie na zero, a wartosc okreslona w funkcji set_coordinats zmienia sie na 1 lub 2

    # po wykonaniu bicia odbywa się liczenie pozostałych pionkow i wyswietlenie aktualnego stanu

    def move(self):
        pass

    def board(self):
        self.pool
        # tworzenie nowego widoku planszy: get_coordinats i set i zmiana wartości w dwóch listach
        # Może utworzyć osobną klase Board i po utworzniu master i wyświetleniu na początku wyciągać z niej wiersze (listy), aby potem je modyfikować i tworzyć z nich zaktualizowane widoki planszy
        pass


# jeżeli wybrae pole jest zajeta -> blad i powtorka
# gdy jest wolne, to pole w rzad+1 i kolumna+1 zmienia wartosc na zero,a pionek przechodzi na wybrane pole i ono zmienia wartosc na wart pionka
# jezeli wybrane pole ma kolumne wieksza od pola aktualnego pionk, to pole w rzad+1 i kolumna+1 zmienia wartosc na zero, a gdy ma kolumne mniejsza, to pole w rzad+1, ale kolumna-1 zmienia wartosc na zero
# gdy wybrane zostanie nowe pole o wartosciach rzad+1 i kol+1, to nie ma bicia i jest zwykły ruchu, zbijanie jest wowczas, gdy nowe współrzędnie mają obie wartości zwiększone/zmniejszone o '2'!!!
