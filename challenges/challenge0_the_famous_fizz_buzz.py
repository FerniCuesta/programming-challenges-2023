"""
Español
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

-------------------------------------------------------------------------------

English
Write a programme that shows on terminal (with a print) the numbers
from 1 to 100 (both included and with a line break between each imprint),
by replacing the following:
- Multiples of 3 by the word "fizz"
- Multiples of 5 by the word "buzz"
- Multiples of 3 & 5 at the same time by the word "fizzbuzz"
"""

for number in range(100):
    if number % (3 * 5) == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
