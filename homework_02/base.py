from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight: int, fuel: int, fuel_consumption: int):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if self.fuel <= 0:
            raise LowFuelError(f"{self.fuel=}")

        if not self.started:
            self.started = True

    def move(self, distance: int):
        max_distance = self.fuel // self.fuel_consumption if self.fuel_consumption > 0 else 0

        if max_distance < distance:
            raise NotEnoughFuel(f"{self.fuel=}, {self.fuel_consumption=} | {distance=} < {max_distance=}")

        self.fuel -= distance * self.fuel_consumption
