import sys


class Player:
    VERSION = "UNSAFe v2"

    def betRequest(self, game_state):
        try:
            current_buy_in = game_state.get("current_buy_in", 100)
            players = game_state["players"]
            in_action = game_state["in_action"]
            hole_cards = players[in_action]["hole_cards"]
            community_cards = game_state["community_cards"] or []
            big_blind = game_state["small_blind"] * 2
            hand = hole_cards + community_cards
            if is_three_of_a_kind(hand):
                bet_adjustment = big_blind * 2
            elif is_pair(hand):
                bet_adjustment = big_blind
            else:
                bet_adjustment = 0
            return current_buy_in - players[in_action]["bet"] + bet_adjustment
        except Exception as e:
            print(e, file=sys.stderr)
            return 0

    def showdown(self, game_state):
        pass


def is_pair(cards):
    ranks = [c["rank"] for c in cards]
    print(ranks)
    count = 0
    return any(ranks.count(element) > 1 for element in ranks)

def is_three_of_a_kind(cards):
    ranks = [c["rank"] for c in cards]
    print(ranks)
    count = 0
    return any(ranks.count(element) > 2 for element in ranks)