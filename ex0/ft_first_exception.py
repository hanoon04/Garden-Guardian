#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)

    except Exception:
        print(f"Error: ’{temp_str}’ is not a valid number")
        return 0

    try:
        if temp > 40:
            raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
        if temp < 0:
            raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp

    except Exception as e:
        print("Error: ", e)
        return 0


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    print("Testing temperature: 25")
    check_temperature("25")
    print()
    print("Testing temperature: abc")
    check_temperature("abc")
    print()
    print("Testing temperature: 100")
    check_temperature("100")
    print()
    print("Testing temperature: -50")
    check_temperature("-50")
    print()
    print("All tests completed - program didn’t crash!")


if __name__ == "__main__":
    test_temperature_input()
