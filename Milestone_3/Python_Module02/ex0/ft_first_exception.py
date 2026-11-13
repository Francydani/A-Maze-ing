#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    temp_str = "25"
    print(f"Input data is '{temp_str}'")
    try:
        input_temperature(temp_str)
        print(f"Temperature is now {temp_str}ºC")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    temp_str1 = "abc"
    print(f"Input data is '{temp_str1}'")
    try:
        input_temperature(temp_str1)
        print(f"Temperature is now {temp_str1}ºC")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===")
    print()
    test_temperature()


if __name__ == "__main__":
    main()
