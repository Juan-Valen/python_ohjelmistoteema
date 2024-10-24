# IDEA
# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h). 
# Jos nopeuden muutos on negatiivinen, auto hidastaa. 
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. 
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. 
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. 
# Tulosta tämän jälkeen auton nopeus. 
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. 
# Kuljettua matkaa ei tarvitse vielä päivittää.

from math import exp
import os
from random import randint
# INTRO
os.system("cls")

class Car:
    speed_unit = 'km/h'
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.travelled_distance = 0
    def accelerate(self, velocity):
        expected_velocity = self.speed + velocity;
        if expected_velocity > self.max_speed:
            self.speed = self.max_speed;
        elif expected_velocity < 0:
            self.speed = 0;
        else:
            self.speed = expected_velocity;
# INPUT
accelerations = [30,70,50,-200]
# LOGIC
car = Car('ABC-123', 142)
print(f"The car {car.registration_number} max speed is {car.max_speed} {car.speed_unit}.\n")
for acc in accelerations:
    car.accelerate(acc)
    # OUTPUT
    print(f"The car {car.registration_number} current speed is {car.speed} {car.speed_unit}.")
    

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")