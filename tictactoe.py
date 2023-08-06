
board = [[0,0,0],[0,0,0],[0,0,0]]
circle_turn = True
col_dict = {"left":0, "middle":1, "right":2}
row_dict = {"top":0, "middle":1, "bottom":2}

def game_won(board):
    for i in range(3):
        if sum(board[i]) == -3:
            return -1
        elif sum(board[i]) == 3:
            return 1
        
        col_sum = 0
        for j in range(3):
            col_sum += board[j][i]
        if col_sum == -3:
            return -1
        elif col_sum == 3:
            return 1
        
    if board[0][0]+board[1][1]+board[2][2] == 3:
        return 1
    elif board[0][0]+board[1][1]+board[2][2] == -3:
        return -1
    elif board[0][2]+board[2][0]+board[1][1] == 3:
        return 1
    elif board[0][2]+board[2][0]+board[1][1] == -3:
        return -1

    return 0

def is_drawn(board):
    for row in board:
        if 0 in row:
            return False
    
    return True

def print_board(board):
    
    print ("-"*13)
    for row in board:
        print (("|"+" "*3)*3+"|")
        for cell in row:
            thing = " "
            if cell == -1:
                thing = "X"
            elif cell == 1:
                thing = "O"
                
            print ("| "+ thing, end = " ")
        print("|")
        print (("|"+" "*3)*3+"|")
        print("-"*13)

        


print_board(board)


# game loop
while game_won(board) == 0 and not is_drawn(board):
    if circle_turn:
        row = input("enter the row you wish to place the circle in (top, middle, or bottom):")
        if row not in row_dict:
            row = input("(Circle turn) enter the row again. Make sure you enter (top/middle/bottom) exactly.")
        col = input("enter the column you wish to place the circle in (left, middle, or right):")
        if col not in col_dict:
            col = input("(Circle turn) enter the column again. Make sure you enter (left/middle/right) exactly.")
        
                
    else:
        row = input("enter the row you wish to place the cross in (top, middle, or bottom):")
        if row not in row_dict:
            row = input("(Cross turn) enter the row again. Make sure you enter (top/middle/bottom) exactly.")
        col = input("enter the column you wish to place the cross in (left, middle, or right):")
        if col not in col_dict:
            col = input("(Cross turn) enter the column again. Make sure you enter (left/middle/right) exactly.")
        
    current_cell = board[row_dict[row]][col_dict[col]]
    if current_cell == 0:
        if circle_turn:
            board[row_dict[row]][col_dict[col]] = 1
        else:
            board[row_dict[row]][col_dict[col]] = -1
        print_board(board)
        circle_turn = 1-circle_turn
    else:
        print_board(board)
        print("invalid circle placement. The square you entered is occupied already.")

if is_drawn(board):
    print("It's a draw! Please restart the program to play again.")
elif game_won(board) == 1:
    print("Circles have won! Please restart the program to play again.")
else:
    print("Crosses have won! Please restart the program to play again.")
        



