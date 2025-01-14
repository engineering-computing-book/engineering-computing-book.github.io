# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="all"
# %matplotlib inline
import engcom

# %% [markdown]
# First, load SymPy and define the expression:
# %%
import sympy as sp
s = sp.symbols("s", complex=True)
expr = (s + 2)*(s + 10)/(s**4 + 8*s**3 + 117*s**2 + 610*s + 500)

# %% [markdown] 
# The SymPy `apart()`{.py} method can be directly applied to find the partial fraction expansion:
# %%
expr.apart()

# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="last_expr"