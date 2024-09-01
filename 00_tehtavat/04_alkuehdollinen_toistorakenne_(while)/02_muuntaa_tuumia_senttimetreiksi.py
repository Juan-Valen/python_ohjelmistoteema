# IDEA
# Kirjoita ohjelma, 
# joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. 
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

import os

os.system("cls")
inches: float = float(input("Anna tuumamäärä: "))
#LOGIC
while inches>=0:
    if inches >= 0:
        print(f"{inches*2.54}cm")
    # INPUT
    inches=float(input("Anna tuumamäärä: "))

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")



