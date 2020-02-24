# print(len(line[5]))

class Game:
    def __init__(self):
        self.f = open("testwords.txt", "r").read().lower().split()
# dont forget to close the text file at some point, or dont open it multiple times

    def start_game(self):
        print("Your word is: \n")
        Mechanics(self.f, 5).four()

    def difficulty(self):
        pass

    def reset_game(self):
        pass


class Mechanics:
    def __init__(self, f, x):
        self.f = f[x]
        self.one = "_"

    def four(self):
        print(f"{self.one}")
        self.response = input("Enter a key to guess ")
        self.test()
        
    def test(self):
        if (self.response == self.f[0]) or (self.response == self.f[1]) or (self.response == self.f[2]) or (self.response == self.f[3]):
        
        

            



Game().start_game()