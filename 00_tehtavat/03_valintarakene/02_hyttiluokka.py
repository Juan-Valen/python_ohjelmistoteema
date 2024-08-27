
# kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
# tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
# Tehtävässä on käytettävä if/elif/else-toistorakennetta.
#     LUX on parvekkeellinen hytti yläkannella.
#     A on ikkunallinen hytti autokannen yläpuolella.
#     B on ikkunaton hytti autokannen yläpuolella.
#     C on ikkunaton hytti autokannen alapuolella.

# Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

import os


os.system("cls")
#INPUT
hyttiluokka = input("Anna laivan hyttiluokan (LUX, A, B, tai C): ")

#LOGIC
if hyttiluokka == "LUX":
    print("\nLUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("\nA on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("\nB on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("\nC on ikkunaton hytti autokannen alapuolella.")
else:
    print("\nVirheellinen hyttiluokka.")

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")