class Table:
    def __init__(self):
        pass
    def whoTakesTrick(self, playedCards, suitOfLeadCard):
        """Return index (0,1,2,3) of the player who wins
        the tick. playedCards is a list of the cards that
        have been played for thes trick. The card that player 1
        played is in playedCards[1]. i = 0...3. The suit 
        that was lead is in suitOfLeadCard. 
        Precondition: no duplicate cards."""
        return -1