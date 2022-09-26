import math

amount = int(input("Montako opiskelijaa? "))
size = int(input("Mikä on ryhmän koko? "))

if amount % size != 0:
    rounded = math.ceil(amount / size)
    print(f"Ryhmien määrä: {rounded}")

else:
    print(f"Ryhmien määrä: {size / 2}")