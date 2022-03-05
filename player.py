import enum
import http.client
import urllib.request
import json
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

            # fold if the first bet is high
            if len(community_cards) == 0:
                if current_call_amount > 100:
                    return 0

            return get_bet_amount(hand, current_call_amount)
        except Exception as e:
            print(e, file=sys.stderr)
            return 0

    def showdown(self, game_state):
        pass


class HandRanks(enum.Enum):
    HighCard = 0
    Pair = 1
    TwoPairs = 2
    ThreeOfAKind = 3
    Straight = 4
    Flush = 5
    FullHouse = 6
    FourOfAKind = 7
    StraightFlush = 8


def get_bet_amount(hand, current_call_amount):
    hand_rank = get_rank(hand)

    raise_by = {
        HandRanks.FourOfAKind: 10000,
        HandRanks.Flush: 100,
        HandRanks.ThreeOfAKind: 10,
        HandRanks.TwoPairs: 5,
        HandRanks.Pair: 1,
    }.get(hand_rank)

    if raise_by is None:
        # fold
        return 0
    else:
        return current_call_amount + raise_by


def get_rank(cards) -> HandRanks:
    response: http.client.HTTPResponse = urllib.request.urlopen(
        "http://rainman.leanpoker.org/rank",
        ("cards=" + json.dumps(cards)).encode("utf-8"),
    )
    response_body = json.loads(response.read().decode("utf-8"))
    result = response_body["rank"]
    return HandRanks(result)
