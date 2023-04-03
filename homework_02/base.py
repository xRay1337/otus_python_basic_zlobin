from abc import ABC
import exceptions


class Vehicle(ABC):

    def __init__(self, weight: int = 0, fuel: int = 0, fuel_consumption: int = 0):
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel <= 0:
            raise exceptions.LowFuelError

        self.started = True

    def move(self, distance: int):
        max_distance = self.fuel // self.fuel_consumption if self.fuel_consumption > 0 else 0

        if max_distance < distance:
            raise exceptions.NotEnoughFuel

        self.fuel -= distance * self.fuel_consumption
