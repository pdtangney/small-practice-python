# Rock-Paper-Scissors
# 2/18/2014
# Version 0.0.01-PRE-ALPHA

import random
import time

def typeInMove():
    print('What is your move? (rock, paper or scissors) ', end='> ')
    move = input()
    move = move.lower()
    while move != 'rock' and move != 'paper' and move != 'scissors': 
        print('Type in either rock, paper or scissors. ', end='> ')
        move = input()
        move = move.lower()
    return move

def computerChoice():
        # In this, pre-alpha version, the computer chooses rock, paper or scissors
        # purely at random. Future versions will have a better algorithm once I get
        # better and move confident at programming.
        allowedChoices = 'rock paper scissors'.split()
        choice = random.choice(list(allowedChoices))
        return choice

    
def gameMoves(player, computer):
    if player == 'scissors' and computer == 'paper':
        print('Scissors cuts paper. You win!')
        return 'win'
    elif player == 'scissors' and computer == 'rock':
        print('Rock crushes scissors. You lose!')
        return 'lose'
    elif player == 'paper' and computer == 'scissors':
        print('Scissors cuts paper. You lose!')
        return 'lose'
    elif player == 'paper' and computer == 'rock':
        print('Paper covers rock. You win!')
        return 'win'
    elif player == 'rock' and computer == 'scissors':
        print('Rock crushes scissors. You Win!')
        return 'win'
    elif player == 'rock' and computer == 'paper':
        print('Paper covers rock You lose!.')
        return 'lose'
    else:# player == computer:
        print('Both players chose %s. The game is a tie!' %(player))
        return 'tie'
   
 

gamesPlayed = 0
gamesWon = 0

while True:
    gamesPlayed += 1
    playerMove = typeInMove()
    print()
    print('You chose %s.' % (playerMove))
    print()
    time.sleep(1)
    computerMove = computerChoice()
    print('The computer chose %s. ' %(computerMove))
    time.sleep(1)
    print()
    gameMoves(playerMove, computerMove)
    print()
    print('You have played %s games today. You have won %s of them.' % (gamesPlayed, gamesWon))
    print('Do you want to play again? (yes or no) ', end='> ')
    playAgain = input()
    if  playAgain.lower().startswith('y'):
        continue
    else:
        print('Thank you for playing. See you again soon!')
        break
