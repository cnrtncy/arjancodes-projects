from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
import math


class Vehicle(ABC):
    @abstractmethod
    def reserve(self, start_date: datetime, days: int):
        """Reserve the vehicle for the given number of days"""


@dataclass
class Car(Vehicle):
    model: str
    reserved: bool = False

    def reserve(self, start_date: datetime, days: int):
        self.reserved = True
        print(f"Reserved {self.model} from {start_date} for {days} days")


@dataclass
class Truck(Vehicle):
    model: str
    reserved: bool = False
    reserved_trailer: bool = False

    def reserve(self, start_date: datetime, days: int):
        months = math.ceil(days / 30)
        self.reserved = True
        self.reserved_trailer = True
        print(
            f"Reserved {self.model} for {months} month(s) at date {start_date} with trailer"
        )


def reserve_now(vehicle: Vehicle):
    vehicle.reserve(datetime.now(), 40)


def main():
    car = Car("Toyota")
    truck = Truck("Volvo")

    reserve_now(car)
    reserve_now(truck)


if __name__ == "__main__":
    main()
