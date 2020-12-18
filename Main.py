import random
from bke import *


class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)

class TTTSlayer800(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        if can_win(board, opponent_symbol):
            getal = getal - 1000
        return getal
            
            
ttt_slayer_800 = TTTSlayer800()
my_random_agent = MyRandomAgent()
start(player_o=my_random_agent, player_x=ttt_slayer_800)
