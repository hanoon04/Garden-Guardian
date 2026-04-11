#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Caught GardenError") -> None:
        super().__init__(message)


class GardenManager:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun
        self.plants: list[str] = []

    def add_plant(self, name: str) -> None:
        try:
            if not name:
                raise GardenError("Plant name cannot be empty!")
            self.plants.append(name)
            print(f"Added {name} successfully")

        except GardenError as e:
            print(f"Error adding plant: {e}")

    def water_plant(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                if not plant:
                    raise GardenError("can't water empty plant")
                print(f"Watering {plant} - success")

        except GardenError as e:
            print(f"Caught Error watering plants: {e}")

        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        water = self.water
        sun = self.sun
        name = self.name
        try:
            if water > 10:
                raise GardenError(f"Water level {water} is too high (max 10)")
            if water < 1:
                raise GardenError(f"Water level {water} is too low (min 1)")
            if sun < 2:
                raise GardenError(f"Sunlight hours {sun} is too low (min 2)")
            if sun > 12:
                raise GardenError(f"Sunlight hours {sun} is too high (max 12")
            print(f"{name}: healthy (water: {water}, sun: {sun})")

        except GardenError as e:
            print(f"Error checking {name}: {e}")

    def check_tank(self) -> None:
        water = self.water
        try:
            if water < 1:
                raise GardenError("Not enough water in tank")
            print("Tank is full")

        except GardenError as e:
            print(f"Caught GardenError: {e}")

        finally:
            print("System recovered and continuing...")


def test_garden_system() -> None:
    plant1 = GardenManager("tomato", 5, 8)
    plant2 = GardenManager("lettuce", 15, 8)
    plant3 = GardenManager("banana", 0, 8)
    plant4 = GardenManager("", 0, 0)
    print("=== Garden Management System ===")
    print()
    print("Adding plants to garden...")
    plant4.add_plant("tomato")
    plant4.add_plant("lettuce")
    plant4.add_plant("")
    print()
    print("Watering plants...")
    plant4.water_plant()
    print()
    print("Checking plant health...")
    plant1.check_health()
    plant2.check_health()
    print()
    print("Testing error recovery...")
    plant3.check_tank()
    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_system()
