# IDEA
# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. 
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. 
# Uusi hissi on aina alimmassa kerroksessa. 
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen. 
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. 
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

import os
from random import randint
# INTRO
os.system("cls")
class Elevator:
    def __init__(self, bottom: int, top: int):
        self.floor_bottom = -bottom
        self.floor_top = top
        self.current_floor = -bottom
        print('Elevator has been configurate.')
        print('Starting program.')
        print(f'current floor is {self.current_floor}')

    def go_to_floor(self, floor: int):
        if floor < self.floor_bottom or floor > self.floor_top:
            return
        print(f'Current floor is {self.current_floor}')
        while floor != self.current_floor:
            if floor > self.current_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        prospect_floor = self.current_floor+1
        if prospect_floor > self.floor_top:
            return
        self.current_floor = prospect_floor
        print(f'current floor is {prospect_floor}')
        
    def floor_down(self):
        prospect_floor = self.current_floor-1
        if prospect_floor < self.floor_bottom:
            return
        self.current_floor = prospect_floor
        print(f'current floor is {prospect_floor}')

# INPUT
# LOGIC
h = Elevator(2,5)

h.go_to_floor(4)
h.go_to_floor(-2)
# OUTPUT

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")