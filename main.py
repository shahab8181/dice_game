# Developed by shahab
'''>>> Written In Python 3.11.2 
This program is a dice game with other people and the computer... 
It may have some bugs and algorithmic problems(Beta)...
but you can enjoy playing with it, and it includes modules for better performance...
'''

from os import system, getlogin
import time
import pyfiglet
from termcolor import colored as cr
from tools.player_type import Human, Computer

# -------------------- main(menu) game ----------------------- #

print(f'hello {getlogin()}!', end='\n')
print('welcome!', end='\n')
time.sleep(0.7)
print('Please wait...', end='\n')
time.sleep(1)

for x in range(30):
    time.sleep(0.0225)
    print('*', end='')

system('cls')
print(cr(text=pyfiglet.figlet_format('Dice Game'), color='yellow'))
print('loading...', end='\n')

for y in range(35):
    time.sleep(0.03)
    print('_', end='')
    if y == 34:
        print('\n')


# ------------------------ count pc or real players ----------------------------- #

count_of_players = int(input(f'hi {getlogin()}:)!\nHow many players are there? : '))
count_o_computers = int(input('ok!\nHow many of these players are computers? : '))

Totale = count_of_players + (count_of_players - count_o_computers)
players = [0 for x in range(Totale)]


if 2 <= Totale <= 4: # if between 2 and 4
    match Totale:
        case 2: # if  totale ----> 2
            for player_number in range(1, Totale):
                if player_number == 1:
                    Human(player_number)
                else:
                    Computer(player_number)
            else: 
                print('game finished!')
        
        case 3: # if totale ----> 3
            for player_number in range(1, Totale):
                if count_o_computers == 1:
                    if (player_number == 1) or (player_number == 2):
                        [Human(player_number=agin) for agin in range(1, 3)]
                    else:
                        Computer(player_number=3)

                elif count_of_players == 2:
                    if player_number == 1:
                        Human(player_number)
                    elif (player_number == 2) or (player_number == 3):
                        [Computer(player_number=again_pc) for again_pc in range(1, 3)]

                else:
                    [Human(player_number=again) for again in range(1, 4)]
          
            else: print('game finished!')

        case 4: # if totale ---------> 4
            for player_number in range(1, Totale):
                if count_o_computers == 0:
                    [Human(player_number=again) for again in range(1, 5)]
                elif count_o_computers == 1:
                    [Human(player_number=again) for again in range(1, 4)]
                    Computer(player_number=4)
                elif count_o_computers == 2:
                    [Human(player_number=again) for again in range(1, 3)]
                    [Computer(player_number=again) for again in range(1, 3)]
                elif count_o_computers == 3:
                    [Computer(player_number=again) for again in range(1, 4)]
                    Human(player_number=4)

            else: 
                print('game finished!')
                
else: # if lower 2 player
    print('Player number error:(\nBut we start the game with you and the computer:) (1V1)', end='\n')
    Human(player_number=1)
    Computer(player_number=1)


