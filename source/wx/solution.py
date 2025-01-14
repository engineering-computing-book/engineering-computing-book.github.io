""""Solution to Chapter 3 problem QX"""
 import numpy as np
# %% [markdown]
## Introduction
# This program defines several mathematical functions as vectorized # functions that can handle NumPy array inputs.
# %% [markdown]
## a. $f(x) = x^2+ 3 x+9$
# %%
def f(x: np.ndarray) -> np.ndarray:
     return x**2 + 3 * x + 9
# %% [markdown]
## b. $g(x)=1+\sin^2{x}
# %%
def g(x: np.ndarray) -> np.ndarray:
    return 1 + np.sin(x) ** 2
# %% [markdown]
## c. $h(x, y) = e^{-3 x} + \ln y
# %%
def h(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.exp(-3 * x) + np.log(y)
# %% [markdown]
## d. $F(x,y) = \lfloor x/y \rfloor$
# %%
def F(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.floor(x / y)
# %% [markdown]
## e. $G(x, y) = \begin{cases} x^2 + y^2 & \text{if } x > y \\ 2 x & \text{otherwise}$
# %%
def G(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.where(x > y, x**2 + y**2, 2 * x)
# %% [markdown]
## Call Functions and Print
# %%
functions_args = (
    (f, 1),
    (g, 1),
    (h, 2),
    (F, 2),
    (G, 2),
)  # (fun, nargs)
x = np.array([1, 5, 10, 20, 30])
y = np.array([2, 7, 5, 10, 30])
print(f"x = {x}\ny = {y}")
for function_args in functions_args:
    if function_args[1] == 1:
        printable = np.array2string(function_args[0](x), precision=3)
        print(f"{function_args[0].__name__}(x) =", printable)
    elif function_args[1] == 2:
        printable = np.array2string(function_args[0](x, y), precision=3)
        print(f"{function_args[0].__name__}(x, y) =", printable)