def add(x, y):
    return x + y


print(add(5, 7))


lab_add = lambda x, y: x + y

print(lab_add(5, 7))


def double(x):
    return x * 2


sequence = [1, 3, 5, 7]
doubled = [double(x) for x in sequence]
print(doubled)


doubled_map = map(double, sequence)

doubled_map = map(lambda x: x * 2, sequence)
print(doubled_map)

doubled_map = list(map(lambda x: x * 2, sequence))
print(doubled_map)
