""""Part of the Solution to Chapter 2 Problem YS"""
import math
from pprint import pprint

# %% [markdown]
## Introduction
# The program will consist of the five functions identified in the
# functional analysis diagram. The pseudocode for each function will
# guide the writing of the functions. The functions are defined in
# the following section and they are tested in the last section.
# %% [markdown]
## Function Definitions
# %%
def mean(x: list) -> float:
    """Returns the mean of a numeric list x."""
    s: float = sum(x)  # Sum of items in list
    n: int = len(x)  # Number of elements in list
    return s / n


def var(x: list, mean_val: float = None) -> float:
    """Returns the sample variance of x.
    Will compute the mean if it isn't supplied
    """
    if mean_val is None:
        mean_val = mean()
    summand = []  # Initialize the summand list
    for xi in x:
        summand.append((xi - mean_val) ** 2)
    s = sum(summand)
    n = len(summand)
    return s / (n - 1)


def std(var_val: float) -> float:
    """Computes the standard deviation from the variance."""
    return math.sqrt(var_val)


def median(x: list) -> float:
    """Returns the median of list x."""
    x_s: list = sorted(x)  # New list
    n: int = len(x_s)
    i_m: float = (n - 1) / 2.0  # Nominal middle index
    if i_m.is_integer():
        med_val = x[int(i_m)]  # Middle value
    else:
        x_low = x[math.floor(i_m)]
        x_high = x[math.ceil(i_m)]
        med_val = (x_low + x_high) / 2  # Mean of middle values
    return med_val


def stats(x: list) -> dict:
    """Returns a dict with the sample mean, variance,
    standard deviation, and median.
    """
    d = {}
    d["mean"] = mean(x)
    d["var"] = var(x, d["mean"])
    d["std"] = std(d["var"])
    d["median"] = median(x)
    return d


# %% [markdown]
## Call Functions and Print
# %%
test_lists = [
    list(range(0, 11)),
    [3.0, -1.0, 10.0, -33.0],
    [1, 2, 3, 4, 5, 3],
]

for test_list in test_lists:
    print(f"Stats for {test_list}:")
    pprint(stats(test_list), width=1)
