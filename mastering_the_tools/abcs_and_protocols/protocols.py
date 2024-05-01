from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
import math
from typing import Protocol


""" 
-> ABC's notice the type issue when creating the Car and Truck instances.
&
-> Protocols notice the type issue when you start using the class.
"""


class Vehicle(Protocol):
    def reserve(self, start_date: datetime, days: int): ...


class LicenseHolder(Protocol):
    def renew_license(self, date: datetime): ...


@dataclass
class Car:
    model: str
    reserved: bool = False

    def reserve(self, start_date: datetime, days: int):
        self.reserved = True
        print(f"Reserved {self.model} from {start_date} for {days} days")


@dataclass
class Truck:
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

    def renew_license(self, date: datetime):
        print(f"Renewed license for {self.model} at {date}")


def reserve_now(vehicle: Vehicle):
    vehicle.reserve(datetime.now(), 40)


def renew_license_now(holder: LicenseHolder):
    holder.renew_license(datetime.now())


def main():
    car = Car("Toyota")
    truck = Truck("Volvo")

    reserve_now(car)
    reserve_now(truck)
    renew_license_now(truck)


if __name__ == "__main__":
    main()
