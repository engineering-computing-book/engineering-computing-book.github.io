``` python
""""Solution to Chapter 3 problem Y1"""
import numpy as np
import matplotlib.pyplot as plt
import engcom.data
```

# Introduction
This program loads ideal gas data with the engcom.data.ideal_gas()
function. It computes the work done by the gas over the given volume.
Finally, it charts the work for each temperature.
# Load the Data
Load the pressure-volume-temperature data as follows:

``` python
d = engcom.data.ideal_gas(
    V=np.linspace(0.1, 2.1, 16),  # (m^3) Volume values
    T=np.array([300, 400, 500]),  # (K) Temperature values
)
```

# Define and Compute the Work
Define a function to compute the work and apply the function.

``` python
def W(P: np.ndarray, V: np.ndarray, axis: int = -1) -> float:
    """Use trapezoidal integration to estimate the work from P(V)"""
    return np.trapz(P, V, axis=0)
work = W(P=d["pressure"], V=d["volume"])
```

# Plot
Create a bar chart of work for each temperature

``` python
x = np.arange(len(work))
labels = np.char.add(d["temperature"].flatten().astype(dtype=str), " K")
fig, ax = plt.subplots()
ax.bar(x, work / 1e6)
ax.set_xticks(x, labels=labels)
ax.set_ylabel("Work (MJ)")
plt.show()
```

::: {.output .execute_result execution_count="5"}
![A caption.](source/y1/figure-0.pgf){#fig:y1-figure-0 .figure .pgf}
:::
