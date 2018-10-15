import BlackJack as BJ
from random import choice
numberOdDecks = 1

card = BJ.Card("Ace", "Spade")
card2 = BJ.Card("8", "Spade")
testDeck = BJ.Deck()
testDeck.make_deck()
td2 = BJ.Deck()
td2.add_card(card)
td2.add_card(card2)
welcome_msg = "Some info Here"
player = BJ.Player()

print("BlackJack by SK\n_______________________________________________")
print(welcome_msg)
print("_______________________________________________")
def test():
    print("\n\nTesting:")


    print("test deck before moving")
    print(td2.deck)
    print(td2.deck_value())
    testDeck.move_card(3, td2)
    print("test deck after moving")
    print(td2.deck)
    print(td2.deck_value())
    print(testDeck.deck)
    print("moving same card")
    testDeck.move_card(33, td2)
    print(td2.deck)
    print(td2.deck_value())
    print(testDeck.deck)

    print("Player hit")
    player.hit(testDeck)
    print(player.deck)
    print(player.deck_value())
    # print(testDeck.deck_value(0))

    # print(choice(testDeck))
    #wyświetlanie kart w talii działa
    # for c in testDeck.deck:
    #     print(c)
