# IDEA
# Kysyy käyttäjältä lukuja 
# siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
import os

os.system("cls")

luku= input("Anna luku: ")
min = luku
max = luku
#LOGIC
while luku:
    float(luku)
    if luku < min:
        min = luku
    if luku > max:
        max = luku
    # INPUT
    luku=input("Anna luku: ")

print(f"Pienimmän arvo: {min}")
print(f"Suurimman arvo: {max}")

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")
