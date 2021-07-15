#   Tic Tac Toe Game 
#   By: Kevin Baffo 
#   Using: Python 
#   'The best way to predict the future is to create it.' Peter Drucker
#   Proper Peparation Prevent Poor Performance

# Function to draw game
def print_game(values):
    print("\n")
    print("\t     __________________")
    print("\t    |     |      |     |")
    print("\t    |  {}  |  {}   |  {}  |".format(values[0], values[1], values[2]))
    print("\t    |_____|______|_____|")
    print("\t    |     |      |     |")
    print("\t    |  {}  |  {}   |  {}  |".format(values[3], values[4], values[5]))
    print("\t    |_____|______|_____|")
    print("\t    |     |      |     |")
    print("\t    |  {}  |  {}   |  {}  |".format(values[6], values[7], values[8]))
    print("\t    |_____|______|_____|")
    
# Function to check if there is a winner
def check_winner(player_pos, current_player):
    #All possible winning combos 
    winners = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for x in winners:
        if all(y in player_pos[current_player] for y in x):
            return True
    return False

# Function to check for draw 
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False


#Function to start a single game
def single_game(current_player):
    values = [' ' for x in range(9)]
    player_pos = {'X':[], 'O':[]}
    while True:
        print_game(values)

        #Getting player move/box to play
        try:
            print("Player ", current_player, " turn. Choose a box: ?", end="")
            move = int(input())
        except ValueError:
            print("Wrong Input! Please try again")
            continue

        #Sanity check            
        if move not in range(1,10):
            print("Wrong Input! Please try again")
            continue

        #Check if box is free
        if values[move -1] != ' ':
            print("Box already filled, Try again!")
            continue
        
        values[move-1] = current_player #Grid update
        player_pos[current_player].append(move) #Player update
        #print_game(values)

        #Checking for winner 
        if check_winner(player_pos, current_player):
            print_game(values)
            print("Player ", current_player, " has won the game!\n")
            return current_player
        
        #Check for Draw 
        if check_draw(player_pos):
            print_game(values)
            print("Game Drawn \n")
            return 'Draw'

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

print_game(['O' for x in range(9)])