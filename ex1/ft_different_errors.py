#!/usr/bin/env python3

def garden_operations() -> None:
    """ValueError"""
    try:
        print("Testing ValueError...")
        int("abc")

    except ValueError:
        print("Caught ValueError: invalid literal for int()")
        print()

    """ZeroDivisionError"""
    try:
        print("Testing ZeroDivisionError..")
        10 / 0

    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
        print()

    """FileNotFoundError"""
    try:
        print("Testing FileNotFoundError...")
        open("file.txt")

    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file ’missing.txt’")
        print()

    """KeyError"""
    try:
        print("Testing KeyError...")
        plant = {"name": "Rose", "color": "red"}
        print(plant["id"])

    except KeyError:
        print("Caught KeyError: ’missing_plant’")
        print()


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print()
    garden_operations()
    print("Testing multiple errors together...")
    try:
        10/0
        open("haneen.txt")
    except (FileNotFoundError, ZeroDivisionError):
        print("Caught an error, but program continues!")
        print()

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
