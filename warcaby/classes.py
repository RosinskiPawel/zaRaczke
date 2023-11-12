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
        player = 1
        while True:
            letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
            while True:
                print(f"Gracz nr {1 if player%2 else 2}")
                # ustalamy pionek do chwycenia przez określenie rzędu i kolumny,

                try:
                    get_row = input("Podaj rząd: ")
                    get_col = int(input("Podaj kolumnę: "))
                    # obsługa błędów w przypadku wyjścia poza zakres a-h oraz 1-8
                    if get_row in letters and get_col in range(1, 9):
                        break
                    else:
                        print("Błędna wartość")
                except ValueError:
                    print("Spróbuj ponownie")
            # określana wartość pionka: 1 lub 2
            pawn = self.board[letters.index(get_row)][get_col - 1]
            # w miejsce pobranego pionka zostaje wpisane 0
            self.board[letters.index(get_row)][get_col - 1] = 0

            # teraz ustalamy miejsce, na ktore przenosimy pobrany pionek ('1' lub '2') - z obsługą błędów
            while True:
                try:
                    set_row = input("Podaj rząd docelowy: ")
                    set_col = int(input("Podaj kolumnę docelową: "))
                    # obsługa błędu przekroczenia zakresu a-h/1-8
                    if set_row in letters and set_col in range(1, 9):
                        # obsługa błędu przeniesienia pionka na pole zajęte przez inny pionek
                        if self.board[letters.index(set_row)][set_col - 1] == 0:
                            # obsługa błędu ruchu do tyłu
                            if (
                                letters.index(set_row) > letters.index(get_row)
                                and pawn == 1
                                or letters.index(set_row) < letters.index(get_row)
                                and pawn == 2
                            ):
                                break
                            else:
                                print("Nie wolno poruszać się do tyłu!")
                        else:
                            print("To pole jest zajęte. Wybierz inne!")
                    else:
                        print("Błędna wartość")
                except ValueError:
                    print("Błędna wartość, spróbuj ponownie")

            # gdy pionek dojdzie do końca planszy, wówczas powraca na początek
            # gdy przy pionku '2' indeks docleowego rzędu  wynosi 0, wówczas pionek dociera do końca planszy,
            # wartość w tym miejscu przyjmuje 0 i pojawia się pytanie do jakiej kolumny wstawić '2' w rzędzie H o indeksie 7
            # i pionek jest ponownie dostepny do gry
            # w przypadku pionka '1' zmieniają się tylko indeksy, zasada taka sama
            # gdy nie zachodzi żaden z obu warunków, w zwykłej sytuacji w wybrane miejsce na planszy
            # zostaje umieszony pionek o określonej wyżej wartości 1 lub 2
            if pawn == 2 and letters.index(set_row) == 0:
                self.board[0][set_col - 1] = 0
                self.board[7][int(input("W której kolumnie umieścić pionek?")) - 1] = 2
            elif pawn == 1 and letters.index(set_row) == 7:
                self.board[7][set_col - 1] = 0
                self.board[0][int(input("W której kolumnie umieścić pionek?")) - 1] = 1
            else:
                self.board[letters.index(set_row)][set_col - 1] = pawn

            # ZBIJANIE!!!!
            # oto pierwotny kształt ustalania warunku bicia.
            # Bicie jest wówczas, gdy różnica między wartościami indeksów kolumn i wierszy wynosi 2/-2.
            # pionek między aktualną pozycją pionka gracza zbijającego a jego pozycją docelową zmienia wartość na zero,
            # określa się go przez odejmowanie lub dodawanie 1 lub 2 do wartości indeksów.

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

            # to jest uproszczona i bardziej kompaktowa wersja bicia
            if (
                abs(get_col - set_col) == 2
                and abs(letters.index(get_row) - letters.index(set_row)) == 2
            ):
                row = letters.index(get_row) + (
                    -1 if letters.index(get_row) > letters.index(set_row) else 1
                )
                col = set_col + (-2 if get_col < set_col else 0)
                self.board[row][col] = 0

            # Dodawanie punktów
            if abs(get_col - set_col) == 2 and pawn == 1:
                self.scoreOne += 1
            elif abs(get_col - set_col) == 2 and pawn == 2:
                self.scoreTwo += 1

            print()
            self.view()
            print(f"Gracz 1 ma {self.scoreOne}. Gracz 2 ma {self.scoreTwo}")
            player += 1

            # wygrywa gracz, który pierwszy zdobędzie 12 punktów
            if self.scoreOne == 12:
                print("Wygrał gracz pierwszy!")
            elif self.scoreTwo == 12:
                print("Wygrał gracz drugi!")
                question = input("Chcesz zagrać ponownie? (y/n)")
                if question == "y":
                    return True
                else:
                    break
