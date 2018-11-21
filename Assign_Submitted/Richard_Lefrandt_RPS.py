
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
    return random.choice(['r', 'p', 's'])
        
    # alternative function sequence = ['rock', 'paper', 'scissors']
    # not needed random.choice(sequence)
    # startswith()
    
def getResult(computer, player):#if they're equal, return a tie
    if computer==player:
        return 'Its a tie'
   
    if computer==paper:#if computer is paper, return win
        if player == rock:
            print('You pick rock computer pick paper')
            return'Computer wins'
        if player == scissors:
            print('You pick scissors, computer picked paper')
            return'You win' #'player'
    if computer == scissors:#if computer is scissors, return win
        if  player == rock:
            print('You pick rock, computer pick scissors')
            return'You win' #'player'
        if player == paper:
            print('You pick paper, computer pick scissors')
            return'Computer wins'
    if computer == rock:#if computer is rock, return win
        if player == paper:
            print('You pick paper, computer picked rock')
            return'You win' #'player'
        if player == scissors:
            print('You picked scissors, computer picked rock')
            return'Computer wins'

"""Main Function main(): that ties together all the following functions
    printWelcome, getUserPick, pickRPS, getResult
    Also while user decision loop with quit and if current results of
    Computer wins, You win, and Its a tie using == and +=1,
    including number rounds. 
"""

def main():
    printWelcome()
    player_victories = 0 
    computer_victories = 0
    number_rounds = 0
    number_ties = 0
    user_decision = getUserPick()
    
    
    while user_decision != 'q':
        computer_decision = pickRPS()
        current_result = getResult(computer_decision, user_decision)
        print(current_result)
        if current_result == 'Computer wins':
            computer_victories+=1
        if current_result == 'You win':
            player_victories+=1 
        user_decision = getUserPick()
        if current_result == 'Its a tie':
            number_ties+=1
        number_rounds+=1

    #Print Final Counts    
    print("Number of rounds:", number_rounds)
    print("Number of times you won:", player_victories)      
    print("Number of times computer won:", computer_victories)    
    print("Number of ties:", number_ties)

    print("Bye")    

main()


      
