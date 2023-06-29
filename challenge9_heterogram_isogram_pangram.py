"""
Español

Crea 3 funciones, cada una encargada de detectar si una cadena de texto es un heterograma, un isograma o un pangrama.
- Heterograma: es una palabra o frase que no tiene ninguna letra repetida.
- Isograma: es una palabra o frase en la que las letras se repiten el mismo número de veces.
- Pangrama: es una frase que contiene todas las letras del alfabeto.

-----------------------------------------------------------------------------
English

Create 3 functions, each one in charge of detecting if a text string is a heterogram, an isogram or a pangram.
- Heterogram: is a word or phrase that doesn't have any repeated letter.
- Isogram: is a word or phrase in which the letters are repeated the same number of times.
- Pangram: is a phrase that contains all the letters of the alphabet.
"""


def is_heterogram(text: str):
    text = text.replace(" ", "").lower()
    for letter in text:
        if text.count(letter) > 1:
            return False
    return True


def is_isogram(text: str):
    text = text.replace(" ", "").lower()
    for letter in text:
        if text.count(letter) != text.count(text[0]):
            return False
    return True


def is_pangram(text: str):
    text = text.replace(" ", "").lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in text:
            return False
    return True


def result(text):
    print(f"Is {text} a heterogram? {is_heterogram(text)}")
    print(f"Is {text} an isogram? {is_isogram(text)}")
    print(f"Is {text} a pangram {is_pangram(text)}")


example = "The big dwarf only jumps"
result(example)
