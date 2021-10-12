x_locations, y_locations = [], []
for _ in range(3):
    x, y = map(int, input().split())
    if x in x_locations:
        x_locations.remove(x)
    else:
        x_locations.append(x)
    if y in y_locations:
        y_locations.remove(y)
    else:
        y_locations.append(y)

print(x_locations[0], y_locations[0])
