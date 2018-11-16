from random import *
import os

class scissor(object):

    def __lt__(self,other):
        if(isinstance(other, rock)):
            return True
        return False

    def __gt__(self,other):
        if(isinstance(other, paper)):
            return True
        return False

    def __eq__(self,other):
        if(isinstance(other, scissor)):
            return True
        return False

class paper(object):
    def __lt__(self,other):
        if(isinstance(other, scissor)):
            return True
        return False

    def __gt__(self,other):
        if(isinstance(other, rock)):
            return True
        return False

    def __eq__(self,other):
        if(isinstance(other, paper)):
            return True
        return False


class rock(object):
    def __lt__(self,other):
        if(isinstance(other, paper)):
            return True
        return False

    def __gt__(self,other):
        if(isinstance(other, scissor)):
            return True
        return False

    def __eq__(self,other):
        if(isinstance(other, rock)):
            return True
        return False


class Player:
    def play(self):
        varInt = randint(1,3)
        if(varInt == 1):
            return rock()
        if(varInt == 2):
            return scissor()
        if(varInt == 3):
           return paper()

class HumanPlayer:
    def play(self,Letter):
        if(Letter == 's'):
            return scissor()
        if(Letter == 'p'):
            return paper()
        if(Letter == 'r'):
            return rock()

def main():
    AI = Player()
    p1 = HumanPlayer()
    playerScore = 0
    aiScore = 0
    while True:
        print("Type 's' for scissor, 'p' for paper and 'r' for rock or 'q' for quit")
        letter = input("Enter the choice: ")
        choice = p1.play(letter)
        if(letter == 'q'):
            break
        os.system('clear')
        if(letter.lower() == 's' or letter.lower() == 'r' or letter.lower() == 'p'):
            aiChoice = AI.play()
            if(choice == aiChoice):
                print("Oops, same hand")
            elif(choice > aiChoice):
                playerScore +=1
            else:
                aiScore +=1
            print("AI: " + str(aiScore))
            print("Player: " + str(playerScore))
        else:
            print("Wrong key, please try again")

if __name__ == "__main__":
    main()