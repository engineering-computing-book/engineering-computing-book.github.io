# %% tags=["remove_input"]
# %matplotlib inline
# %config InteractiveShell.ast_node_interactivity="all"
import engcom


# %% [markdown]
# Import packages:
# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import engcom.data

# %% [markdown]
### Functions for Playing the Game {#functions-for-playing-the-game h="6r"}
# We begin by writing the `neighbor_indices()`{.py} function to get the
# indices of the neighbors of a cell:
# %%
def neighbor_indices(A: np.ndarray, index: tuple) -> list:
    """Returns a list of tuple indices of A that are neighbors of index
    """
    I = np.array(index)  # Index as an array, to treat as a coordinate
    # Define coordinate shifts (x rows, y columns)
    L = np.array([-1, 0])  # Left
    R = np.array([1, 0])  # Right
    U = np.array([0, 1])  # Up
    D = np.array([0, -1])  # Down
    LU = L + U  # Left and up
    LD = L + D  # Left and down
    RU = R + U  # Right and up
    RD = R + D  # Right and down
    shifts = [L, R, U, D, LU, LD, RU, RD]
    # Prewrapped neighbors
    neighbors_pre = []
    for shift in shifts:
        neighbors_pre.append(I + shift)
    # Wrap the neighbors
    x_size, y_size = A.shape
    neighbors = []
    for neighbor in neighbors_pre:
        x, y = neighbor
        neighbors.append((
            x % x_size,  # Wrapped x
            y % y_size,  # Wrapped y
        ))  # Tuples, wrapped
    return neighbors

# %% [markdown]
# Next is to write a function to determine if a given cell is alive:
# %%
def is_alive(A: np.ndarray, index: tuple) -> bool:
    """Returns True if A[index] == 1; returns False, otherwise"""
    if A[*index] == 1:
        return True
    else:
        return False

# %% [markdown]
# Now we can write a function to determine the number of alive neighbors
# a cell has:
# %%
def n_alive_neighbors(A: np.ndarray, index: tuple) -> int:
    """Returns the number of alive neighbors for a tuple index"""
    neighbors = neighbor_indices(A, index)
    n_alive = 0
    for neighbor in neighbors:
        if is_alive(A, neighbor):
            n_alive += 1
    return n_alive

# %% [markdown]
# Now define a function to find the next value of a cell, given its
# current state and those of its neighbors and Life rules:
# %%
def evolve_cell(A: np.ndarray, index: tuple):
    """Returns the next value of A[index] based on neighbor rules"""
    n_alive_neighbors_ = n_alive_neighbors(A, index)
    if is_alive(A, index):
        if n_alive_neighbors_ not in (2, 3):
            return 0  # Kill
        else:
            return 1  # Stayin alive
    else:  # Dead
        if n_alive_neighbors_ == 3:  # Otherwise it stays dead
            return 1  # Bring to life
        else:
            return 0  # The dead may never die

# %% [markdown]
# Now write a function that finds the next state of the entire world:
# %%
def evolve(A: np.array):
    """Returns a new array that is the next generation from A"""
    B = np.zeros(A.shape)  # Initialize
    for i, row in enumerate(A):
        for j, cell in enumerate(row):
            B[i, j] = evolve_cell(A, (i, j))
    return B

# %% [markdown]
# Finally we can write the `game_of_life()`{.py} function:
# %%
def game_of_life(A: np.ndarray, n_generations=5):
    """Plays a game of life on a torus with starting state A"""
    states = [A]  # Initialize list of states to start with A (gen 0)
    for igen in range(1, n_generations):
        states.append(evolve(states[igen-1]))
    return states

# %% [markdown]
### Define Starting States {#starting-states h="71"}
# Now to define the given starting states:
# %%
start1 = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
])
start2 = np.zeros((20, 20))
start2[9:12, 9:12] = np.array([
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
])
start3 = np.zeros((40, 40))
gg = np.array(engcom.data.game_of_life_starts("gosper_glider"))
start3[15:(15+gg.shape[0]), 2:(2+gg.shape[1])] = gg
starting_states = (start1, start2, start3)

# %% [markdown]
### Functions for Visualizing Games {#functions-for-visualizing-games h="nj"}
# The following function can visualize a single state of the world:
# %%
def visualize_state(state: np.ndarray):
    """Visualize a single state of a game"""
    fig, ax = plt.subplots()
    ax.matshow(state)
    plt.show()

# %% [markdown]
#### Visualize the Games with Animation {#visualize-the-games-animation}
# The following function will be used to update the animation:
# %%
def update(j):
    """Update plot with a new game state"""
    plot.set_data(game_states[j])
    return plot

# %% [markdown]
# This function will animate a game (a list of states) and save the
# animation to a gif:
# %%
def animate_game(game_states: list):
    global plot  # Needed global to communicate with update()
    fig = plt.figure(num=0)
    plot = plt.imshow(game_states[0], cmap='gray_r', vmin=0, vmax=1)
    ax = plt.gca()
    ax.set(xticks=[], yticks=[], xticklabels=[], yticklabels=[])
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
    anim = animation.FuncAnimation(
        func=update,
        fig=fig,
        frames=len(game_states), 
        interval = 250,
    )
    # plt.show()
    anim.save(f"animation_{i}.gif")

# %% [markdown]
# Now just to loop through the starting states, play the games, and
# animate:
# %% tags=["remove_output"]
for i, A in enumerate(starting_states):
    game_states = game_of_life(A, n_generations=81)
    animate_game(game_states)

# %% [markdown]
#### Visualize the Games with a Grid {#visualize-the-games-grid}
# This function will arrange visualizations of a game (a list of states)
# in a grid:
# %%
def game_gridder(game_states: list):
    nrows = int(np.floor(np.sqrt(len(game_states))))
    ncols = int(np.ceil(len(game_states)/nrows))
    fig, axs = plt.subplots(num=1, nrows=nrows, ncols=ncols)
    fig.subplots_adjust(
        left=0, right=1, top=1, bottom=0, wspace=0, hspace=0
    )
    for i, state in enumerate(game_states):
        ax = axs.flat[i]
        ax.matshow(game_states[i], cmap='gray_r', vmin=0, vmax=1)
        ax.set(xticks=[], yticks=[], xticklabels=[], yticklabels=[])
        ax.spines['top'].set_visible(True)
        ax.spines['right'].set_visible(True)
        ax.spines['bottom'].set_visible(True)
        ax.spines['left'].set_visible(True)
    n_extra = nrows * ncols - len(game_states)
    for i in range(len(game_states), nrows*ncols):
        axs.flat[i].set_axis_off()
    return fig

# %% [markdown]
# Now just to loop through the starting states, play the games, and
# plotting on a grid:
# %% tags=["remove_output"]
for i, A in enumerate(starting_states):
    game_states = game_of_life(A, n_generations=81)
    game_gridder(game_states)
    plt.show()

# %% tags=["remove_input"]
game_states = game_of_life(starting_states[0], n_generations=81)
fig = game_gridder(game_states)

# %% tags=["remove_input"]
engcom.show(fig, ext="pdf", figsize=(1.5, 1.5))

# %% tags=["remove_input"]
game_states = game_of_life(starting_states[1], n_generations=81)
fig = game_gridder(game_states)

# %% tags=["remove_input"]
engcom.show(fig, ext="pdf", figsize=(4, 4))

# %% tags=["remove_input"]
game_states = game_of_life(starting_states[2], n_generations=81)
fig = game_gridder(game_states)

# %% tags=["remove_input"]
engcom.show(fig, ext="pdf", figsize=(4.55, 4.55))

# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="last_expr"
