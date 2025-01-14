# %%
import numpy as np
import matplotlib.pyplot as plt
import engcom.data
from engcom.data import game_of_life_starts


# %%
def game_of_life(A: np.ndarray):
    rows, cols = A.shape
    state = np.zeros_like(A)

    for x in range(rows):
        for y in range(cols):

            living = count_live_neighbors(A, x, y)
            if A[x, y] == 1:
                if living == 2 or living == 3:
                    state[x, y] = 1
            else:
                if living == 3:
                    state[x, y] = 1
    return state


# %%
def count_live_neighbors(A: np.ndarray, x: int, y: int) -> int:
    rows, cols = A.shape
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx = (x + dx) % rows
            ny = (y + dy) % cols
            count += A[nx, ny]
    return count


# %%
def animate(A: np.ndarray, steps: int):
    plt.figure()
    for _ in range(steps):
        plt.matshow(A)
        plt.show()
        A = game_of_life(A)


# %%
if __name__ == "__main__":

    blinker = np.array(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    glider = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])

    gosper_glider = game_of_life_starts("gosper_glider")

    for name, state in [
        ("Blinker", blinker),
        ("Glider", glider),
        ("Gosper Glider", gosper_glider),
    ]:
        print(f"Starting state: {name}")
        plt.matshow(state)
        plt.show()

        animate(state, steps=10)
# %% tags=["active-py"]
pub = engcom.Publication(title="Problem_2", author="Karis Sanders")
pub.write(to="docx")
