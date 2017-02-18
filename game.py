from piece import Piece, PieceType
import numpy as np

class Game:
    def __init__(self):

        # initialize game state
        self.board = Board()
        print(self.board)

    # plays the game
    def play(self):

        # main game loop
        while True:

            # check if there is a winner
            if self.winner():
                print("{0} is the Winner!".format(self.winner))
                break
        return

class Board:
    def __init__(self):
        self.board = np.array([8*[None] for _ in range(8)])

        # set pieces according to standard rules
        self.set_pieces()


    def set_pieces(self):

        # set pawns
        for i in range(1,9):
            pawn = Piece(PieceType.PAWN, 1)
            self.place_piece(pawn, 7, self.col_to_letter(i))

    # place a piece in the selected square
    def place_piece(self, piece, row, col):

        self.check_valid_coord(row, col)

        # invert row number
        row_set = 8 - row

        # convert col to integer
        col_set = ord(col) - ord('a')

        # make sure square is empty
        if self.board[row_set][col_set] is not None:
            raise Exception("{0},{1} is not empty".format(row, col))

        self.board[row_set][col_set] = piece


    def col_to_letter(self, col):
        return chr(ord('a') + col - 1)

    def check_valid_coord(self, row, col):
        # validate row, col
        col.lower()
        rowInvalid = (row < 1 or row > 8)
        colInvalid = (col < 'a' or col > 'h')
        if rowInvalid or colInvalid:
            raise Exception("invalid row/col combination")


    def __repr__(self):
        chessBoard = []
        for row in self.board:
            rowAsList = ['  ' + piece.__str__() + ' ' if piece is not None else '  *  ' for piece in row]
            chessBoard.append(''.join(rowAsList) + '\n')
        return str(''.join(chessBoard))

    def __str__(self):
        chessBoard = []
        for idr, row in enumerate(self.board):
            rowAsList = [str(8 - idr) + '|' ] + ['  ' + piece.__str__() + ' ' if piece is not None else '  *  ' for piece in row]
            chessBoard.append(''.join(rowAsList) + '\n')
        chessBoard.append(''.join([' ' + '   a ' + '   b ' + '   c ' + '   d ' + '   e '+ '   f ' + '   g '+ '   h ']))
        return str(''.join(chessBoard))



class Player:
    def __init__(self, name):
        self.name = name


def main():
    game = Game()
    #game.play()

if __name__ == "__main__":
    main()
