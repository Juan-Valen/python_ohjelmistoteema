# IDEA
# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, 
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). 
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. 
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

import os
from random import randint
# INTRO
os.system("cls")
# INPUT
kuukausi = int(input("Anna kuukausi numerona (esim. 1, 2): "))
# LOGIC
vuodenaika = ("talvi","kevät", "kesä", "syksy")
# OUTPUT
if kuukausi in (12,1,2):
    print(vuodenaika[0])
elif kuukausi in (3,4,5):
    print(vuodenaika[1])
elif kuukausi in (6,7,8):
    print(vuodenaika[2])
elif kuukausi in (9,10,11):
    print(vuodenaika[3])


#EXIT
input("\n\npress ENTER to exit")
os.system("cls")