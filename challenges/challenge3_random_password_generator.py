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


def random_password_generator():
    """Function that generates random passwords with the parameters above"""
    password = "hola"
    return password


# lets generate some random passwords!
for i in range(10):
    random_password_generator()
