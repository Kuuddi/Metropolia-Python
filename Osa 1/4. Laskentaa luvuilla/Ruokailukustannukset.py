amount = int(input("Montako kertaa viikossa syöt unicafessa? "))
price = float(input("Unicafe-lounaan hinta? "))
groceries = float(input("Paljonko käytät viikossa ruokaostoksiin? "))

total = amount * price + groceries
daily = total / 7

print("Kustannukset keskimäärin: ")
print(f"Päivässä {daily}")
print(f"Viikossa {total}")
