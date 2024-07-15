
import copy
EMPTY = None
X = "X"
O = "O"
l1=[[O, EMPTY, X],
    [O, X, EMPTY],
    [O, X, X]]

x_moves = 0
o_moves = 0

for row in l1:
        x_moves += row.count(X)
        o_moves += row.count(O)

print(x_moves, o_moves)

action_set = set()
for i, row in enumerate(l1):
    for j, col in enumerate(row):
        if col == EMPTY:
            action_set.add((i, j))

print(action_set)

action = (1,0)
result_board = copy.deepcopy(l1)
action_set = action_set
cur_player = O
if action in action_set:
    result_board[action[0]][action[1]] = cur_player
    print(result_board)
else:
    pass
    # raise NameError("Invalid Action !")

board = l1
for row in board:
    if row.count(X) == 3:
        print(X)
    if row.count(O) == 3:
        print(O)

# Vertical
row0, row1, row2 = board[0], board[1], board[2]
for i in range(3):
    if row0[i] == row1[i] == row2[i]:
        print(row0[i])

# diagonal

if board[0][0] == board[1][1] == board[2][2]:
    print( board[0][0] )

if board[0][2] == board[1][1] == board[2][0]:
    print(board[0][2])

print(None)