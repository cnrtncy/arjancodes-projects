from enum import Enum


class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

    def __str__(self) -> str:
        return self.name.title()


def is_birthday(month: Month) -> bool:
    return month == Month.JULY


def main() -> None:
    print(is_birthday(Month.JULY))
    print(Month.JULY)


if __name__ == "__main__":
    main()
