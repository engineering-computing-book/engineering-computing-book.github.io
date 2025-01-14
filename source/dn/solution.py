""""Solution to Chapter 3 problem DN"""
import numpy as np
import matplotlib.pyplot as plt

# %% tags=["remove_input"]
# %matplotlib inline
import engcom


# %% [markdown]
## Introduction
# This program defines several mathematical functions as vectorized
# functions that can handle NumPy array inputs and plots them
# over the given domain using Matplotlib.
# %% [markdown]
## Define Mathematical Functions
# Define $f(x) = x^2 + 3 x + 9$:
# %%
def f(x: np.ndarray) -> np.ndarray:
    return np.tanh(4 * np.sin(x))


# %% [markdown]
# Define $g(x) = 1 + \sin^2 x$:
# %%
def g(x: np.ndarray) -> np.ndarray:
    return np.sin(np.sqrt(x))


# %% [markdown]
# Define $h(x, y) = e^{-3 x} + \ln y$:
# %%
def h(x: np.ndarray) -> np.ndarray:
    return np.where(x >= 0, np.exp(-x) * np.sin(2 * np.pi * x), 0)


# %% [markdown]
## Plotting
# Define a plotting function:
# %%
def plotter(fig, fun, limits, labels):
    x = np.linspace(limits[0], limits[1], 201)
    fig.gca().plot(x, fun(x))
    fig.gca().set_xlabel(labels[0])
    fig.gca().set_ylabel(labels[1])
    return fig

# %% [markdown]
# Plot $f(x)$:

# %% tags=["remove_output"]
fig, ax = plt.subplots()
plotter(fig, fun=f, limits=(-5, 8), labels=("$x$", "$f(x)$"))

# %% tags=["remove_input"]
engcom.show(fig, caption="A graph of $f(x)$.")

# %% [markdown]
# Plot $g(x)$:

# %% tags=["remove_output"]
fig, ax = plt.subplots()
plotter(fig, fun=g, limits=(0, 100), labels=("$x$", "$g(x)$"))

# %% tags=["remove_input"]
engcom.show(fig, caption="A graph of $g(x)$.")

# %% [markdown]
# Plot $h(x)$:

# %% tags=["remove_output"]
fig, ax = plt.subplots()
plotter(fig, fun=h, limits=(-2, 6), labels=("$x$", "$h(x)$"))

# %% tags=["remove_input"]
engcom.show(fig, caption="A graph of $h(x)$.")

# %%
plt.show()