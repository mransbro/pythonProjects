import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        actual = min([self.count(), num])
        if actual == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def shuffle(self):
        random.shuffle(self.cards)
        return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)

class Player:
    def __init__(self):
        self.hand = []

    def deal(self, cards):
        if type(cards) == list:
            self.hand += cards
        else:
            self.hand.append(cards)

        if self.sum_hand() > 21:
            print(f"You lose, you're bust.")
            print(f"{self.hand}")
            quit()

    def show_hand(self):
        return self.hand

    def sum_hand(self):
        total = 0
        for card in self.hand:
            if card.value in ["J", "Q", "K"]:
                total += 10
            elif card.value == "A":
                total += 1
            else:
                total += int(card.value)
        return total




deck = Deck()
deck.shuffle()
playerOne = Player()
dealer = Player()

play = input("Would you like to start the game? \nPress any key to continue \n")


playerOne.deal(deck.deal_hand(2))
dealer.deal(deck.deal_hand(2))


print(f"Your hand is {playerOne.show_hand()[0]} and {playerOne.show_hand()[1]}")
# Show dealers single card
print(f"The dealer has {dealer.show_hand()[0]} and one other card.")


again = input("\nWould you like another card? \nyes or no \n")
if again == "yes":
    playerOne.deal(deck.deal_card())
    print(f"Your hand is now {playerOne.show_hand()[0]}, {playerOne.show_hand()[1]} and {playerOne.show_hand()[2]}")

if dealer.sum_hand() < 16:
    print(f"\nThe dealer has less then 16 and will deal themselves another card\n")
    dealer.deal(deck.deal_card())


playersum = playerOne.sum_hand()
dealersum = dealer.sum_hand()
if playersum > dealersum:
    print(f"Congrats your hand of {playersum} beats the dealers {dealersum}.")
else:
    print(f"Sorry you lose. The dealers {dealersum} beats your {playersum}.")
