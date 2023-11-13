class Comp:
    def __init__(self) -> None:
        pass

    def moveComp(self):
        getRowComp = 0


board = [
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0],
    [0, 2, 0, 2, 0, 0, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
]


matches = []
for index, row in enumerate(board):
    for j, value in enumerate(row):
        if value == 2:
            matches.append((index, j))

print(matches)

for x in board:
    print(x)
print()
for x in range(len(matches)):
    row = matches[x][0]
    col = matches[x][1]
    # ruch o jedno pole w lewo
    if board[row - 1][col - 1] == 0:
        board[row - 1][col - 1] = 2
        board[row][col] = 0
        break
    # ruch o jedno pole w prawo
    elif board[row - 1][col + (1 if col < 7 else 0)] == 0:
        board[row - 1][col + (1 if col < 7 else 0)] = 2
        board[row][col] = 0
        break
    # elif board[row - 1][0] == 1 or board[row - 1][7] == 1:
    #     continue
    # warunek, że nie wolno zbijać, gdy '1' na indexie 0 lub 7
    # elif board[row - 1][0] == 1 or board[row - 1][7] == 1:
    #     continue
    # elif board[row - 1][(col + 1)] == 1 and board[row - 2][(col + 2)] == 0:
    #     board[row - 1][col + 1] = 0
    #     board[row - 2][col + 2] = 2
    #     board[row][col] = 0
    #     break
    elif (
        board[row - 1][col + (1 if col < 7 else 0)] == 1
        and board[row - 2][col + (2 if col < 7 else 0)] == 0
    ):
        board[row - 1][col + 1] = 0
        board[row - 2][col + 2] = 2
        board[row][col] = 0
        break
    elif (
        board[row - 1][col - (1 if col > 1 else 0)] == 1
        and board[row - 2][col - (2 if col > 1 else 0)] == 0
    ):
        board[row - 1][col - 1] = 0
        board[row - 2][col - 2] = 2
        board[row][col] = 0
        break


for x in board:
    print(x)
