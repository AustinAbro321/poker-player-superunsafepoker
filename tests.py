import json
import unittest

from player import Player, is_pair, is_three_of_a_kind, get_bet_amount, is_four_of_a_kind, is_flush, is_two_pair

TWO_PAIR_HAND = [
    {
        "rank": "A",
        "suit": "hearts"
    },
    {
        "rank": "A",
        "suit": "hearts"
    },
    {
        "rank": "8",
        "suit": "hearts"
    },
    {
        "rank": "8",
        "suit": "hearts"
    },
    {
        "rank": "1",
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

GARBAGE_HAND = [{
    "rank": "4",
    "suit": "spades"
},
    {
        "rank": "A",
        "suit": "hearts"
    }]


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

    def test_player(self):
        result = Player().betRequest(game_state=self.game_state)
        self.assertEqual(result, 240)

        self.game_state["round"] = 1
        result = Player().betRequest(game_state=self.game_state)
        self.assertEqual(result, 241)

    def test_check_pair(self):
        result = is_pair(TWO_OF_A_KIND_HAND)
        self.assertTrue(result)

    def test_is_not_three_of_a_kind(self):
        result = is_three_of_a_kind(TWO_OF_A_KIND_HAND)
        self.assertFalse(result)

    def test_is_three_of_a_kind(self):
        result = is_three_of_a_kind(THREE_OF_A_KIND_HAND)
        self.assertTrue(result)

    def test_check_not_pair(self):
        result = is_pair(GARBAGE_HAND)
        self.assertFalse(result)

    def test_is_four_of_a_kind(self):
        result = is_four_of_a_kind(FOUR_OF_A_KIND_HAND)
        self.assertTrue(result)

    def test_is_flush(self):
        result = is_flush(FLUSH_HAND)
        self.assertTrue(result)

    def test_is_two_pair(self):
        result = is_two_pair(TWO_PAIR_HAND)
        self.assertTrue(result)

    def test_is_two_pair_not(self):
        result = is_two_pair(TWO_OF_A_KIND_HAND)
        self.assertFalse(result)

    def test_is_two_pair_not_2(self):
        result = is_two_pair(FOUR_OF_A_KIND_HAND)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
