from typing import Callable, Iterable

from classes_and_dataclasses.exercises import Customer


def send_email_to_support():
    print("Sending email to support")


def store_analytics():
    print("Storing analytics data")


def update_stock_level():
    print("Updating stock level")


def subscribe_to_newsletter():
    print("Subscribing to newsletter")


PostProcessingFunction = Callable[[int, Customer], None]
PAYMENT_POST_PROCESSOR = [
    send_email_to_support,
    store_analytics,
    update_stock_level,
    subscribe_to_newsletter,
]


def handle_payment_post_processors(
    amount: int, customer: Customer, post_processors: Iterable[PostProcessingFunction]
) -> None:
    for post_processor in post_processors:
        post_processor(amount, customer)
