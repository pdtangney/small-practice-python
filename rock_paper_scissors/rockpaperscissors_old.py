# A simple Rock, Paper, Scissors game

import random
def playAgain():
    anotherround = input('Would you like to play again? (yes, no): ')
    anotherround = anotherround.lower()
    
    if anotherround =='yes' or anotherround =='y':
        return 'yes'
    else:
        print('Thank\'s for playing. Have a nice day.')
        

def validChoice():
    choice = input()
    choice = choice.lower()
    while choice != 'rock' and choice != 'paper' and choice != 'scissors':
        print("Type in 'rock', 'paper', or 'scissors'")
        choice = input()
        choice = choice.lower()
    return choice

def aiChoice():
    words = ['rock','paper','scissors']
    randnum = random.randint(1,3) -1
    aichooses = words[randnum]
    return aichooses

def whoWon(user, ai):
    print('You chose: ' + user)
    print('The computer chose: ' +ai)
    if user == ai:
        print('You both chose ' + user + ' It\'s a tie!')
    elif user == 'rock' and ai == 'paper':
        print('Paper covers rock. You lose')
    elif user == 'rock' and  ai == 'scissors':
        print('Rock smashes scissors. You win!')
    elif user == 'paper' and ai == 'rock':
        print('Paper covers rock. You win!')
    elif user =='paper' and ai == 'scissors':
        print('Scissors cut paper. You lose.')
    elif user == 'scissors' and ai == 'rock':
        print('Rock smashes scissors. You lose.')
    elif user == 'scissors' and ai == 'paper':
        print('Scissors cuts paper. You win!')
        
    return
    

name = input('What is your name?')
print ('Hello, ' + name +'!')
print('Welcome to \'Rock, Paper, Scissors.\'')
playagain = 'yes'
while playagain == 'yes':
    validuserchoice = '' #clear our choices from the previous game, if any.
    airesponse = ''
    print('Make your choice, then press (Enter)')

    validuserchoice = validChoice()
    airesponse = aiChoice()
    whoWon(validuserchoice, airesponse)
    playagain = playAgain()
