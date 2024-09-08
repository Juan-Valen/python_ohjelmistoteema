# IDEA
# Kirjoita parametriton funktio, 
    # joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. 
# Kirjoita pääohjelma, 
    # joka heittää noppaa niin kauan kunnes tulee kuutonen. 
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import os
from random import randint
from time import sleep
# INTRO
os.system("cls")
print("I will start throwing a dice until it lands on 6.\n\n")

# INPUT
# LOGIC
def noppaa():
    return randint(1,6)
result = noppaa()
while result != 6:
    print(f"the result was {result}\n")
    sleep(randint(90,110)/100)
    print(f"lets try again!")
    sleep(randint(10,200)/100)
    result = noppaa()



# OUTPUT
print(f"Great! I finally got a SIX!")
# for i in range(100):
#     print(noppaa())

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")