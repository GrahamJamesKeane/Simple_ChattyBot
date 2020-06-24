data = [int(input()), int(input()), int(input())]
if data[0] < data[2] < data[1]:
    print("Normal")
elif data[2] < data[0]:
    print("Deficiency")
else:
    print("Excess")
