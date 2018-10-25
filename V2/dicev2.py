from random import randint, choice

def parse(_input):
    return list(map(int, _input.split()))

class Player:
    def __init__(self, name):
        self.name = name
        self.dice = 5
        self.bet = bet
        self.hand = list()

    def act(self, bet):
        pass

    def _raise(self):
        bet = parse(input("Raise the bet:\n>"))


    def bet(self):
        bet = parse(input("Make a bet:\n>"))
        return bet

    def roll(self):
        self.hand = [randint(1,6) for i in range(self.dice)]


    
class Turn:
    def __init__(self, player, bet=None):
        pass


    def act(self):
        if bet:
            action = parse(input("What do you wish to do?\n>"))
            if action == 'raise':
                return player._raise(bet)
            if action == 'call'
                return 'call'
        else:
            return player.bet()


class Round:
    def __init__(self, players):
        self.players = players
        for i in self.players:
            i.roll()
        self.last_player = None
        self.bet = None

    def show_dice(self):
        dice = list()
        for player in players:
            for die in player.hand:
                dice.append(die)
        return dice

    def play(self):
        pass

    def end(self):
        pass
                
                

                

        



class GameState:
    def __init__(self, players):
        self.player = list(players)

    def play(self):
        round = Round(*players)
        while True:
            game = round.play()
            if game == 'end':
                break
        self.play()
        
