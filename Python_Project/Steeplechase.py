"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    for i in range(11):
        if front_is_clear():
           move()
        else:
            jump()
            turn_left()

def jump():
    up()
    cross()
    down()

def up():
    turn_left()
    while not right_is_clear():
        move()

def cross():
    turn_right()
    move()
    turn_right()

def turn_right():
        turn_left()
        turn_left()
        turn_left()

def down():
    while front_is_clear():
        move()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
