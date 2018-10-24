from random import randint

def convert(_input): return list(map(int, _input.split()))

class Gamestate:
    def __init__(self, *player):
        if len(players) < 2:
            raise ValueError('Can\'t play alone.')
        self.players = list(players)
        self.bet = list()
        #self.turn = 0
        

    def round():
        last_player = Player()
        for player in self.players:
            if not player.alive():
                continue
            in not self.bet:
                # First turn
                player.roll()
                self.bet = convert(input(f"Sage your bet {player.name}"))
                last_player = player

            player.roll()
            choice = input(f"Here's your hand: {player.hand}\n what do you choose to do?")

            if choice == 'bluff':
                if bluff(self.table, self.bet):
                    last_player.lose()
                else:
                    player.lose()
            
            if choice == 'call':
                if player.call(self.table(), self.bet):
                    for p in self.players:
                        if p != player:
                            p.lose()
                else:
                    player.lose()
            
            if choice == 'raise':
                while True:
                    bet = convert(input("Bet: "))
                    if bet[0] < self.bet or (bet[0] == self.bet[0] and bet[1] < self.bet[1]):
                        print("This is not allowed!")
                    else:
                        break
                self.bet = bet


        def play(self):
            pass


        

    def table(self):
        dice = list()
        for player in self.players:
            for value in player.hand:
                dice.append(value)
        return dice

    def show(self, arg, player):
        pass
        

    
class Player:
    def __init__(self, name,  hand):
        self.dice = 5
        self.hand = hand
        self.name = name


    def roll(self):
        self.hand = [randint(1,6) for i in range(dice)]

    def bet(self, amt, die):
        pass

    def call(self, bet, dice):
        return dice.count(bet[1]) == bet[0]



        
    
    def bluff(self, dice, bet):
        return dice.count(bet[1]) < bet[0]
    
    def lose(self):
        self.dice -= 1
    
    def alive(self):
        return self.dice > 0

        

    


    


    


