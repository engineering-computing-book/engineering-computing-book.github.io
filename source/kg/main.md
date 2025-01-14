Import packages:

``` python
import numpy as np
import matplotlib.pyplot as plt
import engcom.data
```

We begin by writing the `binner()`{.py} function:

``` python
def binner(A: np.ndarray, nbins: int = 10) -> (np.ndarray, np.ndarray):
    """Accepts an array A of data and returns an array for the frequency
    of the data in each bin and an array of the bin edges
    """
    Af = np.array(A).flatten()  # Ensure a vector
    minA = Af.min()
    maxA = Af.max()
    bin_edges = np.linspace(minA, maxA, nbins + 1)
    bw = bin_edges[1] - bin_edges[0]  # Bin width
    A_from_min = Af - minA  # Distance from min
    Abin = np.floor(A_from_min / bw)  # Bin index of each element of A
    Abin[Abin == nbins] = (
        nbins - 1
    )  # This moves element at maxA into the proper (last) bin
    nonempty_bin_index, nonempty_bin_frequency = np.unique(
        Abin, return_counts=True
    )  # Identifies nonempty bin indices and the frequency in each bin
    bin_frequency = np.zeros(nbins)  # Initialize frequencies to zero
    bin_frequency[
        nonempty_bin_index.astype(int)
    ] = nonempty_bin_frequency
    return bin_frequency, bin_edges
```

Now the histogram function can be written:

``` python
def histogram(A: np.ndarray, nbins: int = 10, xlabel=None, ylabel=None):
    """Create a histogram figure."""
    bin_frequency, bin_edges = binner(A, nbins=nbins)
    bw = bin_edges[1] - bin_edges[0]  # Bin width
    fig, ax = plt.subplots()
    ax.bar(
        x=bin_edges[0:-1],
        height=bin_frequency,
        width=0.95 * bw,
        align="edge",  # Left edge at x coordinate (left bin edge)
    )
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    return fig
```

Now we load the thermal conductivity data. The material labels (keys)
aren't necessary for the histograms, so we just extract the values.
The data is loaded as follows:

``` python
data = engcom.data.thermal_conductivity()
tc_metals = list(data["Metals"].values())
tc_liquids = list(data["Liquids"].values())
tc_gases = list(data["Gases"].values())
```

Now call the `histogram()`{.py} function to generate a histogram chart
for each data set.

``` python
fig = histogram(
    tc_metals,
    nbins=10,
    xlabel="Thermal conductivity (W/(m$\cdot$K))",
    ylabel="Frequency (metals)",
)
```

::: {.output .execute_result execution_count="7"}
![A caption.](source/kg/figure-0.pgf){#fig:kg-figure-0 .figure .pgf}
:::

``` python
fig = histogram(
    tc_liquids,
    nbins=10,
    xlabel="Thermal conductivity (W/(m$\cdot$K))",
    ylabel="Frequency (liquids)",
)
```

::: {.output .execute_result execution_count="9"}
![A caption.](source/kg/figure-1.pgf){#fig:kg-figure-1 .figure .pgf}
:::

``` python
fig = histogram(
    tc_gases,
    nbins=10,
    xlabel="Thermal conductivity (W/(m$\cdot$K))",
    ylabel="Frequency (gases)",
)
plt.show()
```

::: {.output .execute_result execution_count="11"}
![A caption.](source/kg/figure-2.pgf){#fig:kg-figure-2 .figure .pgf}
:::
