from tkinter import *
import numpy as np

size_of_board = 600
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
symbol_X_color = '#EE4035'
symbol_O_color = '#0492CF'
Green_color = '#7BC043'

'''
==============================================***********=====================================================
    Author                                 changes 
--------------------------------------------------------------------------------------------------------------
Surya Majji      Made changes to the code such that it uses the tkinter UI components which makes the game 
                  more interactive

Surya Majji     implemented the class and method way such that code looks more organised
'''


class Game:
    def initialize_board(self):
        for i in range(2):
            self.canvas.create_line((i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)

        for i in range(2):
            self.canvas.create_line(0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

    def __init__(self):
        self.window = Tk()
        self.window.title('Tic-Tac-Toe')
        self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
        self.canvas.pack()
        # Input from user in form of clicks
        self.window.bind('<Button-1>', self.click)

        self.initialize_board()
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3, 3))

        self.player_X_starts = True
        self.reset_board = False
        self.game_over = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False

        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0

    def mainloop(self):
        self.window.mainloop()

    def play_again(self):
        self.initialize_board()
        self.player_X_starts = not self.player_X_starts
        self.player_X_turns = self.player_X_starts
        self.board_status = np.zeros(shape=(3, 3))

    def convert_logical_to_grid_position(self, logical_position):
        logical_position = np.array(logical_position, dtype=int)
        return (size_of_board / 3) * logical_position + size_of_board / 6

    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        return np.array(grid_position // (size_of_board / 3), dtype=int)

    # equivalent to is boardFUll method check for if the board has some empty spaces
    def is_grid_occupied(self, logical_position):
        if self.board_status[logical_position[0]][logical_position[1]] == 0:
            return False
        else:
            return True

    # created two different methods to insert two different signs of the players as this uses tkinter UI

    def draw_O(self, logical_position):
        logical_position = np.array(logical_position)
        # logical_position = grid value on the board
        # grid_position = actual pixel values of the center of the grid
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                outline=symbol_O_color)

    #method for drawing X to be implemented by shyam
    def is_winner(self, player):
        player = -1 if player == 'X' else 1

        # Three in a row
        for i in range(3):
            if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                return True
            if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                return True

        # Diagonals
        if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
            return True

        if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
            return True

        return False

    def is_tie(self):

        r, c = np.where(self.board_status == 0)
        tie = False
        if len(r) == 0:
            tie = True

        return tie

    @property
    def is_gameover(self):
        # Either someone wins or all grid occupied
        self.X_wins = self.is_winner('X')
        if not self.X_wins:
            self.O_wins = self.is_winner('O')

        if not self.O_wins:
            self.tie = self.is_tie()

        gameover = self.X_wins or self.O_wins or self.tie

        if self.X_wins:
            print('X wins')
        if self.O_wins:
            print('O wins')
        if self.tie:
            print('Its a tie')

        return gameover

    #Method to display the statistics of wins ands ties

if __name__ == "__main__":
    game_instance = Game()
    game_instance.mainloop()

#
# def computerMove():
#     possibleMoves = [ x for x, letter in enumerate(board) if letter == ' ' and x != 0]
#     move = 0
#
#     for let in ['O', 'X']:
#         for i in possibleMoves:
#             boardcopy = board[:]
#             boardcopy[i] = let
#             if IsWinner(boardcopy, let):
#                 move = i
#                 return move
#
#     cornersOpen = []
#     for i in possibleMoves:
#         if i in [1, 3, 7, 9]:
#             cornersOpen.append(i)
#
#     if len(cornersOpen) > 0:
#         move = selectRandom(cornersOpen)
#         return move
#
#     if 5 in possibleMoves:
#         move = 5
#         return move
#
#     edgesOpen = []
#     for i in possibleMoves:
#         if i in [2, 4, 6, 8]:
#             edgesOpen.append(i)
#
#     if len(edgesOpen) > 0:
#         move = selectRandom(edgesOpen)
#         return move
#
# def selectRandom(li):
#     import random
#     ln = len(li)
#     r = random.randrange(0, ln)
#     return li[r]
