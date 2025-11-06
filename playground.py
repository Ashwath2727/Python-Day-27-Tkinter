def add(*args):
    sum = 0

    for num in args:
        sum += num

    return sum


print(add(45,46,23,123, 1, 2, 3, 4))
