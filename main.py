from random import randint
board=[['1','2','3'],['4','X','6'],['7','8','9']]
def onStart():
    display_board(board)
def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[0][0]+"   |   "+board[0][1]+"   |   "+board[0][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[1][0]+"   |   "+board[1][1]+"   |   "+board[1][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[2][0]+"   |   "+board[2][1]+"   |   "+board[2][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
	while True:
		move=int(input("Please Pick a number between 1-9"))
		if move<1 or move>9:
			print("Please Pick a number between 1-9")
			continue
		elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
			print("Sorry, that square is already taken! Please select another square!")
			continue
		elif move==1:
			board[0][0]='0'
			break
		elif move==2:
			board[0][1]='0'
			break
		elif move==3:
			board[0][2]='0'
			break
		elif move==4:
			board[1][0]='0'
			break
		elif move==5:
			board[1][1]='0'
			break
		elif move==6:
			board[1][2]='0'
			break
		elif move==7:
			board[2][0]='0'
			break
		elif move==8:
			board[2][1]='0'
			break
		elif move==9:
			board[2][2]='0'
			break
#def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
#def draw_move(board):
    # The function draws the computer's move and updates the board.
onStart()
def Game():
		enter_move(board)
		display_board(board)
		#draw_move(board)
		# display_board(board)
Game()