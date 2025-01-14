import numpy as np
import matplotlib.pyplot as plt
import engcom.data

d = engcom.data.movie_ratings_binned()
x = list(range(0,len(d["rating_freq"])))

fig, ax = plt.subplots()
ax.bar(x, d["rating_freq"], color="dodgerblue", width=.9)
ax.set_xticks(x)
ax.set_xticklabels(d["labels"])
ax.set_xlabel("Rating out of $10$")
ax.set_ylabel("Frequency")
plt.show()

# %% Book figure

import engcom.tufte

fig, ax = engcom.tufte.bar(
    x,
    d["rating_freq"],
    xlabel="Rating out of $10$",
    ylabel="Frequency",
    # xticklabels=d["labels"],
    barsize=1,
    align="edge",
    save="movie_rating_histogram.pgf",
    figsize=(4,4/1.68),
    color="dodgerblue",
)
plt.show()