# -*- coding: utf-8 -*-
"""
Edited on Thu Jan 16 11:16 2020

@author: Phillip Wellheuser
"""

import Dominion
import random
from collections import defaultdict
import testUtility

# Get player names
player_names = ["Annie", "*Ben", "*Carla"]

# number of curses and victory cards
if len(player_names) > 2:
    nV = 12
else:
    nV = 8
nC = -10 + 10 * len(player_names)

# Define box
box = testUtility.GetBoxes(nV)

supply_order = testUtility.GetSupplyOrder()

# Pick 10 cards from box to be in the supply
supply = testUtility.GetSupplyCards(box)

# The supply always has these cards
supply = testUtility.AddDefaultSupplyCards(supply, nV, nC)

# [BUG TEST] reducing victory points Estate, Duchy, and Province to 0
for pile in supply:
    if pile == "Estate" or pile == "Duchy" or pile == "Province":
        for card in supply[pile]:
            card.vpoints=0
# [END TEST]

# initialize the trash
trash = []

# Construct the Player objects
players = testUtility.InitPlayers()

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)
