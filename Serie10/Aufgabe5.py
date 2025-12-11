import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

def draw_tictactoe(board):
    fig, ax = plt.subplots(3,3)
   # plt.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0, hspace=0)

    # Alle Board-Felder zeichnen
    for row in range(3):
        for col in range(3):
            ax[row][col].set_aspect('equal')
            ax[row][col].set_xticks([]) #achsen deativieren
            ax[row][col].set_yticks([]) #achsen deativieren

            if board[row][col] == "x":
                circle = Circle((0.5, 0.5), 0.4)
                ax[row][col].add_patch(circle)

            if board[row][col] == "o":
                rect = Rectangle((0.1, 0.1), 0.8,0.8)
                ax[row][col].add_patch(rect)

    plt.show()




board = [
    ["x", "o", " "],
    [" ", "x", "o"],
    ["o", " ", "x"]
]

draw_tictactoe(board)
