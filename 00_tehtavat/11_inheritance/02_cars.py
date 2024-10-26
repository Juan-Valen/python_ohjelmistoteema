# IDEA
# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. 
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. 
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina. 
# Kirjoita aliluokille alustajat. 
# Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. 
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. 
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). 
# Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

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

    def print_information(self):
        print(f"Car: {self.registration_number}")
        print(f"Max speed: {self.max_speed} {self.speed_unit}")
        print(f"Speed: {self.speed} {self.speed_unit}")
        print(f"Travelled distance: {self.travelled_distance} km")

class ElectricCar(Car):
    battery_unit = "kWh"

    def __init__(self, registration_number, max_speed, battery_capacity: int):
        self.battery_capacity = battery_capacity
        super().__init__(registration_number, max_speed)
        
    def print_information(self):
        super().print_information()
        print(f"Battery capacity: {self.battery_capacity} {self.battery_unit}")

class GasolineCar(Car):
    gasoline_unit = "ltr"
    
    def __init__(self, registration_number, max_speed, gasoline_capacity: int):
        self.gasoline_capacity = gasoline_capacity
        super().__init__(registration_number, max_speed)
        
    def print_information(self):
        super().print_information()
        print(f"Ganoline capacity: {self.gasoline_capacity} {self.gasoline_unit}\n")
# INPUT
# LOGIC
electric_car = ElectricCar(f'ABC-15', randint(100,200), randint(100,200))
gasoline_car = GasolineCar(f'ABC-123', randint(100,200), randint(100,200))
for n in range(3):
    electric_car.accelerate(randint(-10,40))
    gasoline_car.accelerate(randint(-10,40))
    electric_car.drive(1)
    gasoline_car.drive(1)
# OUTPUT
electric_car.accelerate(-200)
gasoline_car.accelerate(-200)
electric_car.print_information()
print()
gasoline_car.print_information()
#EXIT
input("\n\npress ENTER to exit")
os.system("cls")