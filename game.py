# TIC TAC TOE GAME

# Board variables
BOARD_WIDTH = 3
BOARD_HEIGHT = 3

# Variables
current_player = 0
is_running = True

# Function that creates a new empty 3 x 3 board
def new_board():
    board = []
    # Loop that makes the board filling each tile with None Type
    for row in range(0, BOARD_WIDTH):
        columns = []
        for column in range(0, BOARD_HEIGHT):
            columns.append(None)
        board.append(columns)
    return(board)

# Renders the board and prints out each tile respective to its current state
def render_board(board):
    print("  0 1 2")

    row_num = 0
    rows = []
    # Makes a new array holding each individual row
    for y in range(0, BOARD_HEIGHT):
        row = []
        for x in range(0, BOARD_WIDTH):
            row.append(board[x][y])
        rows.append(row)

    # Printing out each row, filling in all none type objects with spaces
    for row in rows:
        output_tile = ''
        for tile in row:
            if tile is None:
                output_tile += ' '
            else:
                output_tile += tile
        # Prints out rows and columns including numbering
        print("%d|%s|" % (row_num, ' '.join(output_tile)))
        row_num += 1
    print("--------")

#def win_test():
#    #TO-DO: test for all possibilities of wins
#    # output winner and stop running game
#
#def full_board():
#    # TO-DO: check for full board and act accordingly

# Main loop
def main():
    board = new_board()
    board[0][1] = "X"
    board[1][2] = "O"
    render_board(board)
    # get_turns()
    # win_test()

if __name__ == "__main__":
    main()

