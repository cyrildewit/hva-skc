# https://github.com/cyrildewit/hva-skc

import datetime

currentYear = datetime.datetime.now().year

name = input("Hoe heet je?\n")
birthyear = int(input("Wat is je geboortejaar?\n"))

age = currentYear - birthyear
ageOnVenus = age * .62

print("Beste " + name + ", in " + str(currentYear) + " is je leeftijd " + str(age) + ".")
print("En je leeftijd is dan " + str(ageOnVenus) + " in Venusjaren.")
