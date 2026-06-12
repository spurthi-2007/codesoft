import random
import string

print("=" * 50)
print("        PASSWORD GENERATOR ")
print("=" * 50)

while True:

    print("\nChoose Password Complexity:")
    print("1. Letters Only")
    print("2. Letters + Numbers")
    print("3. Letters + Numbers + Special Characters")

    choice = input("Enter your choice (1/2/3): ")

    length = int(input("Enter desired password length: "))

    if choice == "1":
        characters = string.ascii_letters

    elif choice == "2":
        characters = string.ascii_letters + string.digits

    elif choice == "3":
        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

    else:
        print("Invalid Choice!")
        continue

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)

    print("\nPassword Information")
    print("--------------------")
    print("Length :", len(password))

    letters = 0
    digits = 0
    specials = 0

    for ch in password:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1
        else:
            specials += 1

    print("Letters :", letters)
    print("Digits  :", digits)
    print("Special Characters :", specials)

    if length >= 12:
        print("Password Strength : Strong")
    elif length >= 8:
        print("Password Strength : Medium")
    else:
        print("Password Strength : Weak")

    again = input("\nGenerate another password? (yes/no): ")

    if again.lower() != "yes":
        print("\nThank You For Using Password Generator!")
        break