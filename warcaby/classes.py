class MainBoard:
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

    def view(self):
        # tworzenie widoku planszy z numeracją kolumn i nazwami wierszy
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


class Player:
    def __init__(self, id, board):
        self.id = id
        self.board = board
        self.score = 0
        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.pawn = 0

    # pobieranie pionka
    def getting_pawn(self):
        while True:
            print(f"Ruch gracza {self.id}")
            try:
                get_row_letter = input("Podaj rząd: ").lower()
                get_row = self.letters.index(get_row_letter)
                get_col = int(input("Podaj kolumnę: ")) - 1
                # obsługa błędów w przypadku wyjścia poza zakres a-h oraz 1-8
                if get_row_letter in self.letters and get_col in range(0, 8):
                    # gdy na podanych współrzęnych wystepuje 0
                    if self.board.board[get_row][get_col] != 0:
                        break
                    else:
                        print("Na tym polu nie ma twojego pionka.")
                else:
                    print("Błędna wartość")
            except ValueError:
                print("Spróbuj ponownie")
        # określana wartość pionka: 1 lub 2
        self.pawn = self.board.board[get_row][get_col]
        # w miejsce pobranego pionka zostaje wpisane 0
        self.board.board[get_row][get_col] = 0
        return [get_row, get_col]

    # wstawiania pionka na nową pozycję
    def setting_pawn(self, get_row, get_col):
        while True:
            self.pawn = self.pawn
            try:
                set_row_letter = input("Podaj rząd docelowy: ").lower()
                set_row = self.letters.index(set_row_letter)
                set_col = int(input("Podaj kolumnę docelową: ")) - 1
                # obsługa błędu przekroczenia zakresu a-h/1-8
                if set_row_letter in self.letters and set_col in range(0, 8):
                    # obsługa błędu przeniesienia pionka na pole zajęte przez inny pionek
                    if self.board.board[set_row][set_col] == 0:
                        # obsługa błędu ruchu do tyłu
                        if (
                            set_row > get_row
                            and self.pawn == 1
                            or set_row < get_row
                            and self.pawn == 2
                        ):
                            # błąd z powodu wybrania takiej samej kolumny
                            if set_col != get_col:
                                # błąd wybrania kolumny +2 przy wierszu +1 i na odwrót
                                if (
                                    abs(set_row - get_row) == 1
                                    and abs(set_col - get_col) == 1
                                ) or (
                                    abs(set_row - get_row) == 2
                                    and abs(set_col - get_col) == 2
                                ):
                                    break
                                else:
                                    print("Błędna kolumna lub rząd!")
                            else:
                                print("Błędna kolumna!")
                        else:
                            print("Nie wolno poruszać się do tyłu!")
                    else:
                        print("To pole jest zajęte!")
                else:
                    print("Wprowadzona współrzędne są poza planszą!")
            except ValueError:
                print("Spróbuj ponownie")

        self.board.board[set_row][set_col] = self.pawn
        return [set_row, set_col]

    # zbijanie
    def cepture(self, get_row, get_col, set_row, set_col):
        row = get_row + (-1 if set_row < get_row else 1)
        col = get_col + (-1 if set_col < get_col else 1)
        self.board.board[row][col] = 0
        self.score += 1
        print(f"Gracz {self.id} zdobywa punkt!")

    # gdy pionek dojdzie do konca planszy, gracz określa, gdzie może powrócić
    def boardEndPlayer(self, pawn, set_row, set_col):
        newrow = self.letters.index(input("W którym rzędzie wstawić pionek? ").lower())
        newcol = int(input("W której kolumnie wstawić pionek? ")) - 1
        self.board.board[set_row][set_col] = 0
        self.board.board[newrow][newcol] = pawn

    def moves(self):
        getting = self.getting_pawn()
        get_row = getting[0]
        get_col = getting[1]

        setting = self.setting_pawn(get_row, get_col)
        set_row = setting[0]
        set_col = setting[1]

        if abs(get_col - set_col) == 2 and abs(get_row - set_row) == 2:
            self.cepture(get_row, get_col, set_row, set_col)

        if self.pawn == 1 and set_row == 7 or self.pawn == 2 and set_row == 0:
            self.boardEndPlayer(self.pawn, set_row, set_col)


class Computer(Player):
    # sprawdza, czy mozliwe jest bicie w prawo
    def check_if_capture_right(self, match):
        row = match[0]
        col = match[1]
        # pionek musi byc w kolumnie w zakresie 1-6 i w rzędzie c-h
        if (
            col in range(0, 6)
            and row in range(2, 7)
            and self.board.board[row - 1][col + 1] == 1
            and self.board.board[row - 2][col + 2] == 0
        ):
            return True

    # bicie w prawo
    def capture_right(self, match):
        row = match[0]
        col = match[1]
        self.board.board[row - 1][col + 1] = 0
        self.board.board[row - 2][col + 2] = 2
        self.board.board[row][col] = 0
        self.score += 1
        print(f"Gracz {self.id}  zdobywa punkt!")

    # sprawdza, czy mozliwe jest bicie w lewo
    def check_if_capture_left(self, match):
        row = match[0]
        col = match[1]
        # pionek musi byc w kolumnie w zakresie 3-8 i w rzędzie c-h
        if (
            col in range(2, 8)
            and row in range(2, 7)
            and self.board.board[row - 1][col - 1] == 1
            and self.board.board[row - 2][col - 2] == 0
        ):
            return True

    # bicie w lewo
    def capture_left(self, match):
        row = match[0]
        col = match[1]
        self.board.board[row - 1][col - 1] = 0
        self.board.board[row - 2][col - 2] = 2
        self.board.board[row][col] = 0
        self.score += 1
        print(f"Gracz {self.id}  zdobywa punkt!")

    # sprawdza, czy mozliwy jest ruch w prawo
    def check_if_move_right(self, match):
        row = match[0]
        col = match[1]
        if self.board.board[row - 1][col + (1 if col < 7 else 0)] == 0 and col in range(
            0, 7
        ):
            return True

    # ruch w prawo
    def move_right(self, match):
        row = match[0]
        col = match[1]
        self.board.board[row - 1][col + 1] = 2
        self.board.board[row][col] = 0

    # sprawdza, czy mozliwy jest ruch w lewo
    def check_if_move_left(self, match):
        row = match[0]
        col = match[1]
        if self.board.board[row - 1][col - (1 if col > 0 else 0)] == 0 and col in range(
            1, 8
        ):
            return True

    # ruch w lewo
    def move_left(self, match):
        row = match[0]
        col = match[1]
        self.board.board[row - 1][col - 1] = 2
        self.board.board[row][col] = 0

    # dotrcie pionka do konca planszy i przejscie na poczatek
    def boardEnd(self, col):
        # pierwotne wspolrzedne pionkow komputera
        initial = [
            (7, 7),
            (7, 5),
            (7, 3),
            (7, 1),
            (6, 6),
            (6, 4),
            (6, 2),
            (6, 0),
            (5, 7),
            (5, 5),
            (5, 3),
            (5, 1),
        ]
        # jesli wiersz 'A' czyli row[0] i col 0 lub 2/4/6/ == 2, to w pierwszym wolnym polu z listy initial zostaje wstawione '2', a row[0] zostaje wyzerowany

        self.board.board[0][col] = 0
        # dla wspolrzednych z initial szuka miejsca o wart. 0, ale zaczyna od dołu planszy (rząd H) i w pierwszym wolnym miejscu wstawia "1"
        for z in initial:
            if self.board.board[z[0]][z[1]] == 2:
                continue
            elif self.board.board[z[0]][z[1]] == 0:
                self.board.board[z[0]][z[1]] = 2
                break

    # akcja wykonywana przez komputer
    def move_comp(self):
        print()
        print(f"Ruch gracza {self.id}")
        # tworzenie listy z indeksami dostępnych pionków dla komputera (2)
        matches = []
        for index, listInlist in enumerate(self.board.board):
            for indexListInList, valueListInList in enumerate(listInlist):
                if valueListInList == 2:
                    matches.append((index, indexListInList))

        # filtruje pionki (elementy z matches), które spełniają warunek bicia w prawo
        capt_right = list(filter(self.check_if_capture_right, matches))
        # czy możliwe bicie w lewo
        capt_left = list(filter(self.check_if_capture_left, matches))
        # czy możliwy ruch w prawo
        lst_move_right = list(filter(self.check_if_move_right, matches))
        # czy możliwy ruch w lewo
        lst_move_left = list(filter(self.check_if_move_left, matches))

        # gdy dany warunek jest spełniony, wykonuje bicie lub ruch o jedno pole
        if capt_right:
            self.capture_right((capt_right[0][0], capt_right[0][1]))
        elif capt_left:
            self.capture_left((capt_left[0][0], capt_left[0][1]))
        elif lst_move_right:
            self.move_right((lst_move_right[0][0], lst_move_right[0][1]))
        elif lst_move_left:
            self.move_left((lst_move_left[0][0], lst_move_left[0][1]))

        # sprawdza, czy pionek doszedl do konca planszy (0 i parzyste kolumny) i przenosi go na jedno z pierwotnych miejsc
        for col in range(0, 7, 2):
            if self.board.board[0][col] == 2:
                self.boardEnd(col)
                print(
                    f"Pionek gracza {self.id} doszedł do końca planszy = powrót na jedną z pierwotnych pozycji."
                )
