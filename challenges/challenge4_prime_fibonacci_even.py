"""
Español

Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

-------------------------------------------------------------------------------

English

Write a programme that, given a number, checks and shows if it is prime, fibonacci and even.
Example:
- Given number 2: "2 is prime, fibonacci and even"
- Given number 7: "7 is prime, is not fibonacci and odd"
"""


def is_prime(number):
    """Return True if is a prime number and False if not"""
    for i in range(2, number):
        if (number % i == 0):
            return False

    return True


def is_even(number):
    """Return True if is an even number and False if is odd"""
    return (number % 2 == 0)


def is_fibonacci(number):
    """Return True if is a fibonacci number and False if not"""
    return True


def is_prime_fibonacci_even(number):
    """Return a String with the information about is the number is
    prime, fibonacci and even"""
    result = f"{number}"

    if is_prime(number):
        result += " is prime,"
    else:
        result += " is not prime,"

    if is_fibonacci(number):
        result += " is fibonacci"
    else:
        result += " is not fibonacci"

    if is_even(number):
        result += " and is even"
    else:
        result += " and is odd"

    return result


# lets answer for a number and check
num = int(input("Insert a number:\n"))

print(is_prime_fibonacci_even(num))
