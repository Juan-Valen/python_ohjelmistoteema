# IDEA
# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina. 
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. 
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta). 
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

from math import pi
import os
from random import randint
# FUNCTIONS
def pizza_unit_price(length: float, price: float):
    radius = length/2
    area = radius*radius*pi
    return price/area
# INTRO
os.system("cls")
print(f"This program will ask you for the price and length of 2 pizzas and then the program will tell you which one has a better price.\n\n")

input("\n\npress ENTER to continue")
os.system("cls")
print(f"This program will ask you for the price and length of 2 pizzas and then the program will tell you which one has a better price.\n\n")
# LOGIC

pizzas = {"pizza 1": { "length": "", "price": "", "unit_price": 0},"pizza 2": { "length": "", "price": "", "unit_price": 0}}

for pizza in pizzas:
    os.system("cls")
    print(f"This program will ask you for the price and length of 2 pizzas and then the program will tell you which one has a better price.\n\n")
    while pizzas[pizza]["length"] == "":
        # INPUT
        pizzas[pizza]["length"] = input(f"\n\nProvide the length of {pizza}: ")
        
    while pizzas[pizza]["price"] == "":
        # INPUT
        pizzas[pizza]["price"] = input(f"\n\nProvide the price of {pizza}: ")
    pizzas[pizza]["unit_price"] = pizza_unit_price(float(pizzas[pizza]["length"]),float(pizzas[pizza]["price"]))

    

# OUTPUT
os.system("cls")
if pizzas["pizza 1"]["unit_price"] < pizzas["pizza 2"]["unit_price"]:
    print("pizza 1 has a better unit price than pizza 2")
elif pizzas["pizza 2"]["unit_price"] < pizzas["pizza 1"]["unit_price"]:
    print("pizza 2 has a better price than pizza 1")
else:
    print("pizza 1 and pizza 2 have the same unit price")

print("\n\n")

for pizza in pizzas:
    print("%s %.2f €/m2" % (pizza,pizzas[pizza]["unit_price"]))

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")