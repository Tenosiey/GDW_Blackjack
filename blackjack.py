import random

def blackjack_init():    
    game_count = 0

    shoe = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4*6         # Creating the shoe with 6 seperate decks with 13*4 cards

    def deal_player(shoe):
        player_hand = []
        for i in range(2):
            random.shuffle(shoe)
            card = shoe.pop()
            if card == 11:
                card = "J"
            if card == 12:
                card = "Q"
            if card == 13:
                card = "K"
            if card == 14:
                card = "A"
            player_hand.append(card)

        return player_hand

    def deal_dealer(shoe):
        dealer_hand = []
        for i in range(2):
            random.shuffle(shoe)
            card = shoe.pop()
            if card == 11:
                card = "J"
            if card == 12:
                card = "Q"
            if card == 13:
                card = "K"
            if card == 14:
                card = "A"
            dealer_hand.append(card)

        return dealer_hand

    def player_total(player_hand):
        player_total = 0
        
        for card in player_hand:
            if card == "J" or card == "Q" or card == "K":
                player_total += 10
            elif card == "A" and player_total >= 11:
                player_total += 1
            elif card == "A" and player_total <= 10:
                player_total += 11
            else:
                player_total += card

        print("Current Player Hand is: " + str(player_hand))
        print("Current Player Total is: " + str(player_total))
        return player_total

    def dealer_total(dealer_hand):
        dealer_total = 0
        
        for card in dealer_hand:
            if card == "J" or card == "Q" or card == "K":
                dealer_total += 10
            elif card == "A" and dealer_total >= 11:
                dealer_total += 1
            elif card == "A" and dealer_total <= 10:
                dealer_total += 11
            else:
                dealer_total += card

        print("Current Dealer Hand is: " + str(dealer_hand))
        print("Current Dealer Total is: " + str(dealer_total))
        return dealer_total
    
    player_total(deal_player(shoe))
    dealer_total(deal_dealer(shoe))

if __name__ == "__main__":
    blackjack_init()
