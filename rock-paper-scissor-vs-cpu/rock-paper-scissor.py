# -*- coding: utf-8 -*-
import random

check_list = ['rock', 'paper', 'scissor']
won = 'You have won!'

def choices():
    choice = ""
    while choice not in check_list:
        print("Please choose 'rock', 'paper' or 'scissor'!")
        choice = input('> ')
    cpu = random.choice(check_list)
    print('\nPlayer chooses ' + choice, 'and cpu chooses ' + cpu)
    return evaluate(choice, cpu)

def evaluate(choice, cpu):
    if choice == 'rock' and cpu == 'scissor':
        print(won)
    elif choice == 'paper' and cpu == 'rock':
        print(won)
    elif choice == 'scissor' and cpu == 'paper':
        print(won)
    elif choice == cpu:
        print('This is a tie!')
    else:
        print('Cpu has won!')

rematch = 'y'
while rematch != 'n':
    choices()
    rematch = input('\nDo you want to play again? (y/n): ')
