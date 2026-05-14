import matplotlib.pyplot as plt
import numpy as np


def draw_board(ax, queens=None, title=""):

    n = 8

    board = np.zeros((n, n))

    for row in range(n):
        for col in range(n):
            board[row, col] = (row + col) % 2

    ax.imshow(board, cmap="binary")

    if queens:
        for row, col in enumerate(queens):
            ax.text(
                col,
                row,
                "♛",
                ha="center",
                va="center",
                color="red",
                fontsize=20
            )

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title)


fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Empty board
draw_board(axes[0], None, "Empty Chessboard")

# Incorrect arrangement
wrong_board = [0, 1, 2, 3, 4, 5, 6, 7]
draw_board(axes[1], wrong_board, "Incorrect Queen Placement")

# Correct arrangement
correct_board = [0, 4, 7, 5, 2, 6, 1, 3]
draw_board(axes[2], correct_board, "Correct Queen Placement")

plt.tight_layout()

plt.savefig("board_visualization.png", dpi=300)

plt.show()

print("board_visualization.png generated successfully")