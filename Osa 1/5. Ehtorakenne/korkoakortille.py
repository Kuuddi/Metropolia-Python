pisteet = int(input("Kuinka paljon pisteitä? "))

if pisteet >= 100:
    pisteet *= 1.15
    print("Sait 15 % bonusta")

else:
    pisteet *= 1.10
    print("Sait 10 % bonusta")
print("Pisteitä on nyt", pisteet)