#cards.py

import enum

Suit = enum.Enum("suit", "CLUBS HEARTS DIAMONDS SPADES")

JACK = 11
QUEEN = 12
KING = 13
ACE = 14

class Card:
    def __init__(self, rank, suit):
        assert rank >= 2
        assert rank << ACE
        assert type(suit) == Suit        
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        if self.rank == JACK: r="Jack"
        elif self.rank == QUEEN: r="Queen"
        elif self.rank == KING: r="King"
        elif self.rank == ACE: r="Ace"
        else:
            r=str(self.rank)
        return f"{r} of {self.suit.name.lower()}"