# basic.py
# Version:	 0.1
# Developed by:	 DrkRabbit
# Date:		 05/29/2016
# Description:	
# 	'basic.py' will server as the main game engine for the ultimate card counting educational system
#	meant to teach players how to beat the odds by actually playing as opposed to referencing cheat
#	sheets and books.  'basic.py' will provide the core shuffling, dealing, and game mechanics for 
#	Blackjack.
# Core Functions:
#	+ Shuffle (Shuffle the deck arrays, 1 - 6 decks)
#	+ Cut (Cut the deck)
#	+ Deal (Deal cards to the players)
#	+ Compare (If the dealer doesn't bust, compare non-busted player hands to the dealers and determine win)
#	+ Logging (Log the plays in a CSV for analysis)

#Begin Import Chunks
import time
import random #used to randomize arrays

def createDeck(deckNumber):
	masterDeck = []
	
	print ('Creating a ' + str(deckNumber) + ' deck stack')
	for i in range(deckNumber):
		for j in range(9):
			for k in range(4):
				cardValue = j + 2
				masterDeck.append(cardValue)
		masterDeck.append('J')
		masterDeck.append('J')
		masterDeck.append('J')
		masterDeck.append('J')
		masterDeck.append('Q')
		masterDeck.append('Q')
		masterDeck.append('Q')
		masterDeck.append('Q')
		masterDeck.append('K')
		masterDeck.append('K')
		masterDeck.append('K')
		masterDeck.append('K')
		masterDeck.append('A')
		masterDeck.append('A')
		masterDeck.append('A')
		masterDeck.append('A')
	return masterDeck;	

def createSpace (lineNumbers):
	for i in range (lineNumbers):
		print ('')
	return;
	
def shuffleDeck (masterDeck):
	random.shuffle(masterDeck)
	return;

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~ -{---------- BlackJack for Blood ----------}- ~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print (' () ()')
print (' (^_^) - I Win!')
print ('c(u u)')
print ('Starting the BlackJack Simulator at ' + time.strftime("%H:%M:%S"))

createSpace(2)
	
newDeck = createDeck(1)

print('Added ' + str(len(newDeck)) + ' cards to the deck!')

print ('Shuffling the deck!')

shuffleDeck(newDeck)

for i in range(len(newDeck)):
	print (newDeck[i])

