# IDEA
# Muokkaa edellistä funktiota siten, 
    # että funktio saa parametrinaan nopan tahkojen yhteismäärän. 
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. 
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa 
    # kunnes saadaan nopan maksimisilmäluku, 
    # joka kysytään käyttäjältä ohjelman suorituksen alussa.

import os
from random import randint
from time import sleep
# INTRO
os.system("cls")
# INPUT
faces = int(input("Provide the amount of faces on the dice: "))
# LOGIC
def noppaa(faces: int):
    return randint(1,faces)

print(f"\n\nI will start throwing a dice until it lands on {faces}.\n\n")

result = noppaa(faces)
while result != faces:
    print(f"the result was {result}\n")
    sleep(randint(90,110)/100)
    print(f"lets try again!")
    sleep(randint(10,200)/100)
    result = noppaa(faces)



# OUTPUT
print(f"Great! I finally got a {faces}!")

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")