from deck import Deck, Card

class Hand:
    def __init__(self, deck):
        """
              Constructor for the Hand class.
              :param deck: a Deck object used to deal cards
              :return: None
              """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
               Getter for the list of cards in the hand.
               :return: list of 5 Card objects
               """
        return self._cards

    def __str__(self):
        """
              Converts the hand to string format for printing.
              :return: string representation of the hand
              """
        return str(self.cards)

    @property
    def is_flush(self):
        """
             Checks if all cards have the same suit.
             :return: True if the hand is a flush, False otherwise
             """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def num_matches(self):
        """
              Counts the number of matching ranks among the cards.
              Each unique match between two cards increases the count.
              :return: integer number of matches (e.g., 2 for one pair, 4 for two pairs)
              """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Checks if the hand contains exactly one pair.
         :return: True if there is one pair, False otherwise
        """
        if self.num_matches == 2:
            return True
        return False

    @property
    def is_2_pair(self):
        """
                Checks if the hand contains exactly two pairs.
                :return: True if there are two pairs, False otherwise
                """
        if self.num_matches == 4:
            return True
        return False

    @property
    def is_trips(self):
        """
                Checks if the hand contains three cards of the same rank.
                :return: True if three of a kind, False otherwise
                """
        if self.num_matches == 6:
            return True
        return False

    @property
    def is_quads(self):
        """
               Checks if the hand contains four cards of the same rank.
               :return: True if four of a kind, False otherwise
               """
        if self.num_matches == 12:
            return True
        return False

    @property
    def is_full_house(self):
        """
                Checks if the hand is a full house (3 of a kind + a pair).
                :return: True if full house, False otherwise
                """
        if self.num_matches == 8:
            return True
        else:
            return False

    @property
    def is_straight(self):
        """
               Checks if the hand forms a straight (consecutive ranks).
               :return: True if straight, False otherwise
               """
        if self.num_matches != 0:
            return False
        self.cards.sort()
        if Card.RANKS.index(self.cards[-1].rank) != \
                Card.RANKS.index(self.cards[0].rank) + 4:
            return False
        return True
matches = 0
count = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    count += 1
    if hand.is_straight:
        # print(hand)
        matches += 1
        # break

print(f"The probability of straight is {100*matches/count}%")