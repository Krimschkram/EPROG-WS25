import random


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score = {player1: 0, player2: 0}
        self.winner = None

    def announce_winner(self, player):
        if self.winner is None:
            self.winner = player
            print(f"The winner is {player}!")
        else:
            raise Exception("Game already has a winner.")

    def update_score(self, player, points):
        if player in self.score:
            self.score[player] += points
        else:
            raise Exception("Player not found in the game.")


class Cointoss(Game):

    def play_round(self):

        if self.winner is not None:
            print("Das Spiel ist bereits beendet")
            return

        x = random.randint(0, 1)  # 0 = Kopf, 1 = Zahl
        if x == 0:
            self.update_score(self.player1, 1)
            if self.score[self.player1] == 3:
                self.announce_winner(self.player1)
        else:
            self.update_score(self.player2, 1)
            if self.score[self.player2] == 3:
                self.announce_winner(self.player2)
        print(f"Der Spielstand ist {self.score[self.player1]} : {self.score[self.player2]}")


class Battleship1d(Game):

    def __init__(self, player1, player2):
        super().__init__(player1, player2)
        self.ship1 = random.randint(1, 10)
        self.ship2 = random.randint(1, 10)
        self.Options1 = [x for x in range(1, 11)]
        self.Options2 = [x for x in range(1, 11)]

    def play_round(self):

        if self.winner is not None:
            print("Das Spiel ist bereits beendet")
            return

        shot1 = int(input(f"Player1 choose a field from {self.Options1}: "))
        if shot1 not in self.Options1:
            print("You already checked that field")
            shot1 = int(input(f"Player1 choose a field from {self.Options1}: "))
        if shot1 == self.ship2:
            self.announce_winner(self.player1)
            return
        else:
            self.Options1.remove(shot1)
            print("You missed the ship")

        shot2 = int(input(f"Player2 choose a field from {self.Options2}: "))
        if shot2 not in self.Options2:
            print("You already checked that field")
            shot2 = int(input(f"Player2 choose a field from {self.Options2}: "))
        if shot2 == self.ship1:
            self.announce_winner(self.player2)
        else:
            self.Options2.remove(shot2)
            print("You missed the ship")


game1 = Cointoss("a", "b")

while game1.winner is None:
    game1.play_round()

game2 = Battleship1d("a", "b")

while game2.winner is None:
    game2.play_round()