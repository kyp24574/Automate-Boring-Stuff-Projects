# chess_dictionary_validator.py - A program to detect if a chessboard dictionary is valid.
"""A program to determine if the chessboard passed is valid."""
def is_valid_chessboard(chessboard):
    """Returns True if chessboard is valid."""
    # If players have more than 32 pieces on the board.
    if len(chessboard) > 32:
        print('More than 32 pieces on the board.')
        return False
    x_axis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    piece_color = ['w', 'b']
    # lists to keep track of white/black pieces on the board.
    # K=King Q=Queen R=Rook B=Bishop N=Knight P=Pawn
    #               K  Q  R  B  N  P
    white_pieces = [0, 0, 0, 0, 0, 0]
    black_pieces = [0, 0, 0, 0, 0, 0]

    # For loop to travel through chessboard dictionary
    for tile, piece in chessboard.items():
        # If tile number greater than 8
        if int(tile[0]) > 8:
            print('Tile number not in 1-8.')
            return False
        # If tile letter not in 'abcdefgh'
        if tile[1] not in x_axis:
            print('Tile letter not in abcdefgh.')
            return False
        # If there is no piece at that tile.
        if piece == '':
            continue
        # If piece does not start with w or b
        if piece[0] not in piece_color:
            print('Piece does not start with w or b.')
            return False
        # If piece is pawn
        if 'pawn' in piece:
            if piece[0] == 'b':
                black_pieces[5] += 1  # if piece is black
            else:
                white_pieces[5] += 1  # if piece is white
        # If piece is knight
        elif 'knight' in piece:
            if piece[0] == 'b':
                black_pieces[4] += 1  # if piece is black
            else:
                white_pieces[4] += 1  # if piece is white
        # If piece is bishop
        elif 'bishop' in piece:
            if piece[0] == 'b':
                black_pieces[3] += 1  # if piece is black
            else:
                white_pieces[3] += 1  # if piece is white
        # If piece is rook
        elif 'rook' in piece:
            if piece[0] == 'b':
                black_pieces[2] += 1  # if piece is black
            else:
                white_pieces[2] += 1  # if piece is white
        # If piece is queen
        elif 'queen' in piece:
            if piece[0] == 'b':
                black_pieces[1] += 1  # if piece is black
            else:
                white_pieces[1] += 1  # if piece is white
        # If piece is king
        elif 'king' in piece:
            if piece[0] == 'b':
                black_pieces[0] += 1  # if piece is black
            else:
                white_pieces[0] += 1  # if piece is white
        # If piece is none of the above
        else:
            print('Invalid piece name.')
            return False

    # If there are more than 16 white/black pieces on the board
    if sum(white_pieces) > 16 or sum(black_pieces) > 16:
        print('Too many player pieces on board.')
        return False
    # If there are more than 8 white/black pawns
    if white_pieces[5] > 8 or black_pieces[5] > 8:
        print('Too many pawns on board.')
        return False
    # If there are more than 1 white/black king or more than 1 white/black queen
    if white_pieces[0] > 1 or black_pieces[0] > 1 or white_pieces[1] > 1 or black_pieces[1] > 1:
        print('Too many kings/queens on board.')
        return False
    # If there are more than 2 white rooks/bishops/knights
    if white_pieces[2] > 2 or white_pieces[3] > 2 or white_pieces[4] > 2:
        print('Too many white rooks/bishops/knights on board.')
        return False
    # If there are more than 2 black rooks/bishops/knights
    if black_pieces[2] > 2 or black_pieces[3] > 2 or black_pieces[4] > 2:
        print('Too many black rooks/bishops/knights on board.')
        return False

    # Returns True if all tests above are passed.
    return True


def main():
    """Main method to test is_valid_chessboard()"""
    chessboard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '4g': ''}
    print(is_valid_chessboard(chessboard))

# If program is run (and not imported), calls main() method.
if __name__ == '__main__':
    main()
