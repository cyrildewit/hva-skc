# https://github.com/cyrildewit/hva-skc

import datetime

def calculateAgeFromBirthyear(birthyear: int) -> int:
    currentYear = datetime.datetime.now().year

    return currentYear - birthyear

def calculateAgeOnVenus(age: int) -> int:
    return age * .62

def main():
    currentYear = datetime.datetime.now().year

    name = input("Hoe heet je?\n")
    birthyear = int(input("Wat is je geboortejaar?\n"))

    age = calculateAgeFromBirthyear(birthyear)
    ageOnVenus = calculateAgeOnVenus(age)

    print("Beste " + name + ", in " + str(currentYear) + " is je leeftijd " + str(age) + ".")
    print("En je leeftijd is dan " + str(ageOnVenus) + " in Venusjaren.")

if __name__ == "__main__":
    main()
