# IDEA
# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut. 
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

import os
from random import randint
from time import sleep



# FUNCTIONS
def search_even(numbers: list[int]):
    evens = []
    for i in numbers:
        if i % 2 == 0:
            evens.append(i)
    return evens
# INTRO
os.system("cls")
print(f"This program will generate a list of numbers with random length and content. After the program REMOVE the odd numbers of the list and show you both lists.\n\n")

input("\n\npress ENTER to continue")
os.system("cls")
print(f"This program will generate a list of numbers with random length and content. After the program REMOVE the odd numbers of the list and show you both lists.\n\n")
# INPUT
# LOGIC
nums = []

for i in range(randint(5,15)):
    number = randint(1,10)
    nums.append(number)
    print(f"The number {number} was added to the list\n")
    sleep(randint(10,200)/100)

# OUTPUT
print(f"List: {nums}")
print(f"List without odd numbers: {search_even(nums)}")
#EXIT
input("\n\npress ENTER to exit")
os.system("cls")