# IDEA
# Kirjoita ohjelma, joka 
# kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen) ja 
# tallentaa ne listarakenteeseen. 
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin. 
    # käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.


import os
from random import randint
# INTRO
os.system("cls")
# LOGIC
cities = {"city 1": "","city 2": "","city 3": "","city 4": "","city 5": ""}

for city in cities:
    while cities[city] == "":
        # INPUT
        os.system("cls")
        cities[city] = input(f"Provide {city} a name: ")
        
# OUTPUT
os.system("cls")
for city in cities:
    print(f"{city} name is {cities[city]}")
# EXIT
input("\n\npress ENTER to exit")

os.system("cls")