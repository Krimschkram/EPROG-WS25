def tictactoe_check(position):
    # Zeilen und Spalten prüfen
    for i in range(3):
        if position[i][0] == position[i][1] == position[i][2] != "": # und die reihe ist nd leer
            return f"{position[i][0]} gewinnt"
        if position[0][i] == position[1][i] == position[2][i] != "":
            return f"{position[0][i]} gewinnt"

    # Diagonalen prüfen
    if position[0][0] == position[1][1] == position[2][2] != "":
        return f"{position[0][0]} gewinnt"
    if position[0][2] == position[1][1] == position[2][0] != "":
        return f"{position[0][2]} gewinnt"

    return "Kein Gewinner"

position = [["X","O","X"],
            ["X","X","O"],
            ["O","X","O"]]

position2 =[["X","O","X"],
            ["O","X","O"],
            ["X","O","O"]]

print(tictactoe_check(position))

print(tictactoe_check(position2))