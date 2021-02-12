import random
from bke import *


class Anakinisyourfather3000(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)

class TTTSlayer800(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        if can_win(board, opponent_symbol):
            getal = getal - 1000
        return getal
            
            
ttt_slayer_800 = TTTSlayer800()
anakin_is_your_father3000 = Anakinisyourfather3000()
start(player_o=anakin_is_your_father3000, player_x=ttt_slayer_800)
