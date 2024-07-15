"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_moves = 0
    o_moves = 0

    for row in board:
        x_moves += row.count(X)
        o_moves += row.count(O)

    if o_moves < x_moves:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == EMPTY:
                action_set.add((i, j))

    return action_set


def result(board, action):

    result_board = copy.deepcopy(board)
    action_set = actions(board)
    cur_player = player(board)
    if action in action_set:
        result_board[action[0]][action[1]] = cur_player
        return result_board
    else:
        raise NameError("Invalid Action !")


def winner(board):
    # horizontal
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O

    # Vertical
    row0, row1, row2 = board[0], board[1], board[2]
    for i in range(3):
        if row0[i] == row1[i] == row2[i]:
            return row0[i]

    # diagonal

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


def terminal(board):
    if winner(board) is not None:
        return True

    for row in board:
        if row.count(EMPTY) != 0:
            return False

    return True


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None

    cur_player = player(board)
    if cur_player == O:
        util_action = set()
        v = 2
        for action in actions(board):
            v2 = min(v, max_val(result(board, action)))
            if v2 != v:
                v = v2
                util_action.add((v, action))
        return min(util_action)[1]

    else:
        util_action = set()
        v = -2
        for action in actions(board):
            v2 = max(v, min_val(result(board, action)))
            if v != v2:
                v = v2
                util_action.add((v, action))
        print("max", util_action)
        return max(util_action)[1]


def min_val(board):
    if terminal(board):
        return utility(board)

    v = 2
    for action in actions(board):
        v = min(v, max_val(result(board,action)) )

    return v


def max_val(board):
    if terminal(board):
        return utility(board)

    v = -2
    for action in actions(board):
        v = max(v, min_val(result(board, action)))

    return v