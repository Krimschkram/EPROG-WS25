from matplotlib import pyplot as plt
from matplotlib.patches import Circle, Rectangle

def plot_tictactoe(board):
    """
    board: 3x3-Matrix aus Strings " ", "x", "o"
    z.B. [["x","o"," "],
          [" ","x","o"],
          ["o"," ","x"]]
    """
    fig, ax = plt.subplots()

    # Spielfeld (3x3-Gitter) zeichnen
    for i in range(1, 3):
        # vertikale Linien
        ax.plot([i, i], [0, 3], color="black")
        # horizontale Linien
        ax.plot([0, 3], [i, i], color="black")

    # Einträge zeichnen
    for row in range(3):
        for col in range(3):
            cell = board[row][col]
            # Mittelpunkt des Feldes
            x_center = col + 0.5
            # row 0 soll oben sein → 2 - row
            y_center = 2.5 - row

            if cell == "o":
                # Kreis für "o"
                circle = Circle((x_center, y_center), 0.35,
                                fill=False, linewidth=2)
                ax.add_patch(circle)

            elif cell == "x":
                # Rechteck (oder andere Form) für "x"
                rect = Rectangle((col + 0.15, y_center - 0.35),
                                 0.7, 0.7,
                                 fill=False, linewidth=2)
                ax.add_patch(rect)

    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    plt.title("Tic-Tac-Toe")
    plt.tight_layout()
    plt.show()

board = [
    ["x", "o", " "],
    [" ", "x", "o"],
    ["o", " ", "x"]
]

plot_tictactoe(board)