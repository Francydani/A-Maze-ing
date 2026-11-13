#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    val = int(temp_str)
    if val < 0:
        raise ValueError(f"{val}°C is too cold for plants (min 0°C)")
    elif val > 40:
        raise ValueError(f"{val}°C is too hot for plants (max 40°C)")
    return val


def test_temperature() -> None:
    temp_str = "25"
    print(f"Input data is '{temp_str}'")
    try:
        input_temperature(temp_str)
        print(f"Temperature is now {temp_str}°C")
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
    temp_str2 = "100"
    print(f"Input data is '{temp_str2}'")
    try:
        input_temperature(temp_str2)
        print(f"Temperature is now {temp_str2}ºC")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    temp_str3 = "-50"
    print(f"Input data is '{temp_str3}'")
    try:
        input_temperature(temp_str3)
        print(f"Temperature is now {temp_str3}ºC")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature()


if __name__ == "__main__":
    main()
