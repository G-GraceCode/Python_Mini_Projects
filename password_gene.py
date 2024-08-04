import random
import string


def generate_password(min_length, numbers=True, special_character=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    character = letters
    if numbers:
        character += digits
    if special_character:
        character += special
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(character)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_character:
            meets_criteria = meets_criteria and has_special

    return pwd


pwd_length = int(input("Enter the length of your password: "))
has_number = input("Do you want to have numbers: (y/n) ").lower() == "y"
has_special = input(
    "Do you want to have special character: (y/n) ").lower() == "y"
pwd = generate_password(pwd_length, has_number, has_special)
print("Generated Password is: ", pwd)
