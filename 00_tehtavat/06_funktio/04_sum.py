# IDEA
# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
# Ohjelma palauttaa listassa olevien lukujen summan. 
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.



import os
from random import randint
from time import sleep




# FUNCTIONS
def sum(numbers: list[int]):
    sum: int = 0
    for integer in numbers:
        sum += integer
    return sum
# INTRO
os.system("cls")
print(f"This program will generate a list of numbers with random length and content. After the program will calculate the sum of every number in the list.\n\n")

input("\n\npress ENTER to continue")
os.system("cls")
print(f"This program will generate a list of numbers with random length and content. After the program will calculate the sum of every number in the list.\n\n")
# INPUT
# LOGIC
nums = [0]

for i in range(randint(5,15)):
    number = randint(1,10)
    nums.append(number)
    print(f"The number {number} was added to the list\n")
    sleep(randint(10,200)/100)

# OUTPUT
print(f"the sum of these numbers is {sum(nums)}")
# EXIT
input("\n\npress ENTER to exit")
os.system("cls")