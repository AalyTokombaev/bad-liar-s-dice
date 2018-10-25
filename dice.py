from random import randint


class Turn:
    def __init__(self, *players, first=False):
        self.players = players
    
    def bet(self, player, last_player):
        pass

    def call(self):
        pass

    def bluff(self):
        pass

    def winner(self):
        pass
        

    
class Round:
    def __init__(self, *players):
        self.players = list(players)
        self.turn = 0 # first turn

    def is_first_turn(self):
        return self.turn == 0
    
    def play(self):





class GameState:
    def __init__(self, *players):
        if len(players) < 2:
            raise ValueError("Not enough players! (at least 2 needed)")
        self.players = list(players)
        self.round = 0


    def play(self):
        round = Round(*self.players)

        


    
    def run(self):
        while len(self.players) > 1:
            self.play()
        self.players[0] # won the game!



class Player:
    def __init__(self, name="Snoiks"):
        self.dice = 5
        self.name = name
        self.hand = self.roll()

    def alisve(self):
        return self.dice > 0

    def roll(self):
        return [randint(1, 6) for i in range(self.dice)]

    def lose(self):
        self.dice -= 1




if __name__ == '__main__':
    p1 = Player()
    p2 = Player("Your pal Patine")
    gs = GameState(p1, p2)
    gs.play()
    print(gs.round)
