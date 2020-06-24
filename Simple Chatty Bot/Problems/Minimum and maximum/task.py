data = [int(input()), int(input())]
print(data[0] if max(data[0], data[1]) == data[0] else data[1])
print(data[0] if min(data[0], data[1]) == data[0] else data[1])
