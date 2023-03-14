"""
Español

Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)

-------------------------------------------------------------------------------

English

Write a programme that is able to generate random passwords.
You can configurate passwords with the following parameters:
- Length: between 8 - 16.
- With or without capital letters.
- With or without numbers.
- With or without symbols.
(Being able to combine all these parameters between them)
"""
import random


def random_password_generator(length=8, capital_letters=False, numbers=False, symbols=False):
    """Function that generates random passwords with the requirements above"""

    # check parameters
    if length < 8:
        length = 8
    elif length > 16:
        length = 16

    # source: https://www.ascii-code.com

    # characters allowed
    possible_characters = list(range(97, 123))

    if capital_letters:
        possible_characters += list(range(65, 91))

    if numbers:
        possible_characters += list(range(48, 58))

    if symbols:
        possible_characters += list(range(33, 48)) + \
            list(range(58, 65)) + list(range(91, 97)) + \
            list(range(123, 127))

    # create password
    password = ""

    while len(password) < length:
        password += chr(random.choice(possible_characters))

    return password


# lets generate some random passwords!

# 8 lower case letters
print(f"{random_password_generator()}\n")

# 16 lower case letters
print(f"{random_password_generator(length=16)}\n")

# try to 25 lower case letters (convert to 16)
print(f"{random_password_generator(length=25)}\n")

# try to 4 lower case letters (convert to 8)
print(f"{random_password_generator(length=4)}\n")

# lower case + capital letters
print(f"{random_password_generator(length=10, capital_letters=True)}\n")

# lower case + symbols
print(f"{random_password_generator(length=13, symbols=True)}\n")

# lower case + numbers
print(f"{random_password_generator(length=16, numbers=True)}\n")

# lower case letters + capital letters + numbers + symbols
print(f"{random_password_generator(length=16, capital_letters=True, numbers=True, symbols=True)}\n")
