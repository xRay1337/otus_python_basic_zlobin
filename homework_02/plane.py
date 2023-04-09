"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int
    engine: Engine

    def __init__(self, weight: int, fuel: int, fuel_consumption: int, max_cargo: int):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def set_engine(self, engine: Engine):
        self.engine = engine

    def load_cargo(self, cargo: int):
        if self.cargo + cargo > self.max_cargo:
            raise CargoOverload

        self.cargo += cargo

    def remove_all_cargo(self) -> int:
        cargo = self.cargo
        self.cargo = 0
        return cargo
