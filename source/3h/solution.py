""""Solution to Chapter 3 problem 3H"""
import numpy as np

# %% [markdown]
## Introduction
# This program defines matrices A and B and vectors x and y. It then
# computes several quantities that require matrix operations.
# %% [markdown]
## a. Define Arrays
# %%
A = np.array(
    [
        [2, 1, 9, 0],
        [0, -1, -2, 3],
        [-3, 0, 8, -4],
    ]
)
B = np.array(
    [
        [0, 9, -1],
        [1, 0, 3],
        [0, -1, 1],
    ]
)
x = np.array([[1], [0], [-1]])
y = np.array([[3, 0, -1]])
# %% [markdown]
## b. Compute and Print Quantitites

### i. $B A$
# %%
print("B A = \n", B @ A)
# %% [markdown]
### ii. $A^\top B - 6 J_{4\times 3}$
# %%
print("A.T B - 6 J_4x3 = \n", A.T @ B - 6 * np.ones((4, 3)))
# %% [markdown]
### iii. $B \bm{x} + \bm{y}^\top$
# %%
print("B x + y.T = \n", B @ x + y.T)
# %% [markdown]
### iv. $\bm{x} \bm{y} + B$
# %%
print("x y + B = \n", x @ y + B)
# %% [markdown]
### v. $\bm{y} \bm{x}$
# %%
print("y x = \n", y @ x)
# %% [markdown]
### vi. $\bm{y} B^{-1} \bm{x}$
# %%
print("y B^-1 x = \n", y @ np.linalg.inv(B) @ x)
# %% [markdown]
### vii. $C B$
# %%
C = A[:, :3]  # First 3 columns of A (view)
print("C B = \n", C @ B)

# %% tags=["active-py"]
import sys

sys.path.append("../")
import engcom.engcom as engcom

pub = engcom.Publication(title="Problem 3H", author="Rico Picone")
pub.write(to="md")
