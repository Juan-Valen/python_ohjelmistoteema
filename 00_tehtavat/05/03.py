# IDEA


# Kirjoita ohjelma, joka 
# kysyy käyttäjältä kokonaisluvun ja 
# ilmoittaa, onko se alkuluku. 
    # Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

    # Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
    # Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.



import os
from random import randint
# INTRO
os.system("cls")
# INPUT
n = input("Provide a number: ")
isprime = False
# LOGIC
while n:
    if int(n) in [2, 3, 5, 7]:
        isprime = True
    if (not(int(n) % 2 == 0 or int(n) % 3 == 0 or int(n) % 5 == 0 or int(n) % 7 == 0)):
        isprime = True
    if isprime:
        print(f"The number {n} is a prime number.")
        isprime = False
    n = input("Provide a number: ")

# OUTPUT

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")