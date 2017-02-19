from piece import Piece, PieceType
from player import Player
import sys
import numpy as np

class Game:
    def __init__(self):

        # initialize game state
        self.board = Board()
        print(self.board)

        # set up players
        # player_1_name = input("Enter Player one\'s name: ")
        # player_2_name = input("Enter Player two\'s name: ")
        self.player_1 = Player("Joe", 1)
        self.player_2 = Player("Bimbo", 2)
        self.current_player = self.player_1

        # keep track of moves
        self.moves = []

    # plays the game
    def play(self):

        self.print_instructions()

        # main game loop
        while True:

            # ask the current player what piece they would like to move_piece
            while True:
                fromSquare = input("Enter coordinate of the piece you would like to move: ")
                self.check_if_exit(fromSquare)
                toSquare = input("Enter coordinate of the square you'd like to move to: ")
                self.check_if_exit(toSquare)
                try:
                    self.valid_move(fromSquare, toSquare)
                    # flip row/col since chess input is opposite
                    fromSquare = [int(fromSquare[1]), fromSquare[0]]
                    toSquare = [int(toSquare[1]), toSquare[0]]
                    self.moves.append( (fromSquare, toSquare, self.current_player) )
                    break

                except ValueError:
                    print("coordinates were in wrong format, try again")
                except:
                     print("Unexpected error:", sys.exc_info()[0])


            # check if there is a winner
            # if self.winner():
            #     print("{0} is the Winner!".format(self.winner))
            #     break

            self.switch_player()

    def print_instructions(self):
        print('Welcome to Commandline chess! When prompted, please provide coordinates \n \
        in the form of [A-H][1-8], where a letter represents the column \n and the number  \
        represents the row')

    def check_if_exit(self, command):
        command = command.lower()
        exitCommands = ['quit', 'qquit', 'quitt', 'exit','end','done']
        if command in exitCommands:
            sys.exit()

    def valid_move(self, fromSquare, toSquare):

        # make sure coordiantes are exactly 2 characters long
        if len(fromSquare) != 2:
            raise Exception("From Square is not valid")

        if len(toSquare) != 2:
            raise Exception("To Square is not valid")

        # flip coordinates. If wrong format, int() will throw ValueError
        fromSquare = [int(fromSquare[1]), fromSquare[0]]
        toSquare = [int(toSquare[1]), toSquare[0]]

        # make sure the square is on the board
        self.board.check_valid_coord(fromSquare[0], fromSquare[1])
        self.board.check_valid_coord(toSquare[0], toSquare[1])



    # switch the player
    def switch_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

    def is_check_state(self):
        pass

    def move_piece(self, fromSquare, toSquare):

        # unpack coordinates
        fromRow, fromCol = fromSquare
        toRow, toCol = toSquare


class Board(object):
    def __init__(self):
        self.board = np.array([8*[None] for _ in range(8)])

        # set pieces according to standard rules
        self.set_pieces()


    def set_pieces(self):

        # set pawns
        for i in range(1,9):
            pawn_p1 = Piece(PieceType.PAWN, 1)
            pawn_p2 = Piece(PieceType.PAWN, 2)
            self.place_piece(pawn_p1, 2, self.col_to_letter(i))
            self.place_piece(pawn_p2, 7, self.col_to_letter(i))

        # set rooks
        self.place_piece(Piece(PieceType.ROOK, 1), 1, 'a')
        self.place_piece(Piece(PieceType.ROOK, 1), 1, 'h')
        self.place_piece(Piece(PieceType.ROOK, 2), 8, 'a')
        self.place_piece(Piece(PieceType.ROOK, 2), 8, 'h')

        # set knights
        self.place_piece(Piece(PieceType.KNIGHT, 1), 1, 'b')
        self.place_piece(Piece(PieceType.KNIGHT, 1), 1, 'g')
        self.place_piece(Piece(PieceType.KNIGHT, 2), 8, 'b')
        self.place_piece(Piece(PieceType.KNIGHT, 2), 8, 'g')

        # set bishops
        self.place_piece(Piece(PieceType.BISHOP, 1), 1, 'c')
        self.place_piece(Piece(PieceType.BISHOP, 1), 1, 'f')
        self.place_piece(Piece(PieceType.BISHOP, 2), 8, 'c')
        self.place_piece(Piece(PieceType.BISHOP, 2), 8, 'f')

        # set queens
        self.place_piece(Piece(PieceType.QUEEN, 1), 1, 'd')
        self.place_piece(Piece(PieceType.QUEEN, 2), 8, 'd')

        # set kings
        self.place_piece(Piece(PieceType.KING, 1), 1, 'e')
        self.place_piece(Piece(PieceType.KING, 2), 8, 'e')

    # place a piece in the selected square
    def place_piece(self, piece, row, col):

        self.check_valid_coord(row, col)

        # invert row number
        row_set = 8 - row

        # convert col to integer
        col_set = ord(col) - ord('a')

        # make sure square is empty
        # if self.board[row_set][col_set] is not None:
        #     raise Exception("{0},{1} is not empty".format(row, col))

        self.board[row_set][col_set] = piece


    def col_to_letter(self, col):
        return chr(ord('a') + col - 1)

    # check if the coordinate given is a square on the board
    def check_valid_coord(self, row, col):

        # validate row, col
        col = col.lower()
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



def main():

    # set up the game
    game = Game()

    game.play()

if __name__ == "__main__":
    main()
