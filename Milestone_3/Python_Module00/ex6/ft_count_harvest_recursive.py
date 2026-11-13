def recursive(i, size):
    if i > size:
        return
    print("Day", i)
    recursive(i + 1, size)


def ft_count_harvest_recursive():
    data = (int(input("Days until harvest: ")))
    recursive(1, data)
    print("Harvest time!")
