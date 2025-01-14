import numpy as np
import matplotlib.pyplot as plt

def f(x):
	a0, a1, a2, a3, a4 = 10, 10, -20, -1, 1
	return a4 * x ** 4 + a3 * x ** 3 + a2 * x ** 2 + a1 * x + a0

x = np.linspace(-5, 5, 101)
y = f(x)

fig, ax = plt.subplots()  # Create a figure and an axis
ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
# plt.show()


# fig, ax = plt.subplots()  # Create a figure and an axis
# ax.plot(x, y)
# ax.set_xlabel("$x$")
# ax.set_ylabel("$f(x)$")

# fig.savefig("function_graph_example.pgf")
import sys
sys.path.append("../")
import engcom.engcom.tufte as tufte
import engcom.engcom.data as data

fig, ax = tufte.plot(
	x, y,
    xlabel="$x$",
    ylabel="$f(x)$",
    axis=0,
    save="function_graph_example.pgf",
    figsize=(3,3/1.68),
    color="dodgerblue",
    points=False,
)
plt.show()