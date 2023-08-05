#this is my favourite board game that i used to play a lot as a kid, i figured i should code it so i can play it anywhere without a physical set (there are existing online versions but mine's clearly better, cuz i made it myself from scratch)

import sys #for quitting the game when finished

board = []
def make_board(): #7 columns,  6 rows
    for b in range (6):
        row = ["_" for b in range(7)] #create the same row from scratch every time to avoid all rows being affected when one changes
        board.append(row)

def print_board(board_name):
    #board itself
    string = ""
    for i in range(6):
        for j in range(7):
            string = string + board_name[i][j] + " "
        string = string + "\n"

    #column numbers for users to reference
    numbers = ""
    for n in range(1,8):
        numbers += str(n)+" "
        
    print(numbers)
    print(string)

def player_turn(player_name):
    print("Enter the column number you'd like to play")
    
    while True: #input loop
        while True: #validation loop
            user = input(f"Player {player_name}: ")
            if validate_input(user):
                break
            else:
                print("Please enter a valid number")
    
        if not is_column_full(board, user):
            break

    coords = update_board(board, user, player_name)
    print_board(board)
    iswon = check_if_won(board, player_name, coords)
    if iswon:
        print(iswon)
        sys.exit()

def validate_input(input_value):
    if input_value.isdigit() == False:
        return False
    elif int(input_value) < 1 or int(input_value) > 7:
        return False
    else:
        return True

def is_column_full(board_name, column):
    if board_name[0][int(column)-1] == "_":
        return False
    else:
        if is_board_full(board_name): #if a column is full, they may all be full, check
            print("The board is full, it's a draw!")
            sys.exit()
        else: 
            print("This column is full, choose another column")
            return True
    
def is_board_full(board_name):
    for row in range(6):
        for column in range(7):
            if board_name[row][column] == "_":
                return False
    return True

def update_board(board_name, column, user):
    coordinates = [int(column),0]
    i = 0
    while True:
        if board_name[5-i][int(column)-1] == "_":
            if user == "A":
                board_name[5-i][int(column)-1] = "O"
            else:
                board_name[5-i][int(column)-1] = "X"
            coordinates[1] = 6-i
            break
        i += 1
    return coordinates

def check_if_won(board_name, user, coordinates):

    #coordinates: most recently placed item
    #start counter to count how many tokens are in a row and reset with every direction
    #start at the farthest end of row/column/diagonal that crosses coords and work up checking if token is in row or not

    row = coordinates[1] - 1
    column = coordinates[0] - 1
    
    if user == "A":
        token = "O"
    else:
        token = "X"

    #horizontal 
    counter = 0
    for i in range(6):
        if board_name[i][column] == token:
            counter += 1
            if counter == 4:
                return f"Player {user} won!"
        else:
            counter = 0
         
    #vertical
    counter = 0
    for j in range(7):
        if board_name[row][j] == token:
            counter += 1
            if counter == 4:
                return f"Player {user} won!" 
        else:
            counter = 0
     
    #diagonal1
    i = column
    j = row
    counter = 0

    #find grid edge along the diagonal
    while i-1 >= 0 and j-1 >= 0:
        i -= 1
        j -= 1

    #traverse from there with counter
    end = False
    while end == False:
        if board_name[j][i] == token:
            counter += 1
            if counter == 4:
                return f"Player {user} won!" 
        else:
            counter = 0
        if i + 1 < 7 and j + 1 < 6:
            i += 1
            j += 1
        else:
            end = True    

    #diagonal2
    i = row
    j = column
    counter = 0

    #find grid edge along the diagonal
    while i+1 <= 6 and j-1 >= 0:
        i += 1
        j -= 1

    #traverse from there with counter
    end = False
    while end == False:
        if board_name[j][i] == token:
            counter += 1
            if counter == 4:
                return f"Player {user} won!" 
        else:
            counter = 0
        if i - 1 >= 0 and j + 1 < 6:
            i -= 1
            j += 1
        else:
            end = True
            return False


make_board()
print_board(board)

#game loop
while True:
    player_turn("A")
    player_turn("B")
        