# print(len(line[5]))
import random

class Game:
    def __init__(self):
        self.f = open("words.txt", "r").read().lower().split()
        self.list = []

    def start_game(self):
        for word in self.f:
            if (len(word) == 4):
                self.list.append(word)
        self.ran_num = random.randint(0,len(self.list)-1)
        print("Your word is: \n")
        Mechanics(self.list[self.ran_num]).four()

    def difficulty(self):
        pass


class Mechanics:
    def __init__(self, f):
        self.f = f
        self.char_one = "_"
        self.char_two = "_"
        self.char_three = "_"
        self.char_four = "_"
        self.guesses = 8
        self.used_chars = []
        self.acceptable_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def four(self):
        print(f"{self.char_one} {self.char_two} {self.char_three} {self.char_four}")
        self.response = input(f"You have {self.guesses} guesses. Enter a key to guess ").lower()
        self.test()
        
    def test(self):
        if self.response not in self.acceptable_chars:
            print("Please use a letter of the alphabet")
            self.four()
        if self.response in self.used_chars:
            print("You have already used that character\n")
            self.four()
        else:
            self.used_chars.append(self.response)

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
        

Game().start_game()