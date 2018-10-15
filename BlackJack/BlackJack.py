import random

figures = ("Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King")
colors = ("Heart", "Diamond", "Spade", "Club")


def split(x):
    ret = []
    for i in x:
        ret.append(i)
    return ret


class Card():

    def __init__(self, fig, col):
        self.figure = -1
        self.color = -1
        for f in figures:
            if fig == f:
                self.figure = fig
            else:
                continue
        for c in colors:
            if col == c:
                self.color = col
            else:
                continue

    def value(self):
        if isinstance(self.figure, str):
            if len(self.figure) > 1:
                if self.figure == "Jack" or self.figure == "Queen" or self.figure == "King":
                    return 10
                if self.figure == "Ace":
                    return [1, 11]
        elif isinstance(self.figure, int):
            return int(self.figure)

    def __repr__(self):
        return '(' + str(self.figure) + " " + str(self.color) + ')'



class Deck():

    def __init__(self):
        self.deck = []
        self.ace_mul = 1

    def __str__(self):
        s = ""
        return self.deck

    def __repr__(self):
        return self.deck

    def __len__(self):
        return self.deck.__len__()

    def make_deck(self, n=1):
        for i in range(n):
            for color in colors:
                for figure in figures:
                    if n > 1:
                        z = (Card(figure,color), i + 1)
                    else:
                        z = Card(figure, color)
                    self.deck.append(z)

    def __getitem__(self, item):
        return self.deck[item]

    def move_card(self, card_id, destination):
        if isinstance(destination, Deck):
            if self.deck[card_id] is not None:
                destination.add_card(self.deck[card_id])
                self.deck.pop(card_id)
                return True
            else:
                return False

    def add_card(self, c):
        if isinstance(c, Card):
            if c.figure == "Ace" and self.deck_value() > 11:
                self.ace_mul = 0

            self.deck.append(c)

            return True
        else:
            return False

    def deck_value(self):
        v = 0
        for c in self.deck:
            if isinstance(c, Card):
                if c.figure == "Ace":
                    v += 1 + self.ace_mul * 10
                else:
                    v += c.value()
        return v


class Player(Deck):
    def __init__(self):
        super().__init__()
        self.name = ''
        self.stands = False

    def hit(self, deck):
        if isinstance(deck, Deck):
            card_id=0
            while True:
                card_id = random.randint(0, deck.__len__())
                if deck[card_id] is not None:
                    deck.move_card(card_id, self)
                    return deck.deck_value()
                else:
                    continue

    def stand(self):
        self.stands = True
        return self.deck_value()

    def split(self):
        pass

    def insurance(self):
        pass

