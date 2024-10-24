# IDEA
# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. 
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. 
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. 
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

from math import exp
import os
from random import randint
import time
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
    def drive(self, hours):
        self.travelled_distance += self.speed*hours

# INPUT
accelerations = [{'velocity': 30, 'time': 1},{'velocity':70, 'time': 1},{'velocity':50, 'time': 1},{'velocity':-200, 'time': 1}]
# LOGIC
car = Car('ABC-123', 142)
print(f"The car {car.registration_number} max speed is {car.max_speed} {car.speed_unit}.")
print(f'Total traveled distance: {car.travelled_distance}\n')
for acc in accelerations:
    car.accelerate(acc['velocity'])
    car.drive(acc['time'])
    # OUTPUT
    print(f"The car {car.registration_number} current speed is {car.speed} {car.speed_unit} and it will travel for {acc['time']} hours.")
    print(f'Total traveled distance: {car.travelled_distance}')
    

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")