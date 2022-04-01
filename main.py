from random import randint
def onStart():
	# board=[['1','2','3'],['4','X','6'],['7','8','9']]
	board=[['1','2','3'],['4','5','6'],['7','8','9']]
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
	sign='O'
	while True:
		
		move=int(input("Please Pick a number between 1-9"))
		if move<1 or move>9:
			print("Please Pick a number between 1-9")
			continue
		elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
			print("Sorry, that square is already taken! Please select another square!")
			continue
		elif move==1:
			board[0][0]=sign
			break
		elif move==2:
			board[0][1]=sign
			break
		elif move==3:
			board[0][2]=sign
			break
		elif move==4:
			board[1][0]=sign
			break
		elif move==5:
			board[1][1]=sign
			break
		elif move==6:
			board[1][2]=sign
			break
		elif move==7:
			board[2][0]=sign
			break
		elif move==8:
			board[2][1]=sign
			break
		elif move==9:
			board[2][2]=sign
			break
#def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
#def draw_move(board):
    # The function draws the computer's move and updates the board.
def draw_move(board):
    # The function draws the computer's move and updates the board.
	sign='X'
	while True:
		move=randint(1,9)
		if move<1 or move>9:
			print("Please Pick a number between 1-9")
			continue
		elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
			print("Sorry, that square is already taken! Please select another square!")
			continue
		elif move==1:
			board[0][0]=sign
			break
		elif move==2:
			board[0][1]=sign
			break
		elif move==3:
			board[0][2]=sign
			break
		elif move==4:
			board[1][0]=sign
			break
		elif move==5:
			board[1][1]=sign
			break
		elif move==6:
			board[1][2]=sign
			break
		elif move==7:
			board[2][0]=sign
			break
		elif move==8:
			board[2][1]=sign
			break
		elif move==9:
			board[2][2]=sign
			break

#def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

victory_message=""
def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
	if board[0][0]==sign and board[0][1]==sign and board[0][2]==sign:
		victory_message=sign+" Wins"
		return True
	elif board[1][0]==sign and board[1][1]==sign and board[1][2]==sign:
		victory_message=sign+" Wins"
		return True
	elif board[2][0]==sign and board[2][1]==sign and board[2][2]==sign:
		victory_message=sign+" Wins"
		return True
	elif board[0][0]==sign and board[1][1]==sign and board[2][2]==sign:
		victory_message=sign+" Wins"
		return True
	elif board[0][0]==sign and board[1][0]==sign and board[2][0]==sign:
		victory_message=sign+" Wins"
		return True
	elif board[0][1]==sign and board[1][1]==sign and board[2][1]==sign:
		victory_message=sign+" Wins"
		return True
	elif board[0][2]==sign and board[1][1]==sign and board[2][0]==sign:
		victory_message=sign+" Wins"
		return True
	elif board[0][2]==sign and board[1][2]==sign and board[2][2]==sign:
		victory_message=sign+" Wins"
		return True
	else:
		return False
def Game():
	# board=[['1','2','3'],['4','X','6'],['7','8','9']]
	board=[['1','2','3'],['4','5','6'],['7','8','9']]
	onStart()
	victory=False
	while victory==False:
		turn='Player'
		end=input("Want to end?")
		if end=="yes" or end=="Yes" or end=="Y" or end=="YES" or end=="y":
			break
		enter_move(board)
		display_board(board)
		if (victory_for(board, 'X')==True and victory_for(board, 'O')==True):
			victory=True
			victory_message="It's a tie"
			print(victory_message)
		elif victory_for(board, 'X')==True:
			victory=True
			victory_message="X"+" Wins"
			print(victory_message)
			break
		elif victory_for(board, 'O')==True:
			victory=True
			victory_message="O"+" Wins"
			print(victory_message)
			break
		draw_move(board)
		display_board(board)
		if victory_for(board, 'X')==True and victory_for(board, 'O')==True:
			victory=True
			victory_message="It's a tie"
			print(victory_message)
			break
		elif victory_for(board, 'X')==True:
			victory=True
			victory_message="X"+" Wins"
			print(victory_message)
			break
		elif victory_for(board, 'O')==True:
			victory=True
			victory_message="O"+" Wins"
			print(victory_message)
			break
Game()