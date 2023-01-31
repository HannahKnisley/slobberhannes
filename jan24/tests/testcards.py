from unittest import TestCase
from Cards import Card, Suit,ACE,KING,QUEEN,JACK
from GameTable import Table 

class CardTester(TestCase):
    def testcard1(self):
        c = Card(2,Suit.SPADES)
        c = Card(ACE, Suit.DIAMOND)  
    def testcard2(self):
        self.assertRaises( Exception, Card, 1000, Suit.SPADES)
        self.assertRaises( Exception, Card, -2, Suit.HEARTS)
        self.assertRaises( Exception, Card, 8, "hearts")

    def testtake1(self):
        T = Table()
        #check for error on list of cards not having 4 entries
        self.assertRaises( Exception,
            T.whoTakesTrick,
            [Card(9,Suit.SPADES)],
            Suit.SPADES 
        )
        self.assertRaises( Exception,
            T.whoTakesTrick,
            [Card(9,Suit.SPADES), Card(10,Suit.HEARTS)],
            Suit.SPADES 
        )
        self.assertRaises( Exception,
            T.whoTakesTrick,
            [Card(9,Suit.SPADES), Card(10,Suit.HEARTS),
             Card(QUEEN,Suit.HEARTS), Card(KING, Suit.DIAMONDS),
             Card(ACE, Suit.SPADES)],
            Suit.SPADES 
        )

    def testtake2(self):
        T = Table()
        self.assertEquals(
            T.whoTakesTrick(
                [
                    Card(9,Suit.HEARTS),
                    Card(10, Suit.HEARTS),
                    Card(JACK, Suit.HEARTS),
                    Card(QUEEN, Suit.HEARTS)
                ],
                Suit.HEARTS
            ),
            3
        )

    def testtake3(self):
        T = Table()
        self.assertEquals(
            T.whoTakesTrick(
                [
                    Card(9,Suit.HEARTS),
                    Card(QUEEN, Suit.HEARTS),
                    Card(10, Suit.HEARTS),
                    Card(JACK, Suit.HEARTS)
                ],
                Suit.HEARTS
            ),
            1
        )
    def testtake4(self):
        T = Table()
        self.assertEquals(
            T.whoTakesTrick(
                [
                    Card(9,Suit.HEARTS),
                    Card(QUEEN, Suit.SPADES),
                    Card(JACK, Suit.HEARTS),
                    Card(10, Suit.HEARTS)
                ],
                Suit.HEARTS
            ),
            2
        )

    def testtake5(self):
        T = Table()
        self.assertEquals(
            T.whoTakesTrick(
                [
                    Card(JACK, Suit.HEARTS),
                    Card(9,Suit.HEARTS),
                    Card(QUEEN, Suit.SPADES),
                    Card(10, Suit.HEARTS)
                ],
                Suit.HEARTS
            ),
            0
        )


    def testtake6(self):
        T = Table()
        self.assertEquals(
            T.whoTakesTrick(
                [
                    Card(9,Suit.HEARTS),
                    Card(JACK, Suit.HEARTS),
                    Card(QUEEN, Suit.SPADES),
                    Card(10, Suit.CLUBS)
                ],
                Suit.HEARTS
            ),
            1
        )


    def testtake7(self):
        T = Table()
        self.assertEquals(
            T.whoTakesTrick(
                [
                    Card(9,Suit.HEARTS),
                    Card(9, Suit.CLUBS),
                    Card(QUEEN, Suit.SPADES),
                    Card(10, Suit.CLUBS)
                ],
                Suit.HEARTS
            ),
            0
        )

    def testtake8(self):
        T = Table()
        self.assertEquals(
            T.whoTakesTrick(
                [
                    Card(9, Suit.CLUBS),
                    Card(QUEEN, Suit.SPADES),
                    Card(9,Suit.HEARTS),
                    Card(10, Suit.CLUBS)
                ],
                Suit.HEARTS
            ),
            2
        )


    def testtake9(self):
        T = Table()
        self.assertRaises(
            Exception,
            T.whoTakesTrick,
            [
                Card(9, Suit.CLUBS),
                Card(QUEEN, Suit.SPADES),
                Card(9,Suit.HEARTS),
                Card(10, Suit.CLUBS)
            ],
            Suit.DIAMONDS
        )

