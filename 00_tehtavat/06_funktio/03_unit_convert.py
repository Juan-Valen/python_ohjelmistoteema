# IDEA
# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän. 
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. 
# Muuntamista jatketaan siihen saakka, 
    # kunnes käyttäjä syöttää negatiivisen gallonamäärän.

    # Yksi gallona on 3,785 litraa.


import os
from random import randint
# INTRO
os.system("cls")
def gallons_to_liters(gallons: float):
    return gallons * 3.785
print("This program will convert gallons to liters\n\n")
# INPUT
gallons = input("Provide an amount in gallons: ")
# LOGIC
while ((gallons) and (float(gallons) >= 0)):
    print(f"\n\n{gallons} gallons equals to {gallons_to_liters(float(gallons))} liters\n\n")
    gallons = input("Provide an amountin gallons: ")

# OUTPUT

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")