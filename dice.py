from random import randint


class Turn:
    def __init__(self, *players):
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

    
    def play(self):
        print("Hey I'm playing here!")




class GameState:
    def __init__(self, *players):
        if len(players) < 2:
            raise ValueError("Not enough players! (at least 2 needed)")
        self.players = list(players)
        self.round = 0

    def is_first_round(self):
        return self.round == 0

    def play(self):
        if self.is_first_round():
            round = Round(*self.players)
            round.play()
            self.round += 1
        else:
            pass
        


    
    def run(self):
        while len(self.players) > 1:
            self.play()
        self.players[0] # won the game!



class Player:
    def __init__(self, name="Snoiks"):
        self.dice = 5
        self.name = name
        self.hand = self.roll()

    def alve(self):
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
