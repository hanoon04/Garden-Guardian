#!/usr/bin/env python3

def check_plant_health(name: str, water_level: int, sun_hours: int) -> None:
    try:
        if not name:
            raise ValueError("Plant name cannot be empty!")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if sun_hours < 2:
            raise ValueError(f"Sunlight hours {sun_hours} is too low (min 2)")
        if sun_hours > 12:
            raise ValueError(f"Sunlight hours {sun_hours} is too heigh (max 12")
        print(f"Plant ’{name}’ is healthy!")

    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print()
    print("Testing good values...")
    check_plant_health("tomato", 5, 10)
    print()
    print("Testing empty plant name...")
    check_plant_health("", 5, 10)
    print()
    print("Testing bad water level...")
    check_plant_health("tomato", 15, 10)
    print()
    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 5, 0)
    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
