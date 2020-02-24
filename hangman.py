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

    def reset_game(self):
        pass


class Mechanics:
    def __init__(self, f):
        self.f = f
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
        
        

            

# print(random.randint(1,26))
Game().start_game()