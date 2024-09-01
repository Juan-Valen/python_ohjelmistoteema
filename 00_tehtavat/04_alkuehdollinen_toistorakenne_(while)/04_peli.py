# IDEA
# Kirjoita peli, 
# Jossa tietokone arpoo kokonaisluvun väliltä 1..10. 
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. 
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin 
    # Liian suuri arvaus
    # Liian pieni arvaus
    # Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.


import os
from random import randint

os.system("cls")
print("Anna numero 1..10 väliltä: ")
arpoo_arvo = randint(1,10)
arvaus: int = int(input("Anna luku: "))
#LOGIC
while True:
    if arvaus < arpoo_arvo:
        print("Liian pieni arvaus")
    elif arvaus > arpoo_arvo:
        print("Liian suuri arvaus")
    else:
        print("Oikein")
        break
    # INPUT
    arvaus: int = int(input("Anna luku: "))


#EXIT
input("\n\npress ENTER to exit")
os.system("cls")