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
            hand = hole_cards + community_cards
            current_call_amount = current_buy_in - players[in_action]["bet"]
            curr_round = game_state["round"]
            if curr_round == 0:
                return current_call_amount
            return get_bet_amount(hand, current_call_amount)
        except Exception as e:
            print(e, file=sys.stderr)
            return 0

    def showdown(self, game_state):
        pass


def get_bet_amount(hand, current_call_amount):
    result = current_call_amount
    if is_four_of_a_kind(hand):
        result += 10000
    elif is_flush(hand):
        result += 100
    elif is_three_of_a_kind(hand):
        result += 10
    elif is_two_pair(hand):
        result += 5
    elif is_pair(hand):
        result += 1
    else:
        result = 0
    return result

def is_pair(cards):
    ranks = [c["rank"] for c in cards]
    return any(ranks.count(element) > 1 for element in ranks)

def is_three_of_a_kind(cards):
    ranks = [c["rank"] for c in cards]
    return any(ranks.count(element) > 2 for element in ranks)

def is_two_pair(cards):
    ranks = [c["rank"] for c in cards]
    set_of_ranks = list(set(ranks))
    counts = { i : 0 for i in set(set_of_ranks) }
    for r in set_of_ranks:
        counts[r] = ranks.count(r)
    return list(counts.values()).count(2) == 2



def is_four_of_a_kind(cards):
    ranks = [c["rank"] for c in cards]
    return any(ranks.count(element) > 3 for element in ranks)

def is_flush(cards):
    ranks = [c["suit"] for c in cards]
    return any(ranks.count(element) >= 5 for element in ranks)