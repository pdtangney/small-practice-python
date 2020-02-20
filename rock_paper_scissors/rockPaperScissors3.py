# Rock-Paper-Scissors
# 2/10/2020
# Version 0.0.02-PRE-ALPHA

import random
import time

def intro():
    print('''
************
#   ROCK   #
************
~   PAPER  ~
************
^ SCISSORS ^
************
''')
    print('\tBY: Peter Tangney')

def game_rules():
    print('Game rules go here.')
    
def type_in_move():
    move =''
    while move != 'rock' and move != 'paper' and move != 'scissors': 
        print('What is your move? (rock, paper or scissors)', end='> ')
        move = input().lower()
    return move

def computer_choice():
        allowedChoices = 'rock paper scissors'.split()
        choice = random.choice(list(allowedChoices))
        return choice

    
def game_moves(player, computer):
    if player == 'scissors' and computer == 'paper':
        print('Scissors cuts paper. You win!')
        return 'win'
    elif player == 'scissors' and computer == 'rock':
        print('Rock crushes scissors. You lose!')
        return 'lost'
    elif player == 'paper' and computer == 'scissors':
        print('Scissors cuts paper. You lose!')
        return 'lost'
    elif player == 'paper' and computer == 'rock':
        print('Paper covers rock. You win!')
        return 'win'
    elif player == 'rock' and computer == 'scissors':
        print('Rock crushes scissors. You Win!')
        return 'win'
    elif player == 'rock' and computer == 'paper':
        print('Paper covers rock You lose!.')
        return 'lost'
    else:
        print('Both players chose %s. The game is a tie!' %(player))
        return 'tie'
   
 
gamesPlayed = 0 
gamesWon = 0
gamesLost = 0
gamesTied = 0
intro()
while True:
    gamesPlayed += 1
    playerMove = type_in_move()
    print('\nYou chose %s.\n' % (playerMove))
    time.sleep(1)
    computerMove = computer_choice()
    print('The computer chose %s.\n' %(computerMove))
    time.sleep(1)
    result = game_moves(playerMove, computerMove)
    if result == 'win':
        gamesWon += 1
    elif result == 'lost':
        gamesLost += 1
    else:
        gamesTied += 1
    print('\nHere are your game statistics so far:')
    if gamesPlayed == 1:
        print('Out of one game played,', end='')
        if result == 'win':
            print(' you won.')
        elif result == 'tie':
            print(' you tied with the computer.')
        else:
            print(' you lost.')
    else:
        print('Out of %s games played,' %(gamesPlayed), end='')

        if gamesWon == 1:
            print(' you won once.')
        else:
            print(' you have won %s games.' %( gamesWon))
        if gamesTied == 1:
            print('you tied with the computer once.')
        else:
            print('you tied with the computer in %s games.' % (gamesTied))
        if gamesLost == 1:
            print('you have lost one game.')
        else:
             print('you have lost %s games.' %(gamesLost))
             
    print('\n\nDo you want to play again? (yes or no)', end='> ')
    playAgain = input()
    if  playAgain.lower().startswith('y'):
        continue
    else:
        print('\n\nThank you for playing. See you again soon!')
        break 