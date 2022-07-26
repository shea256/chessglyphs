from PIL import Image


RESOURCES = "resources/"
BOARD_DIMENSIONS = 320
BOARD_SIZE = (BOARD_DIMENSIONS, BOARD_DIMENSIONS)
SQUARE_SIZE = 40
PIECE_SIZE = (SQUARE_SIZE, SQUARE_SIZE)


class DrawBoard:
    def __init__(self, board, fmt, dest, fname):
        self.result = Image.open(RESOURCES + "board.png").resize(BOARD_SIZE)
        self.board = board
        self.fmt = fmt
        self.fname = fname
        self.dest = dest

    def open_image(self, piece):
        try:
            im = Image.open(RESOURCES + "{}.png".format(piece))
            return im.resize(PIECE_SIZE)
        except:
            print(piece + ".png", "does not exist.")
            return None

    def insert(self, piece, square):  # square is tuple (r,c)
        R = square[0] * SQUARE_SIZE
        C = square[1] * SQUARE_SIZE
        self.result.paste(piece, (R, C), piece)

    def create(self):  # Fix orientation of board
        for i in range(8):
            for j in range(8):
                if self.board[i][j]:
                    piece = self.open_image(self.board[i][j])
                    self.insert(piece, (i, j))

    def to_image(self):
        self.result.save("{}/{}.{}".format(self.dest, self.fname, self.fmt))