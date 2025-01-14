``` python
""""Solution to Chapter 3 problem WF"""
import numpy as np
import matplotlib.pyplot as plt
import engcom.data
```

# Introduction
This program loads and plots ideal gas data with the
`ideal_gas()`{.py} function from the `engcom.data`{.py} module.
# Load the Data

``` python
d = engcom.data.ideal_gas(
    V=np.linspace(0.1, 2.1, 16),  # (m^3) Volume values
    T=np.array([300, 400, 500]),  # (K) Temperature values
)
```

# Plot
Now `d`{.py} is a dictionary with the following key–value pairs:

- `"volume"`{.py}: $V_{16\times 1}$ (m$^3$)
- `"temperature"`{.py}: $T_{1\times 3}$ (K)
- `"pressure"`{.py}: $P_{16\times 3}$ (Pa)

We would like to plot $P$ versus $V$ for each of the $3$ temperatures
$T$; that is, plot a sequence of pairs $(P_i, V_i)$ for each $T_j$.
The following code loops through the temperatures and plots to the
same axes object:

``` python
fig, ax = plt.subplots()
for j, Tj in enumerate(d["temperature"].flatten()):
    x = d["volume"]  # (m^3)
    y = d["pressure"][:, j] / 1e6  # (MPa)
    ax.plot(x, y, marker="o", label=f"$T = {Tj}$ K")
```

Finally, we label the axes and display the figure with the following
code:

``` python
ax.set_xlabel("Volume (m$^3$)")
ax.set_ylabel("Pressure (MPa)")
ax.legend()  # Show labels in legend
plt.show()
```

::: {.output .execute_result execution_count="6"}
![Ideal gas plot.](source/wf/figure-0.pgf){#fig:wf-figure-0 .figure .pgf}
:::
