import sys


class Player:
    VERSION = "UNSAFe v1"

    def betRequest(self, game_state):
        print("---------------------everything is OK-----------------", game_state, file=sys.stderr)
        try:
            current_buy_in = game_state.get("current_buy_in", 100)
            players = game_state["players"]
            in_action = game_state["in_action"]
            return current_buy_in - players[in_action]["bet"]
        except:
            print("************************exception**********", game_state,  file=sys.stderr)
            return 0

    def showdown(self, game_state):
        pass
