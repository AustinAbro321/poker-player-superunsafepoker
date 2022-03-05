import json
import unittest

import player

TWO_PAIR_HAND = [
    {
        "rank": "A",
        "suit": "hearts"
    },
    {
        "rank": "A",
        "suit": "spades"
    },
    {
        "rank": "8",
        "suit": "hearts"
    },
    {
        "rank": "8",
        "suit": "spades"
    },
    {
        "rank": "3",
        "suit": "hearts"
    }]

FLUSH_HAND = [{
    "rank": "A",
    "suit": "hearts"
},
    {
        "rank": "9",
        "suit": "hearts"
    },
    {
        "rank": "7",
        "suit": "hearts"
    },
    {
        "rank": "2",
        "suit": "hearts"
    },
    {
        "rank": "1",
        "suit": "hearts"
    }]

FOUR_OF_A_KIND_HAND = [{
    "rank": "A",
    "suit": "spades"
},
    {
        "rank": "A",
        "suit": "hearts"
    },
    {
        "rank": "A",
        "suit": "hearts"
    },
    {
        "rank": "A",
        "suit": "hearts"
    }]

THREE_OF_A_KIND_HAND = [{
    "rank": "A",
    "suit": "spades"
},
    {
        "rank": "A",
        "suit": "hearts"
    },
    {
        "rank": "A",
        "suit": "hearts"
    }]

TWO_OF_A_KIND_HAND = [{
    "rank": "4",
    "suit": "spades"
},
    {
        "rank": "4",
        "suit": "hearts"
    }]

GARBAGE_HAND = [
    {"rank": "K", "suit": "hearts"},
    {"rank": "J", "suit": "hearts"},
    {"rank": "8", "suit": "clubs"},
    {"rank": "7", "suit": "diamonds"},
    {"rank": "4", "suit": "spades"},
]


class Tests(unittest.TestCase):
    game_state = json.loads('''
            {
      "tournament_id": "550d1d68cd7bd10003000003",
      "game_id": "550da1cb2d909006e90004b1",
      "round": 0,
      "bet_index": 0,
      "small_blind": 10,
      "current_buy_in": 320,
      "pot": 400,
      "minimum_raise": 240,
      "dealer": 1,
      "orbits": 7,
      "in_action": 1,
      "players": [
        {
          "id": 0,
          "name": "Albert",
          "status": "active",
          "version": "Default random player",
          "stack": 1010,
          "bet": 320
        },
        {
          "id": 1,
          "name": "Bob",
          "status": "active",
          "version": "Default random player",
          "stack": 1590,
          "bet": 80,
          "hole_cards": [
            {
              "rank": "6",
              "suit": "hearts"
            },
            {
              "rank": "K",
              "suit": "spades"
            }
          ]
        },
        {
          "id": 2,
          "name": "Chuck",
          "status": "out",
          "version": "Default random player",
          "stack": 0,
          "bet": 0
        }
      ],
      "community_cards": [
        {
          "rank": "4",
          "suit": "spades"
        },
        {
          "rank": "A",
          "suit": "hearts"
        },
        {
          "rank": "6",
          "suit": "clubs"
        }
      ]
    }
      ''')

    def test__bet_request__first_round_should_check(self):
        result = player.Player().betRequest(game_state=self.game_state)
        self.assertEqual(240, result)


    def test__bet_request__second_round_should_raise(self):
        self.game_state["round"] = 1
        result = player.Player().betRequest(game_state=self.game_state)
        self.assertEqual(241, result)

    def test_ranking(self):
        self.assertEqual(player.HandRanks.HighCard, player.get_rank(GARBAGE_HAND))
        self.assertEqual(player.HandRanks.TwoPairs, player.get_rank(TWO_PAIR_HAND))


if __name__ == "__main__":
    unittest.main()
