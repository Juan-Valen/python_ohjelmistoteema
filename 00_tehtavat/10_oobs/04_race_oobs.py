# IDEA
# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. 
# Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista. 
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. 
# Luokassa on seuraavat metodit:

#     tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
#     tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
#     kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". 
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. 
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. 
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.


from math import exp
import os
from random import randint
import time
from typing import List
# INTRO
os.system("cls")

class Car:
    speed_unit = 'km/h'
    def __init__(self, registration_number, max_speed: int):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.travelled_distance = 0

    def accelerate(self, velocity: int):
        expected_velocity = self.speed + velocity;
        if expected_velocity > self.max_speed:
            self.speed = self.max_speed;
        elif expected_velocity < 0:
            self.speed = 0;
        else:
            self.speed = expected_velocity;
    
    def drive(self, hours: int):
        self.travelled_distance += self.speed*hours

class Race:
    def __init__(self, name, distance: int, cars: List[Car]):
        self.name = name
        self.distance = distance
        self.cars: List[Car] = cars
        self.elapsetime = 0
    
    def hour_passes(self):
        for c in cars:
            c.accelerate(randint(-10,15))
            c.drive(1)
            self.elapsetime += 1

    def print_status(self):
        print(self.name)
        print(f"Time elapsed: {self.elapsetime} hours\n")
        row_format = "|{0.registration_number:<10}|{0.max_speed:<18}|{0.speed:<15}|{0.travelled_distance:<15}|"
        title_format = " {0:<10} {1:<18} {2:<15} {3:<15} "
        print(title_format.format("CAR", "MAX-SPEED (km/h)", "SPEED (km/h)", "DISTANCE (km)"))
        for car in cars:
            print(row_format.format(car))

    def race_finished(self):
        for car in cars:
            if self.distance < car.travelled_distance:
                return True
        return False
            




# INPUT
cars= []
for i in range(1,11):
    cars.append(Car(f'ABC-{i}', randint(100,200)))
race = Race("Grand Demolition Derby", 8000, cars)
while not race.race_finished():
    # # LOGIC
    race.hour_passes()
    # # OUTPUT
    if race.elapsetime % 10 == 0:
        race.print_status()
    time.sleep(1.5)
    os.system("cls")
# OUTPUT
race.print_status()

print("\nThe race has ended!\n")
# print(f"The car {winner.registration_number} got first to the finnish line.\n")
# for c in cars:
#     print(f"Car: {c.registration_number}, Max speed: {c.max_speed} {c.speed_unit}, Total Distance traveled: {c.travelled_distance} km.")
#EXIT
input("\n\npress ENTER to exit")
os.system("cls")