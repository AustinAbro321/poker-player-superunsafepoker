
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        current_buy_in = game_state["current_buy_in"]
        players = game_state["players"]
        in_action = game_state["in_action"]

        return current_buy_in - players[in_action]["bet"]

    def showdown(self, game_state):
        pass

