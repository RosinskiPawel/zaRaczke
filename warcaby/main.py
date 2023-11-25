from classes import *


def main():
    board1 = MainBoard()

    def plVsPl():
        player1 = Player(1, board1)
        player2 = Player(2, board1)
        print("Player vs. Player")

        while True:
            board1.view()
            print(
                f"Gracz {player1.id} ma {player1.score}\nGracz {player2.id} ma {player2.score}"
            )

            player1.moves()
            board1.view()
            player2.moves()
            # player2.move_comp()
            print()
            if player1.score == 12:
                print(f"Wygrał gracz {player1.id}")
                return False
            elif player2.score == 12:
                print(f"Wygrał gracz {player2.id}")
                return False

    def plVsComp():
        computer = Computer(2, board1)
        player1 = Player(1, board1)
        print("Player vs. Computer")

        while True:
            board1.view()
            print(
                f"Gracz {player1.id} ma {player1.score}\nGracz {computer.id} ma {computer.score}"
            )

            player1.moves()
            board1.view()
            computer.move_comp()
            print()
            if player1.score == 12:
                print(f"Wygrał gracz {player1.id}")
                return False
            elif computer.score == 12:
                print(f"Wygrał gracz {computer.id}")
                return False

    if (
        input("Wybierz rodzaj gry: 1 = Player vs. Player; 2 = Player vs. Computer\n")
        == "1"
    ):
        plVsPl()
    else:
        plVsComp()


if __name__ == "__main__":
    main()
