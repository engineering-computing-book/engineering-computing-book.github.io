# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="all"
# %matplotlib inline
import sympy as sp
import numpy as np

# %% [markdown]
# The formula for the power of each element is given, so we are ready to define `power()`{.py} as follows:
# %%
def power(F, G):
	"""Returns the power for vectors F and G"""
	F = sp.Matrix(F)  # In case F isn't symbolic
	G = sp.Matrix(G)  # In case G isn't symbolic
	P = F.multiply_elementwise(G)
	# Alternative using a for loop:
	# P = sp.zeros(*F.shape)  # Initialize
	# for i, Fi in enumerate(F):
	# 	P[i] = Fi * G[i]
	return P

# %% [markdown]
# The formula for the energy stored or dissipated by each element is given, so we are ready to write `energy()`{.py} as follows:
# %%
def energy(F, G):
	"""Returns the energy stored for vectors F and G"""
	P = power(F, G)
	E = sp.integrate(P, (t, 0, t))
	return E

# %% [markdown]
# Apply these functions to the given $\bm{F}$ and $\bm{G}$.
# First, define $\bm{F}$ and $\bm{G}$ as follows:
# %%
t = sp.symbols("t", real=True)
F = sp.Matrix([
	[sp.exp(-t)], 
	[sp.exp(-t)], 
	[1 - sp.exp(-t)], 
	[1 - sp.exp(-t)]
])
G = sp.Matrix([
	[sp.exp(-t)], 
	[sp.exp(-t)], 
	[1 - sp.exp(-t)], 
	[sp.exp(-t)]
])

# %% [markdown]
# Now compute the energy:
# %% tags=["remove_output"]
E = energy(F, G).simplify()
print(E)

# %% tags=["remove_input"]
E

# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="last_expr"