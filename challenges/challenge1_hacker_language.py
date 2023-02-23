"""
Español

Escribe un programa que reciba un texto y transforme lenguaje natural a
"lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
se caracteriza por sustituir caracteres alfanuméricos.

- Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
con el alfabeto y los números en "leet".
(Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

-------------------------------------------------------------------------------

English

Write a programme that receives a text and convert natural language to
"hacker language" (known as "leet" or "1337"). This language is characterize
by replacing characters alphanimeric.

- Use this table (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
with the alphabet and the numbers in "leet".
(Use this first option from each transformation. For example "4" for "a")
"""

hacker_dictionary = {
    "A": "4",
    "B": "I3",
    "C": "[",
    "D": ")",
    "E": "3",
    "F": "|=",
    "G": "&",
    "H": "#",
    "I": "1",
    "J": ",_|",
    "K": ">|",
    "L": "1",
    "M": "JVI",
    "N": "^/",
    "O": "0",
    "P": "|*",
    "Q": "(_,)",
    "R": "I2",
    "S": "5",
    "T": "7",
    "U": "(_)",
    "V": "|/",
    "W": "\/\/",
    "X": "><",
    "Y": "j",
    "Z": "2",
    "1": "L",
    "2": "R",
    "3": "E",
    "4": "A",
    "5": "S",
    "6": "b",
    "7": "T",
    "8": "B",
    "9": "g",
    "0": "o",
}


def hacker_translator(text):
    """Convert a text from natural language to hacker language"""

    final_text = ""

    for i in range(len(text)):
        char = text.upper()[i]

        if char in hacker_dictionary:
            final_text += (hacker_dictionary[char])

    return final_text


# input text
input_text = input("Write the text to transform in to leet\n")

print("input text:\n", input_text)

# Hacker text
hacker_text = hacker_translator(input_text)

print("Hacker text:\n", hacker_text)
