
"""

Richard Lefrandt
richlefrandt@msn.com
Rock Paper Scissors Game
Imports Random

Program


"""
# import random for randomint
import random

rock = 'r'
paper = 'p'
scissors = 's'


def printWelcome():
    """ This prints welcome page
    """
    
    print("Welcome to Rock/Paper/Scissors game")

    print("Rules of the game:")
    print("\tYou and the computer will each pick (r)ock, (p)aper, (s)cissor.")
    print("\tThe winner will be decided using following policy:")
    print("\tRock wins over Scissors but loses to Paper")
    print("\tPaper wins over Rock but loses to Scissors")


    print("Let the game begin!! Enter 'q' to quit.")

   
def getUserPick():
    """Prompt the user to make a choice between rps
        returns the users pick
    """
    return input("Your turn. Pick(r)ock,(p)aper,(s)cissors:")
    
def pickRPS():
    return random.choice(['rock', 'paper', 'scissors'])
        
    # alternative function sequence = ['rock', 'paper', 'scissors']

    # not needed random.choice(sequence)
        # startswith()
def getResult(computer, player):#if they're equal, return a tie
    if computer==player:
        return 'tie'
   
    if computer==paper:#if computer is paper, return win
        if player == rock:
            return 'Computer wins'
        if player == scissors:
            return 'You win' #'player'
    if computer == scissors:#if computer is scissors, return win
        if  player == rock:
            return 'You win' #'player'
        if player == paper:
            return 'computer'
    if computer == rock:#if computer is rock, return win
        if player == paper:
            return 'You win' #'player'
        if player == scissors:
            return 'computer'



def main():
    printWelcome()
    player_victories = 0 
    computer_victories = 0
    number_rounds = 0
    number_ties = 0
    user_decision = getUserPick()

    while user_decision != 'q':
        computer_decision = ('pickRPS', 'getResult')
        print(main)
        
    print("Number of rounds:")
    print("Number of times you won:")      
    print("Number of times computer won:")    
    print("Number of ties:")

    print("Bye")    


main()


      

