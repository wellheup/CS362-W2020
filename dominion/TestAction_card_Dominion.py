from unittest import TestCase
import Dominion

class TestAction_card(TestCase):
    def test___init__(self):
        card = Dominion.Market()
        # name, cost, actions, cards, buys, coins |"Market", 5, 1, 1, 1, 1
        self.assertEqual(card.name, "Market")
        self.assertEqual(card.cost, 5)
        self.assertEqual(card.actions, 1)
        self.assertEqual(card.cards, 1)
        self.assertEqual(card.buys, 1)
        self.assertEqual(card.coins, 1)
        #self.fail()

    def test_use(self):
        player = Dominion.Player('Annie')
        player.hand = [Dominion.Market()] * 1
        trash = []

        player.hand[0].use(player, trash)
        self.assertEqual(len(player.hand), 0)
        self.assertEqual(len(player.played), 1)
        # self.fail("test not written")

    def test_augment(self):
        player = Dominion.Player('Annie')
        player.hand = [Dominion.Market()] * 1
        player.actions = 0
        player.buys = 1
        player.purse = 0
        player.hand[0].augment(player)
        self.assertEqual(player.actions, 1, player.actions)
        self.assertTrue(player.buys==2)
        self.assertTrue(player.purse==1)
        self.assertEqual(len(player.hand), 2)
        # self.fail("test not written")
