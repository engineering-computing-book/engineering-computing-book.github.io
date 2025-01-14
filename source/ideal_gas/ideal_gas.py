import numpy as np
import matplotlib.pyplot as plt
import engcom.data

d = engcom.data.ideal_gas(
    V = np.linspace(1, 2, 16),
    T=np.linspace(273, 573, 4),
    noisy=.015,
)

fig, ax = plt.subplots()
for j, Tj in enumerate(d["temperature"].flatten()):
    x = d["volume"]  # (m^3)
    y = d["pressure"][:,j] / 1e6  # (MPa)
    ax.plot(x, y, marker="o", color="dodgerblue")  # Circle markers
    ax.text(x=x[-1], y=y[-1], s=f"$T = {Tj}$ K")  # Label last point
ax.set_xlabel("Volume (m$^3$)")
ax.set_ylabel("Pressure (MPa)")
plt.show()

# %% Book figure

import engcom.tufte

labels = []
for Ti in d["temperature"].flatten():
    labels.append(f"$T = {Ti}$ K")

fig, ax = engcom.tufte.plot(
    d["volume"],
    d["pressure"] / 1e6,
    axis=0,
    xlabel="Volume (m$^3$)",
    ylabel="Pressure (MPa)",
    labels=labels,
    save="ideal_gas.pgf",
    figsize=(4,4/1.68),
    dotsize=5,
    color="dodgerblue",
)
plt.show()