# Kirjoita ratkaisu tähän

number1 = int(input("Luku 1: "))
number2 = int(input("Luku 2: "))
cmd = input("Komento: ")

if cmd == "summa":
    sum = number1 + number2
    print(f"{number1} + {number2} = {sum} ")

elif cmd == "erotus":
    sum = number1 - number2
    print(f"{number1} - {number2} = {sum} ")

elif cmd == "tulo":
    sum = number1 * number2
    print(f"{number1} * {number2} = {sum}")