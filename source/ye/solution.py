# %% [markdown]
## Packages
# %%
import random

# %% [markdown]
## Functions
# %%
def rand_step(x, d, ymax, wrap=True):
    """Returns the sum of x and a random float between -d and d"""
    step = random.uniform(-d, d)
    y = x + step
    if wrap:
        if y > ymax:
            y = y - ymax
        elif y < 0:
            y = ymax + y
    else:
        if y > ymax:
            y = ymax
        elif y < 0:
            y = 0
    return y


def rand_steps(x0, d, ymax, n, wrap=True):
    """Returns a list of n floats sequentially stepped from x0"""
    values = [x0]
    for i in range(0, n):
        values.append(rand_step(values[-1], d, ymax, wrap=wrap))
    return values


def print_slider(k, x):
    """Prints k '-' characters except for that with index
    closest to x, which prints |
    """
    x_rounded = round(x)
    if x_rounded < 0:
        x_rounded = 0  # Coerce to 0
    elif x_rounded > k:
        x_rounded = k - 1  # Coerce to max index
    for i in range(0, k):
        if i == x_rounded:
            print("|", end="")
        else:
            print("-", end="")
    print("")  # Line break applied


def rand_sliders(n, k, x0=None, d=3, wrap=True):
    """Prints n random sliders with k characters"""
    if not x0:
        x0 = k / 2  # Start in the middle
    values = rand_steps(
        x0,  # Initial value
        d,  # Max step size
        ymax=k - 1,  # Subtract 1 because 0-indexed
        n=n,  # One value per slider
        wrap=wrap,  # Pass wrap
    )
    for x in values:
        print_slider(k, x)


# %% [markdown]
## Call Functions and Print
# %%
print("rand_sliders(25, 44, x0=2, wrap=True):")
rand_sliders(25, 44, x0=2, wrap=True)
print("rand_sliders(20, 44, x0=42, d=5, wrap=False):")
rand_sliders(20, 44, x0=42, d=5, wrap=False)

# %% tags=["active-py"]
import sys

sys.path.append("../")
import engcom.engcom as engcom

pub = engcom.Publication(title="Problem YE", author="Rico Picone")
pub.write(to="pdf")
