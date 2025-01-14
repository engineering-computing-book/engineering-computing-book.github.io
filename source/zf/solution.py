""""Solution to Chapter 3 problem ZF"""
import numpy as np

# %% [markdown]
## Introduction
# This program defines a function inner_flat_trunc() for computing
# the real inner product of two vectors that needn't be the same length
# %% [markdown]
## Function Definitions
# %%
def inner_flat_trunc(x: np.ndarray, y: np.ndarray) -> float:
    """Returns the real inner product of two vectors of potentially
    different lengths
    """
    # Check input dtypes
    ok_dtypes = [np.dtype("float"), np.dtype("int")]
    if not (x.dtype in ok_dtypes and y.dtype in ok_dtypes):
        raise TypeError("Both vectors must be of type float or int.")
    x = x.flatten()
    y = y.flatten()
    min_len = min(len(x), len(y))
    prod = 0  # Initialize inner product
    for i in range(min_len):
        prod += x[i] * y[i]
    return prod


# %% [markdown]
## Call Function and Print
# %%
test_vector_pairs = (
    (
        np.array([-1.1, 3, 2.9, -1, -9.2, 0.1]),
        np.array([1.3, 0.2, 8.3]),
    ),
    (np.arange(0, 14), np.arange(3, 13)),
    (np.linspace(0, 10, 21), np.linspace(5, 25, 11)),
    (np.array([True, False, True]), np.array([0, 1, 2])),
)

for vector_pair in test_vector_pairs:
    print(
        f"Product of\n\tx = {vector_pair[0]} and"
        f"\n\ty = {vector_pair[1]}:"
    )
    try:
        product = inner_flat_trunc(vector_pair[0], vector_pair[1])
    except TypeError as e:
        print(f"\t\tCaught TypeError: {e}")
        break
    print("\t\t", product)
