"""
File: DoubleBeepers.py
Name:
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    move()
    double_beepers()
    put_beepers_back()
    karel_goes_home()
    move()
    turn_around()

def put_beepers_back():
    move()
    while on_beeper():
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        turn_around()
        move()

def double_beepers():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()
        turn_around()

def turn_around():
    for i in range(2):
        turn_left()

def karel_goes_home():
    turn_around()
    move()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
