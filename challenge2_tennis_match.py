"""
Español

Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
gane cada punto del juego.

- Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
- Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
15 - Love
30 - Love
30 - 15
30 - 30
40 - 30
Deuce
Ventaja P1
Ha ganado el P1
- Si quieres, puedes controlar errores en la entrada de datos.
- Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.

-------------------------------------------------------------------------------

English

Write a programme that shows how takes place a tennis game and who wins.
The programme receives a secuence formed by "P1" (Player 1) or "P2" (Player 2), depending on
who wins each point of the game.

- The puntuations are "Love" (zero), 15, 30, 40, "Deuce" (draw), advantage.
- With the secuence [P1, P1, P2, P2, P1, P2, P1, P1], the programme would display:
15 - Love
30 - Love
30 - 15
30 - 30
40 - 30
Deuce
Advantage P1
P1 wins
- If you want, you can control errors in data entries.
- Consult the game rules if you have doubts about the puntuation system.
"""


def tennis_game():

    # array with possible puntuation
    puntuation = ["Love", "15", "30", "40"]

    # puntuation for each player
    puntuation_P1 = 0
    puntuation_P2 = 0

    # stade of the game
    finished = False

    while (not finished):
        # ask to the user the next point
        point = input("Who scores next point? (P1 / P2)")

        # check possible errors
        if (point != "P1" and point != "P2"):
            print("You must print P1 or P2")
        else:
            # update puntuation
            if (point == "P1"):
                puntuation_P1 += 1
            else:
                puntuation_P2 += 1
            # -----------------------------------------------------------------
            # print puntuation

            if (puntuation_P1 >= 3 and puntuation_P2 >= 3):
                if (puntuation_P1 == puntuation_P2):
                    print("Deuce")
                elif (puntuation_P1 > puntuation_P2 + 1):
                    print("P1 wins")
                elif (puntuation_P2 > puntuation_P1 + 1):
                    print("P2 wins")
                elif (puntuation_P1 > puntuation_P2):
                    print("Advantage P1")
                else:
                    print("Advantage P2")
            else:
                print(f"{puntuation[puntuation_P1]} - {puntuation[puntuation_P2]}")


# lets play the game!
tennis_game()
