# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="all"
# %matplotlib inline
import engcom

# %% 
#### Import Packages {-}
# %%
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# %% [markdown]
#### Static Analysis {-}
#
# Using the method of joints, we proceed through the joints, summing forces in the $x$- and $y$-directions.
# We will assume all members are in tension, and their sign will be positive if this is the case and negative, otherwise.
# Beginning with joint A, which includes two reaction forces $R_{A_x}$ and $R_{A_y}$ from the support,
# \begin{align}
# \Sigma F_x &= 0; & R_{A_x} + F_{AD} + F_{AC} \cos\theta &=0 \\
# \Sigma F_y &= 0; & R_{A_y} - F_{AC} \sin\theta &= 0.
# \end{align}
# The angle $\theta$ is known in terms of the dimensions $w$ and $h$ as
# $$\theta = \arctan\frac{h}{w}.$$
# These equations can be encode symbolically as follows:
# %%
RAx, RAy, FAC, FAD, theta = sp.symbols(
	"RAx, RAy, FAC, FAD, theta", real=True
)
h, w = sp.symbols("h, w", positive=True)
eqAx = RAx + FAD + FAC * sp.cos(theta)
eqAy = RAy - FAC*sp.sin(theta)
theta_wh = sp.atan(h/w)

# %% [markdown]
# Proceeding to joint B, which also has two reaction forces $R_{B_x}$ and $R_{B_y}$,
# \begin{align}
# \Sigma F_x &= 0; & R_{B_x} + F_{BC} &= 0 \\
# \Sigma F_y &= 0; & R_{B_y} &= 0.
# \end{align}
# Encoding these equations,
# %%
RBx, RBy, FBC  = sp.symbols("RBx, RBy, FBC", real=True)
eqBx = RBx + FBC
eqBy = RBy

# %% [markdown]
# For joint C,
# \begin{align}
# \Sigma F_x &= 0; & -F_{BC} - F_{AC} \cos\theta &= 0 \\
# \Sigma F_y &= 0; & F_{CD} + F_{AC} \sin\theta &= 0.
# \end{align}
# Encoding these equations,
# %%
FCD = sp.symbols("FCD", real=True)
eqCx = -FBC - FAC * sp.cos(theta)
eqCy = FCD + FAC * sp.sin(theta)

# %% [markdown]
# For joint D, there is an applied load $\vec{f_D}$, so the analysis proceeds as follows:
# \begin{align}
# \Sigma F_x &= 0; & -F_{AD} - f_D \cos\frac{\pi}{4} &= 0 \\
# \Sigma F_y &= 0; & -F_{CD} - f_D \sin\frac{\pi}{4} &= 0.
# \end{align}
# Encoding these equations,
# %%
fD = sp.symbols("fD", positive=True)
eqDx = -FAD - fD * sp.cos(sp.pi/4)
eqDy = -FCD - fD * sp.sin(sp.pi/4)

# %% [markdown]
# In total, we have 8 force equations and 8 unknown forces (4 member forces and 4 reaction forces).
# Let's construct the system and solve it for the unkown forces, as follows:
# %%
S_forces = [
	eqAx, eqAy, eqBx, eqBy, eqCx, eqCy, eqDx, eqDy
]  # 8 force equations
member_forces = [FAC, FAD, FBC, FCD]  # 5 member forces
reaction_forces = [RAx, RAy, RBx, RBy]  # 3 reaction forces
forces_unknown = member_forces + reaction_forces  # 8 unkown forces
sol_forces = sp.solve(S_forces, forces_unknown, dict=True); sol_forces

# %% [markdown]
# This solution is in terms of $f_D$ and $\theta$.
# Because $w$ and $h$ are our design parameters, let's substitute `theta_wh`{.py}
# such that our solution is rewritten in terms of $f_D$, $w$, and $h$.
# Create a `dict`{.py} of solutions as follows:
# %%
forces_wh = {}  # Initialize
for force in forces_unknown:
	force_wh = force.subs(
		sol_forces[0]
	).subs(
		theta, theta_wh
	).simplify()
	forces_wh[force] = force_wh
	print(f"{force} = {force_wh}")

# %% [markdown]
# Identify the member forces in tension and compression as follows:
# %%
tension = []  # Initialize list
compression = []  # Initialize list
for force in member_forces:
    if forces_wh[force] > 0:
        tension.append(force)
        print(f"{force} is in tension")
    elif forces_wh[force] < 0:
        compression.append(force)
        print(f"{force} is in compression")
    else:
        print(f"{force} is a zero-force member")

# %% [markdown]
# Therefore, there are no zero-force members.
# The maximum compression depends on the ratio $w/h$.
# If $w/h = 1$, all three members in compression have the same compression of magnitude
# $$
# \frac{\sqrt{2}}{2} f_D.
# $$
# This is also the maximum compression if $w/h < 1$.
# If $w/h > 1$, the maximum compression is of magnitude
# $$
# \frac{\sqrt{2} w}{2 h} f_D.
# $$

# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="last_expr"