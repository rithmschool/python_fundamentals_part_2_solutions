from random import shuffle

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return "{} of {}".format(self.value, self.suit)

class Deck:
	def __init__(self):
		suits = ['Hearts','Diamonds','Clubs','Spades'] 
		values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
		self.cards = [Card(suit, value) for suit in suits for value in values]

	def __repr__(self):
		return "Cards remaining in deck: {}".format(len(self.cards))

	def shuffle(self):
		if len(self.cards) < 52:
			raise ValueError("Only full decks can be shuffled")
		shuffle(self.cards)
		return self

	def deal(self):
		if len(self.cards) == 0:
			raise ValueError("All cards have been dealt")
		return self.cards.pop()