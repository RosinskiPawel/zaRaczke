from classes import *


def main():
    gra = Warcaby()

    # gra.crator()
    # print(gra.get_vert())
    # print(gra.get_hor())
    gra.view()

    def get_koord():
        j = gra.board[gra.get_hor()][gra.get_vert()]
        print(j)

    get_koord()


if __name__ == "__main__":
    main()
