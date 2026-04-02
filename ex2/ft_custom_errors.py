#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Caught GardenError") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Caught PlantError") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Caught WaterError") -> None:
        super().__init__(message)


def water_tank(tank: int) -> None:
    try:
        if tank < 80:
            raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def plant(name: str, wilt: str) -> None:
    try:
        if wilt == "wilting":
            raise PlantError(f"The {name} plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def garden(name: str, tank: int = 100, wilt: str = "not wilting") -> None:
    try:
        if wilt == "wilting":
            raise GardenError(f"The {name} plant is wilting!")
        if tank < 80:
            raise GardenError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")


def testing() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    plant("tomato", "wilting")
    print()
    print("Testing WaterError...")
    water_tank(60)
    print()
    print("Testing catching all garden errors...")
    garden("tomato", wilt="wilting")
    garden("tomato", tank=55)
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    testing()
