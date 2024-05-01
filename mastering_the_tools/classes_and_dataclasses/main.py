from dataclasses import dataclass, field
import random
import string
from datetime import datetime
from enum import Enum, auto


def generate_vehicle_license() -> str:
    """Helper function to generate a random vehicle license"""

    digit_part = "".join(random.choices(string.digits, k=2))
    letter_part_1 = "".join(random.choices(string.ascii_uppercase, k=2))
    letter_part_2 = "".join(random.choices(string.ascii_uppercase, k=2))
    return f"{letter_part_1}-{digit_part}-{letter_part_2}"


class Accessory(Enum):
    AIRCO = auto()
    CRUISECONTROL = auto()
    NAVIGATION = auto()
    OPENROOF = auto()
    BATHTUB = auto()
    MINIBAR = auto()


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


def default_accessories() -> list[Accessory]:
    return [Accessory.AIRCO, Accessory.NAVIGATION]


@dataclass
class Vehicle:  # (frozen=True) # To make the object immutable, but it will not work with __post_init__, add default_factory to the field
    brand: str
    model: str
    color: str
    # licence_plate: str = field(default_factory=generate_vehicle_license, init=False)

    # Disable init and add __post_init__ to set the licence_plate due to the brand
    licence_plate: str = field(init=False)
    accessories: list[Accessory] = field(
        default_factory=default_accessories
    )  # To avoid mutable default arguments
    fuel_type: FuelType = FuelType.PETROL

    def __post_init__(self):
        self.licence_plate = generate_vehicle_license()
        if self.brand == "Tesla":
            self.licence_plate += "-T"

    def reserve(self, date: datetime) -> None:
        print(f"Vehicle {self.licence_plate} reserved for {date}")


def main() -> None:
    """Create a vehicle object and reserve it"""

    tesla = Vehicle(
        brand="Tesla",
        model="Model S",
        color="Red",
        # licence_plate=generate_vehicle_license(),
        accessories=[Accessory.AIRCO, Accessory.NAVIGATION],
        fuel_type=FuelType.ELECTRIC,
    )

    volkswagen = Vehicle(
        brand="Volkswagen",
        model="Golf",
        color="Blue",
        # licence_plate=generate_vehicle_license(),
        # accessories=[Accessory.AIRCO, Accessory.CRUISECONTROL],
        fuel_type=FuelType.PETROL,
    )

    bmw = Vehicle(
        brand="BMW",
        model="X5",
        color="Black",
        # licence_plate=generate_vehicle_license(),
        accessories=[Accessory.AIRCO, Accessory.OPENROOF],
        fuel_type=FuelType.DIESEL,
    )

    print(tesla)
    print(volkswagen)
    print(bmw)

    tesla.reserve(datetime.now())


if __name__ == "__main__":
    main()
