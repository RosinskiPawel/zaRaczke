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

    def move(self):
        while True:
            letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

            # ustalamy pionek do przeniesienia
            # pionek w przypadku gracza pierwsze to '1', a drugiego to '2' zostaje pobrany/chwycony i jego pole jest puste i zmienia teraz wartość na '0', ale wartość pionek pozostaje niezmieniona i zostanie użyta w dalszej części
            # obsługa błędu w przypadku próby określenia pionka spoza dostępnego zakresu
            while True:
                try:
                    get_row = input("podaj rząd: ")
                    get_col = int(input("Podaj kolumnę: "))
                    if get_row in letters and get_col in range(1, 9):
                        break
                    else:
                        print("błędna wartości")
                except ValueError:
                    print("spróuj ponownie")

            pawn = self.board[letters.index(get_row)][get_col - 1]

            self.board[letters.index(get_row)][get_col - 1] = 0
            # teraz ustalamy miejsce, na ktore przenosimy pobrany pionek ('1' lub '2') - z obsługą błędu

            while True:
                try:
                    set_row = input("podaj rząd docelowy: ")
                    set_col = int(input("Podaj kolumnę docelową: "))
                    if set_row in letters and set_col in range(1, 9):
                        if self.board[letters.index(set_row)][set_col - 1] == 0:
                            break
                        else:
                            print("To pole jest zajęte. Wybierz inne!")
                    else:
                        print("błędna wartość")
                except ValueError:
                    print("błędna wartości, spróuj ponownie")
            self.board[letters.index(set_row)][set_col - 1] = pawn
            # wartosc na nowym miejscu zmienia się na wartość pionka pobranego/chwyconego wyzej

            # ZBIJANIE!!!!
            # if (
            #     get_col - set_col == -2
            #     and letters.index(get_row) - letters.index(set_row) == -2
            # ):
            #     self.board[letters.index(get_row) + 1][get_col] = 0
            # elif (
            #     get_col - set_col == 2
            #     and letters.index(get_row) - letters.index(set_row) == -2
            # ):
            #     self.board[letters.index(get_row) + 1][get_col - 2] = 0
            # elif (
            #     get_col - set_col == 2
            #     and letters.index(get_row) - letters.index(set_row) == 2
            # ):
            #     self.board[letters.index(get_row) - 1][get_col - 2] = 0
            # elif (
            #     get_col - set_col == -2
            #     and letters.index(get_row) - letters.index(set_row) == 2
            # ):
            #     self.board[letters.index(get_row) - 1][get_col] = 0

            if (
                abs(get_col - set_col) == 2
                and abs(letters.index(get_row) - letters.index(set_row)) == 2
            ):
                row = letters.index(get_row) + (
                    -1 if letters.index(get_row) > letters.index(set_row) else 1
                )
                col = set_col + (-2 if get_col < set_col else 0)
                self.board[row][col] = 0

            if abs(get_col - set_col) == 2 and pawn == 1:
                self.scoreOne += 1
            elif abs(get_col - set_col) == 2 and pawn == 2:
                self.scoreTwo += 1

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
