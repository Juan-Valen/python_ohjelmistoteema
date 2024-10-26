# IDEA
# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen. 
# Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

import os
from random import randint
from typing import List
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
class Building:
    def __init__(self, bottom: int, top: int, elevators: int):
        self.elevators: List[Elevator] = []
        print(f"Starting constructions")
        print(f"Starting installation of elevators")
        for n in range(elevators):
            self.elevators.append(Elevator(bottom, top))
        print(f"Max elevators: {len(self.elevators)}")

    def run_elevator(self, elevator: int, floor: int):
        if elevator < 1 or elevator > len(self.elevators):
            return
        print(f"Elevator {elevator} moving.")
        self.elevators[elevator-1].go_to_floor(floor)
    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.floor_bottom)

# INPUT
# LOGIC
b = Building(2, 5, 5)

b.run_elevator(1,2)
b.run_elevator(2,3)
b.run_elevator(3,5)
b.run_elevator(4,5)
b.run_elevator(5,4)
b.fire_alarm()
# OUTPUT

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")