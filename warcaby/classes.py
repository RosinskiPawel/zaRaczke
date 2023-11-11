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
        self.board = [
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0],
            [0, 2, 0, 2, 0, 2, 0, 2],
        ]
        self.scoreOne = 0
        self.scoreTwo = 0

    # def crator(self):
    #     a, b, c = [[0 if (i + j) % 2 else 1 for i in range(8)] for j in range(3)]
    #     f, g, h = [[2 if (i + j) % 2 else 0 for i in range(8)] for j in range(3)]
    #     d, e = [[0 for x in range(8)] for x in range(2)]
    #     pool = [a, b, c, d, e, f, g, h]
    #     k = ["1", "2", "3", "4", "5", "6", "7", "8"]
    #     print("   " + "  ".join(k))
    #     print("   " + "-----------------------")
    #     z = [
    #         ("A", a),
    #         ("B", b),
    #         ("C", c),
    #         ("D", d),
    #         ("E", e),
    #         ("F", f),
    #         ("G", g),
    #         ("H", h),
    #     ]
    #     for variable, value in z:
    #         print(variable, value)
    #     return pool

    # z = [a, b, c, d, e, f, g, h]
    # for row in z:
    #     print("a", row)

    def view(self):
        z = [
            ("A", self.board[0]),
            ("B", self.board[1]),
            ("C", self.board[2]),
            ("D", self.board[3]),
            ("E", self.board[4]),
            ("F", self.board[5]),
            ("G", self.board[6]),
            ("H", self.board[7]),
        ]
        k = ["1", "2", "3", "4", "5", "6", "7", "8"]
        print("    " + " ".join(k))
        print("   " + "-----------------")
        for variable, value in z:
            print(variable, "[", *value, "]")

    # def get_hor(self):
    #     letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    #     horizontal = input("podaj rząd: ")
    #     if horizontal in letters:
    #         return letters.index(horizontal)

    # def get_vert(self):
    #     vertical = int(input("Podaj kolumnę: "))
    #     return vertical - 1

    def move(self):
        while True:
            letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

            # ustalamy pionek do przeniesienia
            while True:
                try:
                    get_h = input("podaj rząd: ")
                    get_v = int(input("Podaj kolumnę: "))
                    # pionek w przypadku gracza pierwsze to '1', a drugiego to '2' zostaje pobrany/chwycony i jego pole jest puste i zmienia teraz wartość na '0', ale wartość pionek pozostaje niezmieniona i zostanie użyta w dalszej części
                    if get_h in letters or get_v in range(1, 9):
                        break
                    else:
                        print("błędna wartości")
                except ValueError:
                    print("spróuj ponownie")

            pionek = self.board[letters.index(get_h)][get_v - 1]

            self.board[letters.index(get_h)][get_v - 1] = 0
            # teraz ustalamy miejsce, na ktore przenosimy pobrany pionek ('1' lub '2')
            set_h = input("podaj rząd docelowy: ")
            set_v = int(input("Podaj kolumnę docelową: "))
            # wartosc na nowym miejscu zmienia się na wartość pionka pobranego/chwyconego wyzej

            # ZBIJANIE!!!!
            if (
                get_v - set_v == -2
                and letters.index(get_h) - letters.index(set_h) == -2
            ):
                self.board[letters.index(get_h) + 1][get_v] = 0
            elif (
                get_v - set_v == 2 and letters.index(get_h) - letters.index(set_h) == -2
            ):
                self.board[letters.index(get_h) + 1][get_v - 2] = 0
            elif (
                get_v - set_v == 2 and letters.index(get_h) - letters.index(set_h) == 2
            ):
                self.board[letters.index(get_h) - 1][get_v - 2] = 0
            elif (
                get_v - set_v == -2 and letters.index(get_h) - letters.index(set_h) == 2
            ):
                self.board[letters.index(get_h) - 1][get_v] = 0

            if abs(get_v - set_v) == 2 and pionek == 1:
                self.scoreOne += 1
            elif abs(get_v - set_v) == 2 and pionek == 2:
                self.scoreTwo += 1

            self.board[letters.index(set_h)][set_v - 1] = pionek

            #     self.board[letters.index(set_h) + 1][set_v - 1] = 0
            # else:
            #     self.board[letters.index(get_h) + 1][get_v + 1] = 0

            # if abs(set_v - get_v) == 2, to jest bicie !!!!!
            # pionek do zbicia jest na self.board[letters.index(set_h)-1][set_v-/+1] minus 1 jesli (set_v - get_v) hest ujemne lub plus jeden jesli (set_v - get_v) jest dodatnie

            print()
            self.view()
            print(f"Gracz 1 ma {self.scoreOne}. Gracz 2 ma {self.scoreTwo}")
            if self.scoreOne == 12:
                print("wygał gracz pierwszy")
            elif self.scoreTwo == 12:
                print("wybrał gracz drugi")
                question = input("chcesz zagrać ponownie? (y/n)")
                if question == "y":
                    return True
                else:
                    break

        # TODO 1) obsługa błędów (pole zajęte, za duży skok, wyjście poza zasięg tablicy)


# może by tę funkcję rozbić na mniejsze - chyba bedzie konieczne, bo musi dojść jeszcz BICIE

# po wykonaniu bicia odbywa się liczenie pozostałych pionkow i wyswietlenie aktualnego stanu


# jeżeli wybrae pole jest zajeta -> blad i powtorka
# gdy jest wolne, to pole w rzad+1 i kolumna+1 zmienia wartosc na zero,a pionek przechodzi na wybrane pole i ono zmienia wartosc na wart pionka
# jezeli wybrane pole ma kolumne wieksza od pola aktualnego pionk, to pole w rzad+1 i kolumna+1 zmienia wartosc na zero, a gdy ma kolumne mniejsza, to pole w rzad+1, ale kolumna-1 zmienia wartosc na zero
# gdy wybrane zostanie nowe pole o wartosciach rzad+1 i kol+1, to nie ma bicia i jest zwykły ruchu, zbijanie jest wowczas, gdy nowe współrzędnie mają obie wartości zwiększone/zmniejszone o '2'!!!
