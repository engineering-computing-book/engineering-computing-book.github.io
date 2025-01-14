import numpy as np
import matplotlib.pyplot as plt
import engcom.data

d = engcom.data.thermal_conductivity(category="Metals", paired=False)
y = np.arange(len(d["labels"]))
x_alpha = d["conductivity"]  # Alphabetically sorted
labels_alpha = np.array(d["labels"])  # Alphabetically sorted

ix = np.lexsort((labels_alpha, x_alpha))  # Sorting indices by conductivity
x = x_alpha[ix]
labels = labels_alpha[ix].tolist()

fig, ax = plt.subplots()
ax.barh(y, x, color="dodgerblue")
ax.set_yticks(y, labels=labels)
ax.set_xlabel("Thermal conductivity (W/(m$\\cdot$K))")
plt.show()

# # %% Book figure

import engcom.tufte

fig, ax = engcom.tufte.bar(
    x, y,
    orientation="horizontal",
    xlabel="Thermal conductivity (W/(m$\\cdot$K))",
    labels=labels,
    save="charts_bar_thermal_conductivity.pgf",
    figsize=(4.8,4.8),
    color="dodgerblue",
)
plt.show()