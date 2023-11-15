# from classes import Warcaby


# class Comp:
#     def __init__(self):
#         self.board = Warcaby.self.board


# matches = []
# for index, row in enumerate(Warcaby.self.board):
#     for j, value in enumerate(row):
#         if value == 2:
#             matches.append((index, j))


# board = [
#     [1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0],
#     [1, 0, 1, 0, 1, 0, 0, 0],
#     [0, 2, 0, 2, 0, 0, 0, 2],
#     [2, 0, 2, 0, 2, 0, 2, 0],
#     [0, 2, 0, 2, 0, 2, 0, 2],
# ]


# matches = []
# for index, row in enumerate(board):
#     for j, value in enumerate(row):
#         if value == 2:
#             matches.append((index, j))

# print(matches)

# for x in board:
#     print(x)
# print()
# for x in range(len(matches)):
#     row = matches[x][0]
#     col = matches[x][1]
#     # ruch o jedno pole w lewo
#     if board[row - 1][col - 1] == 0:
#         board[row - 1][col - 1] = 2
#         board[row][col] = 0
#         break
#     # ruch o jedno pole w prawo
#     elif board[row - 1][col + (1 if col < 7 else 0)] == 0:
#         board[row - 1][col + (1 if col < 7 else 0)] = 2
#         board[row][col] = 0
#         break

#     # bicie w prawo
#     elif (
#         board[row - 1][col + (1 if col < 7 else 0)] == 1
#         and board[row - 2][col + (2 if col < 7 else 0)] == 0
#     ):
#         board[row - 1][col + 1] = 0
#         board[row - 2][col + 2] = 2
#         board[row][col] = 0
#         break
#     # bicie w lewo
#     elif (
#         board[row - 1][col - (1 if col > 1 else 0)] == 1
#         and board[row - 2][col - (2 if col > 1 else 0)] == 0
#     ):
#         board[row - 1][col - 1] = 0
#         board[row - 2][col - 2] = 2
#         board[row][col] = 0
#         break


# for x in board:
#     print(x)
# ---------------------------------------------------------


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

    def move(self):
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        while True:
            print(f"Gracz {self.id}")

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
        pawn = self.board.board[letters.index(get_row)][get_col - 1]
        # w miejsce pobranego pionka zostaje wpisane 0
        self.board.board[letters.index(get_row)][get_col - 1] = 0

        # teraz ustalamy miejsce, na ktore przenosimy pobrany pionek ('1' lub '2') - z obsługą błędów
        while True:
            try:
                set_row = input("Podaj rząd docelowy: ")
                set_col = int(input("Podaj kolumnę docelową: "))
                # obsługa błędu przekroczenia zakresu a-h/1-8
                if set_row in letters and set_col in range(1, 9):
                    # obsługa błędu przeniesienia pionka na pole zajęte przez inny pionek
                    if self.board.board[letters.index(set_row)][set_col - 1] == 0:
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

        self.board.board[letters.index(set_row)][set_col - 1] = pawn

        if (
            abs(get_col - set_col) == 2
            and abs(letters.index(get_row) - letters.index(set_row)) == 2
        ):
            row = letters.index(get_row) + 1
            col = set_col + (1 if get_col < set_col else -1)
            self.board.board[row][col] = 0
            self.score += 1

        if pawn == 1 and letters.index(set_row) == 7:
            self.board.board[7][set_col - 1] = 0
            self.board.board[0][
                int(input("W której kolumnie umieścić pionek? ")) - 1
            ] = 1


class Computer(Player):
    def move_comp(self):
        print()
        print(f"Oto ruchu gracza {self.id}")
        # tworzenie listy z indeksami dostępnych pionków dla komputera (2)
        matches = []
        for index, row in enumerate(self.board.board):
            for j, value in enumerate(row):
                if value == 2:
                    matches.append((index, j))
        # iteracja, aby znalźć pierwszy dostępny pionek 2 i poniższej
        # sprawdzanie warunków do wykonania ruchów oraz bicia
        for x in range(len(matches)):
            row = matches[x][0]
            col = matches[x][1]
            # if col == 0 and self.board.board[row - 1][col + 1] == 0:
            #     self.board.board[row - 1][col + 1] = 2
            #     self.board.board[row][col] = 0
            #     break

            # ruch o jedno pole w lewo
            if self.board.board[row - 1][col - 1] == 0 and col in range(1, 7):
                self.board.board[row - 1][col - 1] = 2
                self.board.board[row][col] = 0
                break
            # ruch o jedno pole w prawo
            elif self.board.board[row - 1][col + 1] == 0 and col in range(0, 6):
                self.board.board[row - 1][col + 1] = 2
                self.board.board[row][col] = 0
                break

            # bicie w prawo
            elif (
                self.board.board[row - 1][col + (1 if col < 7 else 0)] == 1
                and self.board.board[row - 2][col + (2 if col < 7 else 0)] == 0
            ):
                self.board.board[row - 1][col + 1] = 0
                self.board.board[row - 2][col + 2] = 2
                self.board.board[row][col] = 0
                self.score += 1
                break
            # bicie w lewo
            elif (
                self.board.board[row - 1][col - (1 if col > 1 else 0)] == 1
                and self.board.board[row - 2][col - (2 if col > 1 else 0)] == 0
            ):
                self.board.board[row - 1][col - 1] = 0
                self.board.board[row - 2][col - 2] = 2
                self.board.board[row][col] = 0
                self.score += 1
                break


def main():
    board1 = MainBoard()
    player1 = Player(1, board=board1)
    player2 = Computer(2, board=board1)

    while player1.score or player2.score < 12:
        board1.view()
        player1.move()
        board1.view()
        player2.move_comp()


if __name__ == "__main__":
    main()
