import sys


class Player:
    VERSION = "UNSAFe v2"

    def betRequest(self, game_state):
        current_buy_in = game_state.get("current_buy_in", 100)
        players = game_state["players"]
        in_action = game_state["in_action"]
        hole_cards = players[in_action]["hole_cards"]
        community_cards = game_state["community_cards"] or []
        bet_adjustment = 10 if is_pair(hole_cards + community_cards) else 0
        return current_buy_in - players[in_action]["bet"] + bet_adjustment

    def showdown(self, game_state):
        pass


def is_pair(cards):
    ranks = [c["rank"] for c in cards]
    print(ranks)
    count = 0
    return any(ranks.count(element) > 1 for element in ranks)