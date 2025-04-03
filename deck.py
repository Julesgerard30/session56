import random
class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]
    # SUITS = ["clubs", "diamonds", "hearts", "spades"]
    def __init__(self, rank, suit):
        """
                Creates a card with the given rank and suit.
                :param rank: a string from Card.RANKS
                :param suit: a string from Card.SUITS
                :raises ValueError: if rank or suit are invalid
                """
        if rank not in self.RANKS:
            raise ValueError("invalid rank")
        if suit not in self.SUITS:
            raise ValueError("invalid suit")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """
                Returns the rank of the card.
                :return: string rank
                """
        return self._rank

    @property
    def suit(self):
        """
                Returns the suit of the card.
                :return: string suit
                """
        return self._suit

    def __str__(self):
        """
               Converts the card to string format.
               :return: string like 'A♣'
               """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
                Returns the official string representation of the card.
                Same as __str__ in this case.
                :return: string representation
                """
        return self.__str__() # repr is the same as str

    def __eq__(self, other):
        """
                Checks equality between two cards by comparing their rank.
                :param other: another Card object
                :return: True if ranks are equal, False otherwise
                """
        return self.rank == other.rank

    def __lt__(self, other):
        """
              Checks if this card is less than another based on rank order.
              :param other: another Card object
              :return: True if this card's rank is lower, False otherwise
              """
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)

class Deck:
    """
       Class representing a standard 52-card deck.
       """
    def __init__(self):
        """
               Constructs a full deck of 52 cards (all ranks and suits).
               """
        _cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                _cards.append(Card(rank, suit))
        self._cards = _cards

    @property
    def cards(self):
        """
                Returns the list of cards currently in the deck.
                :return: list of Card objects
                """
        return self._cards

    def __str__(self):
        """
                Converts the deck to a string for printing.
                :return: string representation of the deck
                """
        return str(self._cards)

    def shuffle(self):
        """
                Shuffles the cards in the deck in place.
                :return: None
                """
        random.shuffle(self.cards)

    def deal(self):
        """
               Deals (removes and returns) the top card of the deck.
               :return: a Card object
               """
        return self.cards.pop(0)

if __name__ == "__main__":
    """
        Example test code when running the file directly.
        Creates a card and a deck, shuffles and deals one card.
        """
    c1 = Card("A", "♣")
    print(c1.suit, c1.rank)
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
    print(deck)