from bke import start


start()

class TTTSlayer800 (EvaluatieAgent):
    def evaluatie(self, bord, mijn_symbool, tegenstander_symbool):
        return random.integer(1, 500)
    
TTT_Slayer_800 = TTTSlayer800()
start(speler_o=TTT_Slayer_800)
