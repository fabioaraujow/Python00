def recursive_counter(i, days):
    if i > days:
        return
    print(f"Day {i}")
    recursive_counter(i + 1, days)


def ft_count_harvest_recursive():
    i = 1
    days = int(input("Days until harvest: "))
    recursive_counter(i, days)
    print("Harvest time!")
