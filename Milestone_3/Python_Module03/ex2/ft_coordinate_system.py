#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            coor = input("Enter new coordinates as floats in format 'x,y,z': ")
            lst = coor.split(",")

            if len(lst) != 3:
                raise ValueError("Invalid syntax")
            else:
                bad_param = lst[0].strip()
                x = float(bad_param)

                bad_param = lst[1].strip()
                y = float(bad_param)

                bad_param = lst[2].strip()
                z = float(bad_param)
                return x, y, z
        except ValueError as e:
            if str(e) == "Invalid syntax":
                print(e)
            else:
                print(f"Error on parameter '{bad_param}': "
                      f"could not convert string to float '{bad_param}'")


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    p1 = get_player_pos()
    dis_origin = math.sqrt(p1[0]**2 + p1[1]**2 + p1[2]**2)
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    print(f"Distance to center: {round(dis_origin, 4)}")
    print()
    print("Get a second set of coordinates")
    p2 = get_player_pos()
    dis_p1_p2 = math.sqrt((p2[0] - p1[0])**2 + (
                          p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(dis_p1_p2, 4)}")


if __name__ == "__main__":
    main()
