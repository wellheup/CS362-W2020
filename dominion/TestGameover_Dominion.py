from unittest import TestCase
import Dominion


class Test(TestCase):

    def test_gameover(self):
        # make a supply, call game over on that supply, assert that it gave the right answer
        supply = {"Province": [Dominion.Province()] * 1,
                  "Market": [Dominion.Market()] * 1,
                  "Militia": [Dominion.Militia()] * 1,
                  "Cellar": [Dominion.Cellar()] * 1}
        self.assertFalse(Dominion.gameover(supply))

        supply["Province"].pop(0)
        self.assertTrue(Dominion.gameover(supply))

        supply["Province"].append(Dominion.Province())
        supply["Market"].pop(0)
        supply["Militia"].pop(0)
        supply["Cellar"].pop(0)
        self.assertTrue(Dominion.gameover(supply))

        #self.fail("test not implemented")
