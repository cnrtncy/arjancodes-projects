from typing import Callable


int_function = Callable[[int, int], int]
float_function = Callable[[int], float]


def multiply_by_two(x: int) -> float:
    return x * 2.0


def add_three(x: int, y: int) -> int:
    return x * y + 3


def main() -> None:
    """If multiply function is assigned to my_var, there will be a type error,
    but still runs the code. You have to create another callable type to avoid
    """
    my_var: int_function = add_three
    print(my_var(5, 3))


if __name__ == "__main__":
    main()
