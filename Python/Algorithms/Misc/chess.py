from dataclasses import dataclass

WHITE_PIECES = ["♜","♞","♝","♛","♚","♟"]

BLACK_PIECES = ["♖","♘","♗","♕","♔","♙"]

@dataclass
class Piece:
    ...


@dataclass
class Board:
    def __init__(self) -> None:
        self.board = [
            ["♖","♘","♗","♕","♔","♗","♘","♖"],
            ["♟","♟","♟","♟","♟","♟","♟","♟"],
            [],
            [],
            [],
            [],
            ["♙","♙","♙","♙","♙","♙","♙","♙"],
            [],
        ]
