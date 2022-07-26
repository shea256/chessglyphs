import os
import argparse
from fen_glyph import random_fen_for_glyph
from chess_board import ChessBoard
from draw_board import DrawBoard


parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="fmt", metavar="format", default="png", help="")
parser.add_argument("-o", dest="filename", metavar="output file", default="result", help="")
parser.add_argument("-dir", dest="folder", metavar="output folder", default="output", help="")


def main():
    args = parser.parse_args()
    fen = random_fen_for_glyph()
    fen = ChessBoard(fen.split(" "))

    if not fen.isvalid:
        print("Invalid FEN. No Image file was generated.")

    if not os.path.isdir(args.folder):
        os.mkdir(args.folder)

    boardGrid = fen.board
    boardImg = DrawBoard(boardGrid, args.fmt, args.folder, args.filename)
    boardImg.create()
    boardImg.to_image()
    print("Completed! File created in {}/{}.{}".format(args.folder, args.filename, args.fmt))

if __name__ == "__main__":
    main()
    os.system("open output/result.png")