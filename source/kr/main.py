# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="all"
# %matplotlib inline
import engcom

# %% [markdown]
# First, load SymPy as follows:
# %%
import sympy as sp

# %% [markdown]
# Now define the symbolic variables and the equation:
# %%
x = sp.symbols("x", complex=True)
a, b, c = sp.symbols("a, b, c", positive=True)
eq = a*x**2 + b*x + c/x + b**2  # == 0

# %% [markdown]
# Let's try `sp.solve()`{.py}, as follows:
# %%
sol = sp.solve(eq, x, dict=True)
print(sol)

# %% [markdown]
# This is a cubic solution, so it is unwieldy.

# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="last_expr"