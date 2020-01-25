from unittest import TestCase
import Dominion


class TestPlayer(TestCase):
    # prepare data, call function, make sure function worked correctly
    # def test_other(self):
    #     self.fail()
    #
    # def test_stack(self):
    #     self.fail()

    def test_draw(self):
        # make a player, set their deck to contain 1 Market, their hand to empty, and their discard to 4 coppers
        player = Dominion.Player('Annie')
        player.deck = [Dominion.Market()] * 1
        player.hand = []
        player.discard = [Dominion.Copper()] * 4

        # make sure hand is empty, draw a Market, make sure it's in the hand, make sure deck is now empty
        self.assertTrue(len(player.hand) == 0)
        self.assertTrue(player.draw().name == "Market")
        self.assertTrue(len(player.hand) > 0)
        self.assertTrue(player.hand[0].name == "Market")
        self.assertTrue(len(player.deck) == 0, "player.deck = " + str(len(player.deck)))

        # draw another card triggering a reshuffle, check that the new card is from discard, check that deck is less
        #   by 2 cards, check discard is now empty
        self.assertTrue(player.draw().name == "Copper")
        self.assertTrue(player.hand[1].name == "Copper")
        self.assertTrue(len(player.deck) == 3, "len(player.deck = " + str(len(player.deck)))
        self.assertTrue(len(player.discard) == 0, "len(player.discard = " + str(len(player.discard)))
        # self.fail()

    # def test_turn(self):
    #     self.fail()
    #
    # def test_gaincard(self):
    #     self.fail()
    #
    # def test_yesnoinput(self):
    #     self.fail()
    #
    # def test_choose_discard(self):
    #     self.fail()
    #
    # def test_show(self):
    #     self.fail()

    def test_action_balance(self):
        # make a player
        player = Dominion.Player('Annie')
        player.actions = 0
        # balance ( should be nothing)
        self.assertEqual(player.action_balance(), 0, "Balance is " + str(player.action_balance()))
        # add an action card to their stack
        player.discard = [Dominion.Village()] * 1
        # balance again should return more
        self.assertEqual(player.action_balance(), (0-1 + player.discard[0].actions)*70/len(player.stack()))
        # self.fail()

    def test_cardsummary(self):
        # make a player
        player = Dominion.Player('Annie')
        # add several cards
        player.discard = [Dominion.Village()] * 1 + [Dominion.Moat()] * 1  + [Dominion.Market()] * 1
        # test summary
        self.assertEqual(player.cardsummary(), {'Copper': 7, 'Estate': 3, 'Village': 1, 'Moat': 1, 'Market': 1, 'VICTORY POINTS': 3})
        # add duplicate cards and new cards including vpoint card
        player.discard.clear()
        player.discard = [Dominion.Village()] * 2 + [Dominion.Moat()] * 2  + [Dominion.Market()] * 2 + [Dominion.Province()] *1
        # test summary
        self.assertEqual(player.cardsummary(),{'Copper': 7, 'Estate': 3, 'Village': 2, 'Moat': 2, 'Market': 2, 'Province': 1, 'VICTORY POINTS': 9})
        # self.fail()

    def test_calcpoints(self):
        # make a player
        player = Dominion.Player('Annie')
        # add some cards
        player.discard = [Dominion.Village()] * 2 + [Dominion.Moat()] * 2  + [Dominion.Gardens()] * 0 + [Dominion.Province()] *1
        # test calcpoints
        self.assertEqual(player.calcpoints(), 3 + 6)
        # add a gardens
        player.discard.clear()
        player.discard = [Dominion.Village()] * 2 + [Dominion.Moat()] * 2  + [Dominion.Gardens()] * 2 + [Dominion.Province()] *1
        # test calcpoints
        self.assertEqual(player.calcpoints(), (3 + 6) + (17 // 10 * 2))
        # self.fail()
