from random import randint
from termcolor import colored as cr
import time


# It must be determined whether the player is a human or a computer.


def Human(player_number:int) -> None:
        input('ready %d ? please enter any key to start game...\n' % player_number)
        while True:
            p1 = randint(1, 6)
            if p1 != 1:
                players[0] += p1
                print(cr('----------------------------------------------\n', color='dark_grey'))
                print('\t#######\n\t##({0:})##\n\t#######'.expandtabs(tabsize=1).format(cr(p1, color='green')), end='\n\n')
                print(cr('----------------------------------------------\n', color='dark_grey'))
                time.sleep(2)
                input(cr('try your luck : (enter any key to try again...) \n', color='dark_grey'))
                p1 = None
                continue
            else:
                players[0] += 1
                print('\t#######\n\t##({0:})##\n\t#######'.expandtabs(tabsize=1).format(cr(1, color='red')))
                print('Your turn is over player %d .' % player_number, end='\n')
                print(cr('your score is %d' % players[0], color='green'), end='\n')
                for i in range(41):
                    time.sleep(0.1)
                    print(cr('\u265F', color='blue'), end='')
                    if i == 40:
                        print('\n')
                        break
                break


def Computer(player_number:int) -> None:
    print('pc turn(player %d).' % player_number, end='\n')
    time.sleep(1)
    print('please wait...', end='\n')
    time.sleep(2)
    while True:
        p2_pc = randint(1, 6)
        if p2_pc != 1:
            print('not one!', end='\n')
            players[1] += p2_pc
            time.sleep(2)
            continue
        else:
            players[1] += 1
            print('The computers turn is over (player %d)' % player_number, end='\n')
            break