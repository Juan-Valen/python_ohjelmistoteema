# IDEA
# Nyt ohjelmoidaan autokilpailu. 
# Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. 
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. 
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. 
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. 
# Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

#     Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
#     Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.

# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. 
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

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
cars= []
for i in range(1,11):
    cars.append(Car(f'ABC-{i}', randint(100,200)))
winner = Car('ABC-1',0)

# LOGIC
total_time = 0
timelapse = 10
while winner.travelled_distance < 10000:
    # LOGIC
    total_time += timelapse
    # OUTPUT
    print(f'\nTotal time: {total_time:.2f} hours \n')
    for c in cars:
        c.accelerate(randint(-10,15))
        c.drive(timelapse)
        # OUTPUT
        print(f"The car {c.registration_number} current speed is {c.speed} {c.speed_unit} and it will travel for {timelapse} hours.")
        print(f'Total traveled distance: {c.travelled_distance:.2f}')
        if winner.travelled_distance < c.travelled_distance:
            winner = c
    time.sleep(1.5)
    os.system("cls")
# OUTPUT
print(f"The car {winner.registration_number} got first to the finnish line.\n")
for c in cars:
    print(f"Car: {c.registration_number}, Max speed: {c.max_speed} {c.speed_unit}, Total Distance traveled: {c.travelled_distance} km.")
#EXIT
input("\n\npress ENTER to exit")
os.system("cls")