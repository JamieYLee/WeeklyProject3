from random import shuffle

# function creating deck
# suits - Hearts, Spades, Diamonds, Clubs - ranks: A, 2-10, J, Q, K
# returns a shuffled deck with 52 cards
def deck():
    deck = []
    for suit in ['Hearts', 'Spades', 'Diamonds', 'Clubs']:
        for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            deck.append(rank)
    shuffle(deck)

    return deck

# function for counting points
# takes in the player's cards and returns its total points
def countPoint(myCards):
    myCount = 0
    aceCount = 0

    for card in myCards:
        if card == 'J' or card == 'Q' or card == 'K' or card == '10':
            myCount += 10
        elif card != 'A':
            myCount += int(card)
        else:
            myCount += 1

    if aceCount == 1 and myCount >= 10:
        myCount += 11
    elif aceCount != 0:
        myCount += 1

    return myCount


# function for creating hands of player and dealer
# randomly gives each 2 cards from the deck
# returns a list with both hands
def createPlayingHands(myDeck):
    dealerHand = []
    playerHand = []

    dealerHand.append(myDeck.pop())
    dealerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())

    while countPoint(dealerHand) <= 16:
        dealerHand.append(myDeck.pop())

    return [dealerHand, playerHand]

# create game stuff
game = ""
myDeck = deck()
hands = createPlayingHands(myDeck)
dealer = hands[0]
player = hands[1]

# game loop
while(game != "exit"):
    dealerCount = countPoint(dealer)
    playerCount = countPoint(player)

    print("Dealer has: {}".format(dealer[0]))
    print()
    print("You have: {}".format(player))

    if playerCount == 21:
        print("Blackjack! You win!")
        break
    elif playerCount > 21:
        print("You BUSTS! With {} points. Dealer wins!".format(str(playerCount)))
        break
    elif dealerCount > 21:
        print("Dealer BUSTS! With {} points. You win!".format(str(dealerCount)))

    game = input("What would you do? H for Hit / S for Stand: ")

    if game.upper() == 'H':
        player.append(myDeck.pop())
    elif playerCount > dealerCount:
        print("You won with {} points".format(str(playerCount)))
        print("Dealer has {} or {} points.".format(str(dealer), str(dealerCount)))
        break
    else:
        print("Dealer wins!")
        print("Dealer has {} or {} points.".format(str(dealer), str(dealerCount)))
        break
