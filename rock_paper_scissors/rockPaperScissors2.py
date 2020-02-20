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
        return 'Scissors cuts paper. You win!'
    elif player == 'scissors' and computer == 'rock':
        return 'Rock crushes scissors. You lose!'
    elif player == 'paper' and computer == 'scissors':
        return 'Scissors cuts paper. You lose!'
    elif player == 'paper' and computer == 'rock':
        return 'Paper covers rock. You win!'
    elif player == 'rock' and computer == 'scissors':
        return 'Rock crushes scissors. You win!'
    elif player == 'rock' and computer == 'paper':
        return 'Paper covers rock You lose!.'
    else:# player == computer:
        return ('Both players chose %s. The game is a tie!' %(player))
   
 

gamesPlayed = 0
gamesWon = 0
gamesTied = 0
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
    result = gameMoves(playerMove, computerMove)
    print(result)
    if 'win!' in result:
        gamesWon += 1
    if 'tie! in result':
        gamesTied += 1

    while 
           
    print('You have played %s game%s today. You won %s game%,' % (gamesPlayed, GameS, gamesWon, extraS))
    print('and tied with the computer %s time%s.' %(gamesTied, extraS))
    print('Do you want to play again? (yes or no) ', end='> ')
    playAgain = input()
    if  playAgain.lower().startswith('y'):
        continue
    else:
        print('Thank you for playing. See you again soon!')
        break
