def tictactoe_check(position):
    # Zeilen und Spalten prüfen
    for i in range(3):
    # geht alle Zeilen und Spalten mit einer Schleife durch und prüft ob alle elemente der Zeilen und spalten gleich sind
    # wenn sie gleich sind dann hat einer gewonnen
        if position[i][0] == position[i][1] == position[i][2] != "": # und die reihe ist nd leer
            return f"{position[i][0]} gewinnt"
        if position[0][i] == position[1][i] == position[2][i] != "":
            return f"{position[0][i]} gewinnt"

    # Diagonalen prüfen
    # prüft manuell ob die Elemente der Diagonalen gleich sind
    if position[0][0] == position[1][1] == position[2][2] != "":
        return f"{position[0][0]} gewinnt"
    if position[0][2] == position[1][1] == position[2][0] != "":
        return f"{position[0][2]} gewinnt"

    # wenn es für nichts einen gewinner gibt, dann kann keiner gewinnen
    return "Kein Gewinner"

position = [["X","O","X"],
            ["X","X","O"],
            ["O","X","O"]]

position2 =[["X","O","X"],
            ["O","X","O"],
            ["X","O","O"]]

print(tictactoe_check(position))

print(tictactoe_check(position2))