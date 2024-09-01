# IDEA
# Kirjoita ohjelma, joka
# Kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
    # (Oikea käyttäjätunnus on python ja salasana rules).
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes
    # Kirjautumistiedot ovat oikein
    # Väärät tiedot on syötetty viisi kertaa.
        # Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.

import os
from random import randint
# INTRO
os.system("cls")
user1 = "python"
pas1 = "rules"
# LOGIC
i=1
while True:
    user = input("Username: ")
    pas = input("Password: ")
    if user != user1 or pas != pas1:
        if i < 5:
            i+=1
            continue
        print("Väärät tiedot on syötetty viisi kertaa.")
        print("Pääsy evätty")
        break
    else:
        print("kirjautumistiedot ovat oikein.")
        print("Tervetuloa")
        break





#EXIT
input("\n\npress ENTER to exit")
os.system("cls")