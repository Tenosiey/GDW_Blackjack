import random

def deal():
    hand = []

    for i in range(2):
        card = shoe.pop()
        if card == 1:
            card = "A"
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        hand.append(card)
    return hand

def total(hand):
    total = 0
    for card in hand:
        if card == "A" and total >= 11:
            total += 1
        elif card == "A" and total <= 10:
            total += 11
        elif card == "J" or card == "Q" or card == "K":
            total += 10
        else:
            total += card
    return total

def blackjack():
    print("Player got a Blackjack")

def play_split():
    input("Would you like to split your cards? y/n\n")

def stand():
    print("Ok, stand")

def hit():
    print("Ok, hit")

def double():
    print("Ok, double")

def play():
    choice = input("Would you like to Hit, Stand or Double?\n")
    if choice == "stand":
        stand()
    elif choice == "hit":
        hit()
    elif choice == "double":
        double()
    else:
        print("Error, command not known")

def game():
    dealer_hand = deal()
    player_hand = deal()

    dealer_total_var = total(dealer_hand)
    player_total_var = total(player_hand)

    print("Dealers hand is: " + str(dealer_hand))
    print("Dealers total is: " + str(dealer_total_var))
    
    print("Players hand is: " + str(player_hand))
    print("Players total is: " + str(player_total_var))

    if player_total_var == 21:
        blackjack()
    elif player_hand[0] == player_hand[-1]:
        play_split()
    else:
        play()

if __name__ == "__main__":
    decks = 6                                                               # Setting the size of the shoe
    shoe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4*decks              # Creating the shoe
    random.shuffle(shoe)                                                    # Shuffle the shoe (5 times for good meassure)

    game()
