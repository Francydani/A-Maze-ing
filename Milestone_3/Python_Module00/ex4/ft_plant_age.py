def ft_plant_age():
    data = int(input("Enter plant age in days: "))
    if data > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
