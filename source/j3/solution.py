""""Solution to Chapter 3 problem J3"""
import numpy as np

# %% [markdown]
## Introduction
# This program will define two functions, left_up_sum() and
# left_up_sums(), and it will call left_up_sums() on a given
# matrix A for various numbers of sums.
# %% [markdown]
## Function Definitions
# %%
def get_element_wrapped(A: np.array, row: int, col: int) -> complex:
    """Returns an element from matrix with wrapped indices"""
    n, m = A.shape
    r = row % n  # Mod operator % returns remainder of division
    c = col % m
    return A[r, c]


def left_up_sum(A: np.ndarray) -> np.ndarray:
    """Adds the element to the left and the element above
    (wrapping, if necessary) to each component. Passes through
    the array once, row-by-row, and returns a new array.
    """
    shape = A.shape
    B = A.copy()  # Initialize output array
    for r in range(0, shape[0]):  # Each row
        for c in range(0, shape[1]):  # Each column
            left = get_element_wrapped(B, r - 1, c)
            up = get_element_wrapped(B, r, c + 1)
            B[r, c] = B[r, c] + left + up
    return B


def left_up_sums(A: np.ndarray, n: int) -> np.ndarray:
    """Calls left_up_sum() n times on A and returns the result"""
    for iteration in range(0, n):
        A = left_up_sum(A)
    return A


# %% [markdown]
## Call Function and Print
# %%
A = np.array(
    [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    ]
)
test_sum_numbers = [0, 1, 4]

for n in test_sum_numbers:
    print(f"left_up_sums() of A for {n} sums:")
    print(left_up_sums(A, n))
