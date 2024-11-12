print("Welcome to Tic Tac Toe\n")

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

current_player = "O"
winner = None
game_running = True

def print_board(board):
    print("+---+---+---+")
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("+---+---+---+")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("+---+---+---+")
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("+---+---+---+")

def main(board):
    print_board(board)
    check_player()
    while True:
        row = int(input("Pick a row (1, 2, 3): "))
        column = int(input("Pick a column (1, 2, 3): "))
        if 1 <= row <= 3 and 1 <= column <= 3 and board[row-1][column-1] == " ":
            board[row-1][column-1] = current_player
            break
        else:
            print(f"Invalid position!\n")
            
    print()
    check_win()
    check_tie()
    
def check_horizontal(board):
    global winner
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != " ":
        winner = board[0][0]
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != " ":
        winner = board[1][0]
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != " ":
        winner = board[2][0]
        return True
    
def check_vertical(board):
    global winner
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != " ":
        winner = board[0][0]
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != " ":
        winner = board[0][1]
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != " ":
        winner = board[0][2]
        return True
    
def check_diagonal(board):
    global winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        winner = board[0][0]
        return True
    
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        winner = board[0][2]
        return True
    
def check_tie():
    global game_running
    new_board = []
    for row in board:
        for item in row:
            new_board.append(item)
        
    if " " not in new_board:
        print_board(board)
        print("\nIt's a tie!\n\nGame over!")
        game_running = False

def check_win():
    global game_running
    if check_diagonal(board) or check_horizontal(board) or check_vertical(board):
        print_board(board)
        print(f"\n{winner} wins!\n\nGame over!")
        game_running = False
        
def check_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    print(f"\n{current_player}'s turn")
    
if __name__ == "__main__":
    while game_running:
        main(board)
