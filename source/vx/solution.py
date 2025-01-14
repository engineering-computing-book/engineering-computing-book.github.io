""""Part of the Solution to Chapter 2 Problem VX"""

# %% [markdown]
## Introduction
# The program requirements specify a single function bubble_sort()
# be defined. It will be defined in the following section and tested
# on three lists afterward.
# %% [markdown]
## Function Definition
# %%
def bubble_sort(l: list) -> list:
    """Returns a list sorted smallest to largest."""
    n: int = len(l)
    ls: list = l.copy()  # Init. sorted list (because mutable)
    for i in range(0, n - 1):  # Pass through list n-1 times
        swapped: bool = False  # Init. swapped test (early return)
        for j in range(
            0, n - i - 1
        ):  # Pass through potentially unsorted elements
            if ls[j] > ls[j + 1]:
                jp1 = ls.pop(j + 1)
                ls.insert(j, jp1)
                swapped = True
        if not swapped:
            print(f"Early return! Had {n - i} passes left.")
            return ls  # Return early
    return ls


# %% [markdown]
## Call Function and Print
# %%
test_lists = [
    [4, 2, 6, 1, 9],
    [3.0, -1.0, 10.0, -33.0],
    [1, 2, 3, 4, 5, 3],
    [5, 4, 3, 2, 1, 0],
]

for test_list in test_lists:
    print(f"Sorted {test_list} into {bubble_sort(test_list)}")
