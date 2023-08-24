import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
from algorithm import *
from workfile import *
n = 2
while True:
    clear()
    print_instructions()
    choose(input("Input command "))
    input("Press Enter ")
