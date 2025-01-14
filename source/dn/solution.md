``` python
""""Solution to Chapter 3 problem DN"""
import numpy as np
import matplotlib.pyplot as plt
```

# Introduction
This program defines several mathematical functions as vectorized
functions that can handle NumPy array inputs and plots them
over the given domain using Matplotlib.
# Define Mathematical Functions
Define $f(x) = x^2 + 3 x + 9$:

``` python
def f(x: np.ndarray) -> np.ndarray:
    return np.tanh(4 * np.sin(x))
```

Define $g(x) = 1 + \sin^2 x$:

``` python
def g(x: np.ndarray) -> np.ndarray:
    return np.sin(np.sqrt(x))
```

Define $h(x, y) = e^{-3 x} + \ln y$:

``` python
def h(x: np.ndarray) -> np.ndarray:
    return np.where(x >= 0, np.exp(-x) * np.sin(2 * np.pi * x), 0)
```

# Plotting
Define a plotting function:

``` python
def plotter(fig, fun, limits, labels):
    x = np.linspace(limits[0], limits[1], 201)
    fig.gca().plot(x, fun(x))
    fig.gca().set_xlabel(labels[0])
    fig.gca().set_ylabel(labels[1])
    return fig
```

Plot $f(x)$:

``` python
fig, ax = plt.subplots()
plotter(fig, fun=f, limits=(-5, 8), labels=("$x$", "$f(x)$"))
```

::: {.output .execute_result execution_count="8"}
![A graph of $f(x)$.](source/dn/figure-0.pgf){#fig:dn-figure-0 .figure .pgf}
:::

Plot $g(x)$:

``` python
fig, ax = plt.subplots()
plotter(fig, fun=g, limits=(0, 100), labels=("$x$", "$g(x)$"))
```

::: {.output .execute_result execution_count="10"}
![A graph of $g(x)$.](source/dn/figure-1.pgf){#fig:dn-figure-1 .figure .pgf}
:::

Plot $h(x)$:

``` python
fig, ax = plt.subplots()
plotter(fig, fun=h, limits=(-2, 6), labels=("$x$", "$h(x)$"))
```

::: {.output .execute_result execution_count="12"}
![A graph of $h(x)$.](source/dn/figure-2.pgf){#fig:dn-figure-2 .figure .pgf}
:::

``` python
plt.show()
```
