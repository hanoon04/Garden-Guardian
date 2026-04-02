#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Caught GardenError") -> None:
        super().__init__(message)


class GardenManager:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun

    def add_plant(name: str) -> None:
        try:
            if not name:
                raise GardenError("Plant name cannot be empty!")
            print(f"Added {name} successfully")

        except GardenError as e:
            print(f"Error adding plant: {e}")

    def water_plant(plant_list: list) -> None:
        print("Opening watering system")
        try:
            for plant in plant_list:
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
        except GardenError as e:
            print(f"Error checking {name}: {e}")

        try:
            if water < 1:
                raise GardenError(f"Not enough water in tank")
            print(f"{name}: healthy (water: {water}, sun: {sun})")

        except GardenError as e:
            print(f"Caught GardenError: {e}")

        finally:
            print("System recovered and continuing...")


def test_garden_system() -> None:
    plant1 = GardenManager("tomato", 5, 8)
    plant2 = GardenManager("lettuce", 15, 8)
    plant3 = GardenManager("banana", 0, 8)
    print("=== Garden Management System ===")
    print()
    print("Adding plants to garden...")
    GardenManager.add_plant("tomato")
    GardenManager.add_plant("lettuce")
    GardenManager.add_plant(None)
    print()
    print("Watering plants...")
    GardenManager.water_plant(["tomato", "lettuce"])
    print()
    print("Checking plant health...")
    plant1.check_health()
    plant2.check_health()
    print()
    print("Testing error recovery...")
    plant3.check_health()
    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_system()
