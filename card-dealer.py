import random
NUMBERS = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
SUITS = ("Clubs", "Spades", "Diamonds", "Hearts")
PLAYER_COUNT = 5 #change this to change number of players

class Dealer:
    def __init__(self, players):
        self.players = players
        self.playerhands = [[None for _ in range(2)] for _ in range(players)]
        self.table_cards = []
        self.river = []

    def fdeal(self): #deals just to players
        for x in range(self.players):
            for i in range(2):
                while True:
                    num = random.choice(NUMBERS)
                    suit = random.choice(SUITS)
                    card = f"{num}-{suit}"
                    if card not in self.table_cards:
                        break
                self.playerhands[x][i] = card
                self.table_cards.append(card)
        return f"{self.players} hands successfully made."

    def printhands(self): #simply just printing function
        for x in range(self.players):
            card1 = self.playerhands[x][0].split("-")
            card2 = self.playerhands[x][1].split("-")
            print(f"Player {x+1} has the {card1[0]} of {card1[1]} and the {card2[0]} of {card2[1]}")

    def add1card(self):
        for i in range(1): #just incase playing different rules
            while True:
                num = random.choice(NUMBERS)
                suit = random.choice(SUITS)
                card = f"{num}-{suit}"
                if card not in self.table_cards:
                    break
            self.table_cards.append(card)
            self.river.append(card)
        return self.river

    def add3cards(self):
        for i in range(3): #just incase playing different rules
            while True:
                num = random.choice(NUMBERS)
                suit = random.choice(SUITS)
                card = f"{num}-{suit}"
                if card not in self.table_cards:
                    break
            self.table_cards.append(card)
            self.river.append(card)
        return self.river

class Game:
    def __init__(self):
        self.dealer = Dealer(PLAYER_COUNT)
        self.mimimum = 0
        self.pot = 0 #this is overall pot, not per player
        self.playerbets = [0 for _ in range(PLAYER_COUNT)] #this is per player
        self.playerfolds = [False for _ in range(PLAYER_COUNT)]
        self.playerchips = [1000 for _ in range(PLAYER_COUNT)] #this is per player, just an example

    def bets(self):
        #TODO NEED TO RELOOP TILL ALL BETS ARE SAME
        for x in range(self.dealer.players):
            if self.playerfolds[x]:
                while True:
                    try:
                        bet = int(input(f"Player {x+1}, please enter your bet (-1 to fold): "))
                        if bet == -1:
                            print("You have folded.")
                            self.playerfolds[x] = True
                            break
                        elif bet < minimum:
                            print("You need to bet at least the minimum.")
                            continue
                        else:
                            if bet > self.playerchips[x]:
                                print("You cannot bet more than you have.")
                                continue
                            else:
                                if bet > minimum:
                                    print(f"You have raised the bet to {bet}.")
                                    minimum = bet
                                else:
                                    print(f"You have called the bet of {bet}.")
                                pot += bet
                                self.playerbets[x] += bet
                                self.playerchips[x] -= bet
                        break
                    except ValueError:
                        print("Please enter a valid number.")
            else:
                pass



def cligameplay():
    pass





# This is just used to deal cards and how no gameplay
def deal():
    game = Dealer(PLAYER_COUNT)
    print(game.fdeal()) #all cards are delt to players
    game.printhands() #prints out all cards (obviously wouldn't use in real game)

    for x in range (3):
        if x < 2:
            table = game.add1card()
            print("---------- River ----------")
            for x in table:
                card = x.split("-")
                print(f"The {card[0]} of {card[1]} is on the table")
            print("----------       ----------") 
        else:
            table = game.add3cards()
            print("---------- River ----------")
            for x in table:
                card = x.split("-")
                print(f"The {card[0]} of {card[1]} is on the table")
            print("----------       ----------")

if __name__ == "__main__":
    deal()
