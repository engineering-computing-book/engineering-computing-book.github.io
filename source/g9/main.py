# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="all"
# %matplotlib inline
import engcom

# %% [markdown]
# Load SymPy as follows:
# %%
import sympy as sp

# %% [markdown]
# Now define the symbolic variables:
# %%
w, x, y, z = sp.symbols("w, x, y, z", complex=True)

# %% [markdown]
# Define the set of equations:
# %%
S = [
	8*w - 6*x + 5*y + 4*z + 20,  # == 0
	2*y - 2*z - 10,  # == 0
	2*w - x + 4*y + z,  # == 0
	w + 4*x - 2*y + 8*z - 4, # == 0
]

# %% [markdown]
# Let's try `sp.solve()`{.py}, as follows:
# %%
sol = sp.solve(S, [w, x, y, z], dict=True)
print(sol)

# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="last_expr"