# IDEA
# Kirjoita ohjelma, joka 
# kysyy käyttäjältä arpakuutioiden lukumäärän. 
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. 
    # Käytä for-toistorakennetta.

import os
from random import randint
# INTRO
os.system("cls")
# INPUT
n = int(input("Provide the ammount of dice to throw: "))
# LOGIC
for x in range(n):
    print(f"dice {x+1}: {randint(1,6)}")
# OUTPUT

#EXIT
input("\n\npress ENTER to exit")    
os.system("cls")