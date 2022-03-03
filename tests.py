import json
import unittest

from player import Player, is_pair, is_three_of_a_kind


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
        # game_state[payers][]
        result = Player().betRequest(game_state=self.game_state)
        self.assertEqual(result,320 - 80 + 20)

    def test_check_pair(self):
        result = is_pair(cards=[{
            "rank": "4",
            "suit": "spades"
        },
            {
                "rank": "4",
                "suit": "hearts"
            }])
        self.assertTrue(result)

    def test_is_not_three_of_a_kind(self):
        result = is_three_of_a_kind(cards=[{
            "rank": "4",
            "suit": "spades"
        },
            {
                "rank": "4",
                "suit": "hearts"
            }])
        self.assertFalse(result)

    def test_is_three_of_a_kind(self):
        result = is_three_of_a_kind(cards=[{
            "rank": "4",
            "suit": "spades"
        },
            {
                "rank": "4",
                "suit": "hearts"
            },
            {
                "rank": "4",
                "suit": "hearts"
            }
        ])
        self.assertTrue(result)

    def test_check_not_pair(self):
        result = is_pair(cards=[{
            "rank": "4",
            "suit": "spades"
        },
        {
            "rank": "A",
            "suit": "hearts"
        }])
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
