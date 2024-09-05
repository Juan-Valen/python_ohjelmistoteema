# IDEA


# Kirjoita ohjelma, joka 
# kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. 
    # Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.


import os
from random import randint
# INTRO
os.system("cls")
# INPUT
n = input("Provide a number: ")
l = []
# LOGIC
while n:
    l.append(int(n))
    n = input("Provide a number: ")
l.sort(reverse=True)
i=0
while i < 5:
    print(l[i])
    i+=1
    

# OUTPUT

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")