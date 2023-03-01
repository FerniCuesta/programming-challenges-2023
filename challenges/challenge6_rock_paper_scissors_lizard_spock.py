"""
Español
Crea un programa que calcule quien gana más partidas al piedra,
papel, tijera, lagarto, spock.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
  "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
- Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
- Debes buscar información sobre cómo se juega con estas 5 posibilidades.

Como explica Sheldon, "Tijeras cortan papel, papel cubre piedra, piedra aplasta lagarto,
lagarto envenena a Spock, Spock destruye tijeras, tijeras decapitan lagarto, 
lagarto come papel, papel desaprueba a Spock, Spock vaporiza piedra, y como siempre,
piedra aplasta tijeras."
-------------------------------------------------------------------------------

English
Create a programme that calculates who wins more matches in rock, paper,
 scissors, lizard, spock.
- The result can be: "Player 1", "Player 2", "Tie"
- The function receives a pair list, in representation of each play-
- The pair can contain combinations of "🗿" (rock), "📄" (paper),
  "✂️" (scissors), "🦎" (lizard) o "🖖" (spock).
- For example. Entry: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Result: "Player 2".

As Sheldon explains, "Scissors cuts paper, paper covers rock, rock crushes lizard, 
lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, 
lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, 
rock crushes scissors."

-------------------------------------------------------------------------------
To solve this problem we are going to create a matrix with the possible options of the
Player 1 in the columns and the possible options of the Player 2 in the rows.
In each cell will be a number:
- 0: if tie
- 1: if wins Player_1
- 2: if wins Player_2
"""


def winner(puntuation_1, puntuation_2):
    """Function that prints the result of the game"""
    print("Result of the game: ")
    if puntuation_1 > puntuation_2:
        print("Player 1 wins!!")
    elif puntuation_2 > puntuation_1:
        print("Player 2 wins!!")
    else:
        print("Tie")


def update_score(play_result, array):
    """Funtion that update the game score after a play"""
    if play_result == 1:
        array[0] += 1
    elif play_result == 2:
        array[1] += 1


results = ([[0, 2, 1, 1, 2],
            [1, 0, 2, 2, 1],
            [2, 1, 0, 1, 2],
            [2, 1, 2, 0, 1],
            [1, 2, 1, 2, 0]])


options = {
    0: "🗿",
    1: "📄",
    2: "✂️",
    3: "🦎",
    4: "🖖"
}


puntuation = [0, 0]

option_p1 = 0
option_p2 = 0

# play = results[0][1]
play = results[options.get("🗿")][options.get("📄")]

# update score after this last play
update_score(play, puntuation)

# print who wins
print(f"{winner(puntuation[0], puntuation[1])}")
