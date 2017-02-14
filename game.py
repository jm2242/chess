
class Game:
    def __init__(self):

        # initialize game state
        board = Board()

        self.winner = self.play()


    # plays the game
    def play(self):

        # main game loop
        while True:







class Board:
    def __init__(self):
        self.board = 8*[8*[None]]





class Player:
    def __init__(self, name):
        self.name = name

# Pawn, Rook, Knight, Bishop, Queen, King
class Piece:
