# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="all"
# %matplotlib inline
import engcom
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from IPython.display import display, Math, Latex

# %% [markdown]
# An engineering analysis typically requires that a symbolic solution be applied via the substitution of numbers into a symbolic expression.
# In [kn]{.hashref}, we considered how to subsitute numerical values into expressions using SymPy's `evalf()`{.py} method.
# This is fine for a single value, but frequently an expression is to be evaluated at an array of numerical values.
# Looping through the array and applying `evalf()`{.py} is cumbersome and computationally slow.
# An easier and computationally efficient technique using the `sp.lambdify()`{.py} function is introduced in this section.
# The function `sp.lambdify()`{.py} creates an efficient, numerically evaluable function from a SymPy expression.
# The basic usage of the function is as follows:
# %%
x = sp.symbols("x", real=True)
expr = x**2 + 7
f = sp.lambdify(x, expr)
f(2)

# %% [markdown]
# By default, if NumPy is present, `sp.lambdify()`{.py} vectorizes the function such that the function can be provided with NumPy array arguments and return NumPy array values.
# However, it is best to avoid relying on the function's implicit behavior, which can change when different modules are present, it is best to provide the numerical module explicitly, as follows:
# %%
f = sp.lambdify(x, expr, modules="numpy")
f(np.array([1, 2, 3.5]))

# %% [markdown]
# Multiple arguments are supported, as in the following example:
# %%
x, y = sp.symbols("x, y", real=True)
expr = sp.cos(x) * sp.sin(y)
f = sp.lambdify([x, y], expr, modules="numpy")
f(3, 4)

# %% [markdown]
# \noindent
# All the usual NumPy broadcasting rules will apply for the function.
# For instance,
# %%
X = np.array([[1], [2]])  # 2x1 matrix
Y = np.array([[1, 2, 3]])  # 1x3 matrix
f(X, Y)

# %% [markdown]
#
# ::: {.example h="5j"}
#
# You are designing the circuit shown in [@fig:ur-circuit].
# Treat the source voltage $V_S$, the source resistance $R_S$, and the overall circuit topology as known constants.
# The circuit design requires the selection of resistances $R_1$, $R_2$, and $R_3$ such that the voltage across $R_3$, $v_{R_3} = V_{R_3}$, and the current through $R_1$, $i_{R_1} = I_{R_1}$, where $V_{R_3}$ and $I_{R_1}$ are known constants (i.e., design requirements).
# Proceed through the following steps:
#
# #. Solve for all the resistor voltages $v_{R_k}$ and currents $i_{R_k}$ in terms of known constants and $R_1$, $R_2$, and $R_3$ using circuit laws
# #. Apply the constraints $v_{R_3} = V_{R_3}$ and $i_{R_1} = I_{R_1}$ to obtain two equations relating $R_1$, $R_2$, and $R_3$
# #. Solve for $R_2$ and $R_3$ as functions of $R_1$ and known constants
# #. Create a design graph for the selection of $R_1$, $R_2$, and $R_3$ given the following design parameters: $V_S = 10$ V, $R_S = 50$ $\Omega$, $V_{R_3} = 1$ V, and $I_{R_1} = 20$ mA.
#
# ![A resistor circuit design for [5j]{.hashref}.](figures/ur-circuit/ur-circuit){#fig:ur-circuit .figure .standalone .nofloat}
#
# ::: {.example-solution}
#
#### Solve for the Resistor Voltages and Currents {-}
#
# Each resistor has an unknown voltage and current.
# We will develop and solve a system of equations using circuit laws.
# Begin by defining symbolic variables as follows:
# %%
v_RS, i_RS, v_R1, i_R1, v_R2, i_R2, v_R3, i_R3 = sp.symbols(
	"v_RS, i_RS, v_R1, i_R1, v_R2, i_R2, v_R3, i_R3", real=True
)
viR_vars = [v_RS, i_RS, v_R1, i_R1, v_R2, i_R2, v_R3, i_R3]
R1, R2, R3 = sp.symbols("R1, R2, R3", positive=True)
V_S, R_S, V_R3, I_R1 = sp.symbols("V_S, R_S, V_R3, I_R1", real=True)

# %% [markdown]
# There are $4$ resistors, so there are $2\cdot 4 = 8$ unknown voltages and currents;
# therefore, we need $8$ independent equations.
# The first circuit law we apply is Ohm's law, which states that the ratio of voltage over current for a resistor is approximately constant.
# Applying this to each resistor, we obtain the following $4$ equations:
# %%
Ohms_law = [
	v_RS - R_S*i_RS,  # == 0
	v_R1 - R1*i_R1,  # == 0
	v_R2 - R2*i_R2,  # == 0
	v_R3 - R3*i_R3,  # == 0
]

# %% [markdown]
# The second circuit law we apply is Kirchhoff's current law (KCL), which states that the sum of the current into a node must equal $0$.
# Applying this to the upper-middle and upper-right nodes, we obtain the following $2$ equations:
# %%
KCL = [
	i_RS - i_R1 - i_R2,  # == 0
	i_R2 - i_R3,  # == 0
]

# %% [markdown]
# The third circuit law we apply is Kirchhoff's voltage law (KVL), which states that the sum of the voltage around a closed loop must equal $0$.
# Applying this to the left and right inner loops, we obtain the following $2$ equations:
# %%
KVL = [
	V_S - v_R1 - v_RS,  # == 0
	v_R1 - v_R3 - v_R2, # == 0
]

# %% [markdown]
# Our collection of $8$ equations are independent because none can be derived from another.
# They make a linear system of equations, which can be solved simultaneously as follows:
# %% tags=["remove_output"]
viR_sol = sp.solve(Ohms_law + KCL + KVL, viR_vars, dict=True)[0]
print(viR_sol)

# %% tags=["remove_input"]
for viR_key, viR_val in viR_sol.items():
	sp.Eq(viR_key, viR_val.simplify())

# %% [markdown]
#### Apply the Requirement Constraints {-}
#
# The requirements that $v_{R_3} = V_{R_3}$ and $i_{R_1} = I_{R_1}$ can be encoded symbolically as two equations as follows:
# %% tags=["remove_output"]
constraints = {v_R3: V_R3, i_R1: I_R1}  # Design constraints
constraint_equations = [
	sp.Eq(v_R3.subs(constraints), v_R3.subs(viR_sol)),
	sp.Eq(i_R1.subs(constraints), i_R1.subs(viR_sol)),
]
print(constraint_equations)

# %% tags=["remove_input"]
for eq in constraint_equations:
	eq

# %% [markdown]
#### Solve for Resistances {-}
#
# The system of $2$ constraint equations and $3$ unkowns ($R_1$, $R_2$, and $R_3$) is underdetermined, which means there are infinite solutions.
# The two equations can be solved for $R_1$ and $R_2$ in terms of $R_3$ and parameters as follows:
# %% tags=["remove_output"]
constraints_sol = sp.solve(
	constraint_equations, [R1, R2], dict=True
)[0]
print(constraints_sol)

# %% tags=["remove_input"]
for con_key, con_val in constraints_sol.items():
	sp.Eq(
		con_key, 
		engcom.apply_to_numden(con_val.simplify(), lambda x: sp.collect(x, R3)).simplify()
	)

# %% [markdown]
#### Create a Design Graph {-}
#
# Applying the design parameters and defining numerically evaluable functions for $R_1$ and $R_2$ as functions of $R_3$,
# %%
design_params = {V_S: 10, R_S: 50, V_R3: 1, I_R1: 0.02}
R1_fun = sp.lambdify(
	[R3],
	R1.subs(constraints_sol).subs(design_params),
	modules="numpy",
)
R2_fun = sp.lambdify(
	[R3],
	R2.subs(constraints_sol).subs(design_params),
	modules="numpy",
)

# %% [markdown]
# And now we are ready to create the design graph, as follows:
# %% tags=["remove_output"]
R3_ = np.linspace(10, 100, 101)  # Values of $R_3$
fig, ax = plt.subplots()
ax.plot(R3_, R1_fun(R3_), label="$R_1$ ($\\Omega$)")
ax.plot(R3_, R2_fun(R3_), label="$R_2$ ($\\Omega$)")
ax.set_xlabel("$R_3$ ($\\Omega$)")
ax.legend()
ax.grid()
plt.show()

# %% tags=["remove_input"]
engcom.show(fig, caption="A design graph for resistors $R_1$, $R_2$, and $R_3$.")

# %% [markdown]
#
# :::
# :::

# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="last_expr"