from enum import Enum

class PieceType(Enum):
    PAWN = "P"
    KNIGHT = "N"
    BISHOP = "B"
    ROOK = "R"
    QUEEN = "Q"
    KING = "K"


class Piece:
    def __init__(self, pieceType, player):
        self.piece_type = pieceType
        self.player = player

    def __str__(self):
        return (self.piece_type.value + str(self.player))

    def __repr__(self):
        return (self.piece_type.value + str(self.player))
