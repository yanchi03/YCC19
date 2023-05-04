"""
File: PotholeFilling.py
Name: Yan Chen
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()


def go_in():
    move()
    turn_right()
    move()

def go_out():
    turn_around()
    move()
    turn_right()
    move()

def put_99_beepers():
    for i in range(99):
        put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()







# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
