import random
import re
import time
import copy

def simulate(num_sims, display=True):
    # starting game field
    results = []
    for i in range(num_sims):
        global game_board
        game_board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        state = 0

        if display is True:
            print('You have entered simulation mode.')
            time.sleep(1)   # wait 1 sec before proceeding

        while state is 0:
            simulate_move('X', game_board)

            if display is True:
                time.sleep(1)

            simulate_move('O', game_board)

            # only show in console if display=True
            if display is True:
                for row in game_board:
                    print(row)
                print('-'*15)

            # check for 3 in a row
            if check_for_three('X', game_board):
                state = 1
                break
            elif check_for_three('O', game_board):
                state = 2
                break

            # check for draw
            state = check_for_draw()

        results.append(state)
    return results


def check_for_draw():
    empty_spaces = [(r, p) for r in range(len(game_board))
                    for p in range(len(game_board[r]))
                    if game_board[r][p] is ' ']

    if len(empty_spaces) > 1:
        return 0
    else:
        # simulate
        board_copy = copy.deepcopy(game_board)  # make deep copy of game_board
        simulate_move('X', board_copy)

        if check_for_three('X', board_copy):
            return 1

        board_copy = copy.deepcopy(game_board)  # re store board to previous state
        simulate_move('O', board_copy)

        if check_for_three('O', board_copy):
            return 2

    return 3


def load_game():
    global first_or_second
    first_or_second = random.randint(1,2)
    global player_piece, cpu_piece

    global game_board
    game_board = [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]

    for row in game_board:
        print(row)

    if first_or_second is 1:
        player_piece = 'X'
        cpu_piece = 'O'
    else:
        player_piece = 'O'
        cpu_piece = 'X'

    print('Welcome to Tic-Tac-Toe!')
    print('For this game, you are (' + player_piece + ').')
    # print('Press Enter to start the game.')


def update_game():
    # calls player_move() and simulate_move()
    if first_or_second is 1:
        player_move()
        simulate_move(cpu_piece, game_board)

        for row in game_board:
            print(row)
    else:
        simulate_move(cpu_piece, game_board)

        for row in game_board:
            print(row)

        player_move()

    # check for 3 in a row
    if check_for_three(player_piece, game_board):
        return 1
    elif check_for_three(cpu_piece, game_board):
        return -1
    else:
        return 0


def check_for_three(piece, board):
    # check row, column, or diagonal
    for i in range(len(game_board)):
        if board[i][0] == board[i][1] == board[i][2] == piece:    # row
            return True
        if board[0][i] == board[1][i] == board[2][i] == piece:    # col
            return True

    if board[0][0] == board[1][1] == board[2][2] == piece:        # diagonal
        return True
    if board[0][2] == board[1][1] == board[2][0] == piece:        # diagonal
        return True

    return False


def check_board(row, col, board):
    if board[row][col] is ' ':
        return True
    else:
        return False


def simulate_move(piece, board):
    row = random.randint(0, 2)
    col = random.randint(0, 2)

    while check_board(row, col, board) is False:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

    board[row][col] = piece    # update the game board HERE


def player_move():

    while True:
        try:
            player_move = input('Type (row,column) of where you want to place (' + player_piece + ').')
            point = re.split(',', player_move)
            row = int(point[0])
            col = int(point[1])
            # point = [int(point[i]) for i in range(len(point))]

            if check_board(row, col, game_board):
                game_board[row][col] = player_piece  # update the game board HERE
                return
            else:
                print('You cannot move there.')
        except ValueError:
            print('Please enter (row,column) of your move.')
        except IndexError:
            print('That is off the board.')


if __name__ == '__main__':
    game_state = 0  # means game in progress, no win or loss
    load_game()

    while game_state is 0:
        game_state = update_game()

        if check_for_draw():
            game_state = 3

    if game_state is 1:
        print('You win :)')
    if game_state is 2:
        print('You lose :(')
    if game_state is 3:
        print('This game has ended in a draw.')

## END OF PROGRAM ##