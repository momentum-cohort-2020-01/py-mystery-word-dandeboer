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
        self.char_one = "_"
        self.char_two = "_"
        self.char_three = "_"
        self.char_four = "_"
        self.guesses = 6

    def four(self):
        print(f"{self.char_one} {self.char_two} {self.char_three} {self.char_four}")
        self.response = input(f"You have {self.guesses} guesses. Enter a key to guess ")
        self.test()
        
    def test(self):
        # for char in self.f[0:]:
        if (self.response == self.f[0]):
            self.char_one = self.response
        if (self.response == self.f[1]):
            self.char_two = self.response
        if (self.response == self.f[2]):
            self.char_three = self.response
        if (self.response == self.f[3]):
            self.char_four = self.response

        if (self.response != self.f[0]) and (self.response != self.f[1]) and (self.response != self.f[2]) and (self.response != self.f[3]):
            self.guesses -= 1
            if (self.guesses <= 0):
                print(f"You lose! the word was {self.f}")
            else:
                print("Incorrect \n")
                self.four()
        else:
            if (self.char_one != "_") and (self.char_two != "_") and (self.char_three != "_") and (self.char_four != "_"):
                print(f"The word was {self.f} \nYou Win!")
            else:
                print("")
                self.four()

        # self.four()
        
        

            



Game().start_game()