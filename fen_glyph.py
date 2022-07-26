import io
import random
from utils import chunks


def board_to_fen(board):
    # Use StringIO to build string more efficiently than concatenating
    with io.StringIO() as s:
        for row in board:
            empty = 0
            for cell in row:
                c = cell[0]
                if c in ('w', 'b'):
                    if empty > 0:
                        s.write(str(empty))
                        empty = 0
                    s.write(cell[1].upper() if c == 'w' else cell[1].lower())
                else:
                    empty += 1
            if empty > 0:
                s.write(str(empty))
            s.write('/')
        # Move one position back to overwrite last '/'
        s.seek(s.tell() - 1)
        # If you do not have the additional information choose what to put
        s.write(' b - - 0 1')
        return s.getvalue()


def random_board_for_glyph():
    empty_list = ["em"] * 64
    l = empty_list
    positions_left = list(range(64))

    specified_placements = [
        ["wk", 63], ["wr", 62], ["wp", 55], ["wp", 54],
        ["bk", 0],  ["br", 1], ["bp", 8],  ["bp", 9],
    ]

    for [piece, position] in specified_placements:
        l[position] = piece
        positions_left.remove(position)

    unrestricted_placements = [
        "wr", "br",
        "wq", "wq", "bq", "bq",
        "wb", "wb", "bb", "bb",
    ]

    for piece in unrestricted_placements:
        position = random.choice(positions_left)
        l[position] = piece
        positions_left.remove(position)

    knight_placements = [
        "wn", "bn", "wn", "bn", # place knights with restrictions
    ]

    for piece in knight_placements:
        knight_allowed_positions_left = positions_left.copy()
        disallowed_knight_positions = [10, 17, 53, 46]
        for position in disallowed_knight_positions:
            if position in knight_allowed_positions_left:
                knight_allowed_positions_left.remove(position)

        position = random.choice(knight_allowed_positions_left)
        l[position] = piece
        positions_left.remove(position)

    pawn_placements = [
        "wp", "wp", "wp", "wp", "wp", "wp",
        "bp", "bp", "bp", "bp", "bp", "bp",
    ]

    for piece in pawn_placements:
        pawn_allowed_positions_left = positions_left.copy()
        disallowed_pawn_positions = [2, 3, 4, 5, 6, 7, 56, 57, 58, 59, 60, 61]
        for position in disallowed_pawn_positions:
            if position in pawn_allowed_positions_left:
                pawn_allowed_positions_left.remove(position)

        position = random.choice(pawn_allowed_positions_left)
        l[position] = piece
        positions_left.remove(position)

    matrix = list(chunks(l, 8))

    return matrix


def random_fen_for_glyph():
    matrix = random_board_for_glyph()
    fen = board_to_fen(matrix)
    return fen


if __name__ == "__main__":
    fen = random_fen_for_glyph()
    print(fen)
