# IDEA
# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon. 
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa. 
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. 
# Käytä joukkotietorakennetta nimien tallentamiseen.

import os
from random import randint
# INTRO
os.system("cls")
names = []
while True:
    # INPUT
    nimi = input("Anna nimi: ")
    # LOGIC
    if not nimi:
        break
    if nimi in names:
        print(nimi)
    else:
        print("Uusi nimi")
    names.append(nimi)
# OUTPUT
os.system("cls")
for name in names:
    print(name)
#EXIT
input("\n\npress ENTER to exit")
os.system("cls")