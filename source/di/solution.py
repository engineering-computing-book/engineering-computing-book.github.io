""""Solution to Chapter 3 problem DI"""
import numpy as np

# %% [markdown]
## Introduction
# This program defines a NumPy array and prints the results of
# several operations.
# %% [markdown]
## Define Array
# %%
a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])  # 4x3
# %% [markdown]
## a. Adds 1 to all elements
print("Adds 1 to all elements:\n", a + 1)
# %% [markdown]
## b. Adds 1 to the last column
b = a.copy()
b[:, -1] = b[:, -1] + 1
print("Adds 1 to the last column:\n", b)
# %% [markdown]
## c. Flattens a to a vector
print("Flattens a to a vector\n", a.flatten())
# %% [markdown]
## d. Reshapes a into a 3×4 matrix
print("Reshapes a into a 3×4 matrix:\n", a.reshape((3, 4)))
# %% [markdown]
## e. Adds the vector [1, 2, 3] to each row
c = np.array([1, 2, 3])
cr = c.reshape((1, 3))  # Reshape for broadcasting
print("Adds the vector [1, 2, 3] to each row:\n", a + cr)
# %% [markdown]
## f. Adds the vector [1, 2, 3, 4] to each column
d = np.array([1, 2, 3, 4])
dr = d.reshape((4, 1))  # Reshape for broadcasting
print("Adds the vector [1, 2, 3, 4] to each column:\n", a + dr)
# %% [markdown]
## g. Reshapes a to a column vector
print("Reshapes a to a column vector:\n", a.reshape((a.size, 1)))
# %% [markdown]
## h. Reshapes a to a row vector
print("Reshapes a to a row vector:\n", a.reshape((1, a.size)))
