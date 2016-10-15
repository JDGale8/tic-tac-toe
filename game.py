# Pseudo code

# Functionality:

# Allows user input of a square
#   for now make user always X, can change between them with a bool, or an input line
# Has computer generated responses
# Can check if either player has won
#
# Draws a board


# ideally - Has machine learning aspects that allow a number of supervised training situations
# that will teach the game how to play and be undefeatable

class Game:

    def __init__(self):
        pass
        # initiate blank arrays for both players to represent the board
        self.board = [0]*9
        # for player vs computer games, have a counter saying who's go it is
        self.turn_count = 1
        # this will increment with each turn
        #   we can use the mod of this to determine who's go it is

    def draw(self):
        pass
        9.
        print('   |   |')

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
        # draw the board with the computer and user choices
        # use print functionality or draw on matplotlib (that can come later)

    def play_round(self, move):
        pass
        # check whose go it is
        # check if array is already filled by a piece in place defined by move
        # if not, save placed piece to array (1 for X, 2 for O)
        #   if it is, ask to play again and return a failure key, perhaps a bool
        # check if game has been won
        #   if not, increment the turn count

    def check_if_won(self):
        pass
        # check if the board has been won by anyone

        # possible wins include
        # horizontal along: Top, Middle, Bottom
        # vertical along Left, Middle, Bottom
        # diagonal from top left or top right corner
        return True


class Computer:

    def __init__(self):
        # does it need to do anything?
        pass

    def make_move(self):
        # this will need to learn, but for now let's make it choose randomly against the opponent
        pass
