from dataclasses import dataclass, field
from datetime import datetime

from enum import Enum
import random
import string

""" 
EXERCISE 1 -> Convert the following classes into dataclasses such that the initializers that the dataclass generates have the same behavior as the regular class:

class A:
  def __init__(self) -> None:
    self._length = 0

class B:
  def __init__(self, x: int, y: str = "hello", l: list[int] | None = None) -> None:
    self.x = x
    self.y = y
    self.l = [] if not l else l

class C:
  def __init__(self, a: int = 3) -> None:
    self.a = a
    self.b = a + 3
"""


""" 
EXERCISE 2 -> The mobile phone company PhonyPhones needs to create a system for managing their customers' phone plans 
and they need to get better insight into the data that they need to store. 
Because their CEO knows a bit of Python, he asks you to write a few dataclasses representing the data structure of their application. 
In short, they have customers (name, address, email address), phones (brand, model, price, serial number) and plans (which refer to a customer, 
a phone, a start date, the total number of months in the contract, 
a monthly price, and whether the phone is included in the contract).
Write dataclasses that can represent this data. You may take some freedom in how things like addresses etc. are represented.
"""


# EXERCISE 1
@dataclass
class A:
    length: int = 0


@dataclass
class B:
    x: int
    y: str = "hello"
    l: list[int] = field(default_factory=list)


@dataclass
class C:
    a: int = 3
    b: int = field(init=False)

    def __post_init__(self):
        self.b = self.a + 3


# EXERCISE 2


def generate_serial_number(brand: str, model: str) -> str:
    digits = "".join(random.choices(string.digits, k=8))
    return f"{brand[0]}-{model[0:3]}-{digits}"


@dataclass
class Address:
    street: str
    number: int
    city: str
    postal_code: str

    def __str__(self) -> str:
        return f"{self.street} {self.number}, {self.city} {self.postal_code}"


class Brand(Enum):
    APPLE = "Apple"
    SAMSUNG = "Samsung"
    GOOGLE = "Google"
    HUAWEI = "Huawei"
    XIAOMI = "Xiaomi"
    MOTOROLA = "Motorola"


class Contract(Enum):
    MINIMUM = 6
    MEDIUM = 12
    MAXIMUM = 24


@dataclass
class Customer:
    name: str
    address: Address
    email: str


@dataclass
class Phone:
    brand: Brand
    model: str
    price: float
    serial_number: str = field(init=False)

    def __post_init__(self):
        self.serial_number = generate_serial_number(self.brand.value, self.model)


@dataclass
class Plan:
    customer: Customer
    phone: Phone
    monthly_price: float
    phone_included: bool = True
    start_date: datetime = datetime.now()
    total_months: Contract = Contract.MEDIUM

    def total_price(self) -> float:
        return self.monthly_price * self.total_months.value


def main() -> None:
    customer_1 = Customer(
        name="John Doe",
        address=Address(
            street="Main Street",
            number=123,
            city="New York",
            postal_code="10001",
        ),
        email="johndoe@example.com",
    )

    plan = Plan(
        customer=customer_1,
        phone=Phone(brand=Brand.APPLE, model="iPhone 12", price=999.99),
        monthly_price=49.99,
        phone_included=True,
        total_months=Contract.MEDIUM,
    )

    print(plan)
    print(plan.total_price())
    print(plan.phone.serial_number)


if __name__ == "__main__":
    main()
