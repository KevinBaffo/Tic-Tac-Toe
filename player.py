import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        value = None 
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-9)')
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print('Invalid square. Try again!')
        return value

class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
            value = self.minimax(game, self.letter)['score']
            # print(f' here it happened {value}')
        return square
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # check if previous move was a winner 
        if state.current_winner == other_player:
            return {'position': None, 'score':1*(state.num_empty_squares()+1) if other_player == max_player else -1*(state.num_empty_squares() + 1)}
        elif not state.num_empty_squares(): #no empty squares
            return {'position': None, 'score':0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        
        for possible_move in state.available_moves():
            # 1. Try move in a spot
            state.make_move(possible_move, player)
            # 2. recursive minimax to simulate after moves 
            sim_score = self.minimax(state, other_player)
            # 3. Undo move 
            state.board[possible_move] = ' '
            state.current_winner = None 
            sim_score['position'] = possible_move
            # 4. update dictionary 
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score    
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score            
        return best