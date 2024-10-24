# IDEA
# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka. 
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. 
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. 
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). 
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

import os
from random import randint
# INTRO
os.system("cls")

class Car:
    speed_unit = 'km/h'
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
# INPUT
# LOGIC
car = Car('ABC-123', 142)
# OUTPUT
print(f"The car {car.registration_number} max speed is {car.max_speed} {car.speed_unit}.")

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")