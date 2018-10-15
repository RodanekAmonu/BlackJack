import Testing
import random
import time
import BlackJack as BJ
random.seed = time.time()
def game():
    deck = BJ.Deck()
    deck.make_deck()

    players = []
    try:
        players_count = input("Enter number of players.")
        players_count = int(players_count)
    except Exception as e:
        print("input must be integer")
        print(e)

    for i in range(players_count):
        players.append(BJ.Player())
        players[i].name = i
    #bc - continue condition
    bc = False
    while bc is not True:
        bc = True
        for player in players:
            if isinstance(player, BJ.Player):
                print("\nPlayer {} deck Value is {}.".format(player.name, player.deck_value()))
                print(player.deck)
                if player.deck_value() > 21:
                    print("You lose player {}".format(player.name))
                    player.stand()
                    continue
                elif player.stands == True:
                    continue
                else:
                    p = input("[H]it, [S]tands")
                    if p == "H" or p == "h" :
                        player.hit(deck)
                        print(player.deck[-1])
                        bc = False
                    elif p == "S" or p == "s":
                        player.stand()

        if bc:
            break

    for player in players:
        print("player name: {} \t deck value: {}\n".format(player.name,player.deck_value()))


game()
