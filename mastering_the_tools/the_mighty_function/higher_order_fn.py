from dataclasses import dataclass
from functools import partial
from typing import Callable


@dataclass
class Customer:
    name: str
    age: int


# Higher order function
def send_email_promotion(
    customers: list[Customer],
    is_eligible: Callable[[Customer], bool],
):
    for customer in customers:
        if is_eligible(customer):
            print(f"Sending promotion to {customer.name}")


def is_eligible_for_promotion(customer: Customer, cutoff_age: int = 40) -> bool:
    return customer.age >= cutoff_age


def main() -> None:
    customers = [
        Customer("Alice", 25),
        Customer("Bob", 30),
        Customer("Charlie", 35),
        Customer("David", 40),
        Customer("Eve", 45),
    ]

    # Functools Partial to pass the argument to the function
    is_eligible = partial(is_eligible_for_promotion, cutoff_age=40)
    send_email_promotion(customers, is_eligible)
