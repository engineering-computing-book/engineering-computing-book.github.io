# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="all"
# %matplotlib inline
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# Engineering analysis regularly includes the solution of differential equations.
# [Differential equations]{.keyword} are those equations that contain derivatives.
# An [ordinary differential equation (ODE)]{.keyword} is a differential equation that contains only ordinary, as opposed to partial, derivatives.
# A [linear ODE]{.keyword}—one for which constant multiples and sums of solutions are also solutions—is an important type that represent [linear, time-varying (LTV) systems]{.keyword}.
# For this class of ODEs, it has been proven that for a set of initial conditions, a unique solution exists [@Kreyszig2010,p. 108].
#
# A [constant-coefficient, linear ODE]{.keyword} can represent [linear, time-invariant (LTI) systems]{.keyword}.
# An LTV or LTI system model can be represented as a scalar $n$th-order ODE, or as a system of $n$ 1st-order ODEs.
# As a scalar $n$th-order linear ODE, with independent time variable $t$, output function $y(t)$, forcing function $f(t)$, and constant coefficients $a_i$, has the form
# $$
# y^{(n)}(t) + a_{n-1} y^{(n-1)}(t) + \cdots a_1 y'(t) + a_0 y(t) = f(t).
# $$ {#eq:scalar-linear-ode}
# The forcing function $f(t)$ can be written as a linear combination of derivatives of the input function $u(t)$ with $m+1 \le n+1$ constant coefficients $b_j$, as follows:
# $$
# f(t) = b_{m} u^{(m)}(t) + b_{m-1} u^{(m-1)}(t) + \cdots + b_1 u'(t) + b_0 u(t).
# $$
# Alternatively, the same LTI system model can be represented by a system of $n$ 1st-order ODEs, which can be written in vector form as
# \begin{subequations}\label{eq:state-space-model}
# \begin{align}
# \vec{x}'(t) &= \mat{A} \vec{x}(t) + \mat{B} \vec{u}(t)\label{eq:state-space-model-state} \\
# \vec{y}(t) &= \mat{C} \vec{x}(t) + \mat{D} \vec{u}(t), \label{eq:state-space-model-output}
# \end{align}
# \end{subequations}
# where $\vec{x}(t)$ is called the state vector, $\vec{u}(t)$ is called the input vector, and $\vec{y}(t)$ is called the output vector (they are actually vector-valued functions of time), and $\mat{A}$, $\mat{B}$, $\mat{C}$, and $\mat{D}$ are matrices containing constants derived from system parameters (e.g., a mass, a spring constant, a capacitance, etc.).
# [@Eq:state-space-model] is called an LTI [state-space model]{.keyword}, and it is used to model a great many engineering systems.
#
# Solving ODEs and systems of ODEs is a major topic of mathematical engineering analysis.
# It is typically the primary topic of one required course and a secondary topic of several others.
# Understanding when these solutions exist, whether they are unique, and how they can be found adds much to the understanding of engineering systems.
# However, it is also true that CASs such as SymPy offer the engineer excellent tools for making quick and adaptable work of this task.
# 
# Consider the ODE
# $$
# 3 y'(t) + y(t) = f(t),
# $$
# where the forcing function $f(t)$ is defined piecewise as
# $$
# f(t) = \begin{cases} 0 & t < 0 \\ 1 & t \ge 0. \end{cases}
# $$
# The SymPy `dsolve()`{.py} function can find the [general solution]{.keyword} (i.e., a family of solutions for any initial conditions) with the following code:
# %%
t = sp.symbols("t", nonnegative=True)
y = sp.Function("y", real=True)
f = 1  # Or sp.Piecewise(), but $t \ge 0$ already restricts $f(t)$
ode = sp.Eq(3*y(t).diff(t) + y(t), f)  # Define the ODE
sol = sp.dsolve(ode, y(t)); sol  # Solve

# %% [markdown]
# \noindent
# The solution is returned as an `sp.Eq()`{.py} equation object.
# Note the unknown constant $C_1$ in the solution.
# To find the [specific solution]{.keyword} (i.e., the general solution with the initial condition applied to determine $C_1$) for a given initial condition $y(0) = 5$,
# %%
sol = sp.dsolve(ode, y(t), ics={y(0): 5}); sol

# %% [markdown]
# Now consider the ODE
# $$
# y''(t) + 5 y'(t) + 9 y(t) = 0.
# $$
# The SymPy `dsolve()`{.py} function can find the general solution with the following code:
# %%
ode = sp.Eq(y(t).diff(t, 2) + 5*y(t).diff(t) + 9*y(t), 0)
sol = sp.dsolve(ode, y(t)); sol

# %% [markdown]
# \noindent
# This is a decaying sinusoid.
# Applying two initial conditions, $y(0) = 4$ and $y'(0) = 0$, we obtain the following:
# %%
sol = sp.dsolve(
    ode, y(t), 
    ics={y(0): 4, y(t).diff(t).subs(t, 0): 0}
); sol

# %% [markdown]
# \noindent
# We see here that to apply the initial condition $y'(0) = 0$, the derivative must be applied before substituting $t \rightarrow 0$.
# 
# Solving sets (i.e., systems) of first-order differential equations is similar.
# Consider the set of differential equations
# $$
# y_1'(t) = y_2(t) - y_1(t) \text{ and } y_2'(t) = y_1(t) - y_2(t).
# $$
# To find the solution for initial conditions $y_1(0) = 1$ and $y_2(0) = -1$, we can use the following technique:
# %%
t = sp.symbols("t", nonnegative=True)
y1, y2 = sp.symbols("y1, y2", cls=sp.Function, real=True)
odes = [y1(t).diff(t) + y1(t) - y2(t), y2(t).diff(t) + y2(t) - y1(t)]
ics = {y1(0): 1, y2(0): -1}
sol = sp.dsolve(odes, [y1(t), y2(t)], ics=ics)
print(sol)

# %% [markdown]
# In engineering, it is common to express a set of differential equations as a state-space model, as in [@eq:state-space-model].
# The following example demonstrates how to solve these with SymPy.
#
# ::: {.example h="m4"}
#
# Consider the electromechanical schematic of a direct current (DC) motor shown in [@fig:motor-circuit].
# A voltage source $V_S(t)$ provides power, the armature winding loses some energy to heat through a resistance $R$ and stores some energy in a magnetic field due to its inductance $L$, which arises from its coiled structure.
# An electromechanical interaction through the magnetic field, shown as M, has torque constant $K_M$ and induces a torque on the motor shaft, which is supported by bearings that lose some energy to heat via a damping coefficient $B$.
# The rotor's mass has rotational moment of inertia $J$, which stores kinetic energy.
# We denote the voltage across an element with $v$, the current through an element with $i$, the angular velocity across an element with $\Omega$, and the torque through an element with $T$.
#
# ![An electromechanical schematic of a DC motor.](figures/motor-circuit/motor-circuit){#fig:motor-circuit .figure .standalone .nofloat color=bw}
#
# A state-space model state equation in the form of [@eq:state-space-model-state] can be derived for this system, with the result as follows:
# 
# $$
# \underbrace{
# \frac{d}{d t}
# \begin{bmatrix} 
# \Omega_J \\ i_L
# \end{bmatrix}
# }_{\vec{x}'(t)} = 
# \underbrace{
# \begin{bmatrix}
#   -B/J & K_M/J \\
#   -K_M/L & -R/L
# \end{bmatrix}
# }_{\mat{A}}
# \underbrace{
# \begin{bmatrix} 
# \Omega_J \\ i_L
# \end{bmatrix}
# }_{\vec{x}(t)} + 
# \underbrace{
# \begin{bmatrix}
# 0 \\ 1/L
# \end{bmatrix}
# }_{\mat{B}}
# \underbrace{
# \begin{bmatrix} 
# V_S
# \end{bmatrix}
# \vphantom{\begin{bmatrix}0\\0\end{bmatrix}}
# }_{\vec{u}(t)}.
# $$
# We choose $\vec{y} = \begin{bmatrix} \Omega_J \end{bmatrix}$ as the output vector, which yields output equation (i.e., [@eq:state-space-model-output])
# $$
# \underbrace{
# \begin{bmatrix} \Omega_J \end{bmatrix}
# \vphantom{\begin{bmatrix}0\\0\end{bmatrix}}
# }_{\vec{y}(t)} = 
# \underbrace{
# \begin{bmatrix} 1 & 0 \end{bmatrix}
# \vphantom{\begin{bmatrix}0\\0\end{bmatrix}}
# }_{\mat{C}}
# \underbrace{
# \begin{bmatrix} 
# \Omega_J \\ i_L
# \end{bmatrix}
# }_{\vec{x}(t)} + 
# \underbrace{
# \begin{bmatrix} 0 \end{bmatrix}
# \vphantom{\begin{bmatrix}0\\0\end{bmatrix}}
# }_{\mat{D}} 
# \underbrace{
# \begin{bmatrix} 
# V_S
# \end{bmatrix}
# \vphantom{\begin{bmatrix}0\\0\end{bmatrix}}
# }_{\vec{u}(t)}.
# $$
# Together, these equations are a state-space model for the system.
#
# Solve the state equation for $\vec{x}(t)$ and the output equation for $\vec{y}(t)$ for the following case:
# 
# - The input voltage $V_S(t) = 1$ V for $t \ge 0$
# - The initial condition is $\vec{x}(0) = \vec{0}$
# 
# ::: {.example-solution}
#
# We begin by defining the parameters and functions of time as SymPy symbolic variables and unspecified functions as follows:
# %%
R, L, K_M, B, J = sp.symbols("R, L, K_M, B, J", positive=True)
W_J, i_L, V_S = sp.symbols(
    "W_J, i_L, V_S", cls=sp.Function, real=True
)  # $\Omega_J, i_L, V_S$
t = sp.symbols("t", real=True)

# %% [markdown]
# Now we can form the symbolic matrices and vectors:
# %%
A_ = sp.Matrix([[-B/J, K_M/J], [-K_M/L, -R/L]])  # $\mat{A}$
B_ = sp.Matrix([[0], [1/L]])  # $\mat{B}$
C_ = sp.Matrix([[1, 0]])  # $\mat{C}$
D_ = sp.Matrix([[0]])  # $\mat{D}$
x = sp.Matrix([[W_J(t)], [i_L(t)]])  # $\vec{x}$
u = sp.Matrix([[V_S(t)]])  # $\vec{u}$
y = sp.Matrix([[W_J(t)]])  # $\vec{y}$

# %% [markdown]
# The input and initial conditions can be encoded as follows:
# %%
u_subs = {V_S(t): 1}
ics = {W_J(0): 0, i_L(0): 0}

# %% [markdown]
# The set of first-order ODEs comprising the state equation can be defined as follows:
# %% tags=["remove_output"]
odes = x.diff(t) - A_*x - B_*u
print(odes)

# %% tags=["remove_input"]
odes

# %%
x_sol = sp.dsolve(list(odes.subs(u_subs)), list(x), ics=ics)

# %% [markdown]
# The symbolic solutions for $\bm{x}(t)$ are lengthy expressions.
# Instead of printing them, we will graph them for the following set of parameters:
# %%
params = {
    R: 1,  # (Ohms)
    L: 0.1e-6,  # (H)
    K_M: 7,  # (N$\cdot$m/A)
    B: 0.1e-6,  # (N$\cdot$m/(rad/s))
    J: 2e-6,  # (kg$\cdot$m$^2$)
}

# %% [markdown]
# Create a numerically evaluable version of each function as follows:
# %%
W_J_ = sp.lambdify(t, x_sol[0].rhs.subs(params), modules="numpy")
i_L_ = sp.lambdify(t, x_sol[1].rhs.subs(params), modules="numpy")

# %% [markdown]
# Graph each solution as follows:
# %% tags=["remove_output"]
t_ = np.linspace(0, 0.000002, 201)
fig, axs = plt.subplots(2, sharex=True)
axs[0].plot(t_, W_J_(t_))
axs[1].plot(t_, i_L_(t_))
axs[1].set_xlabel("Time (s)")
axs[0].set_ylabel("$\\Omega_J(t)$ (rad/s)")
axs[1].set_ylabel("$i_L(t)$ (A)")
plt.show()

# %% tags=["remove_input"]
import engcom
engcom.show(fig, caption=f"The state response to a unit step voltage input.")

# %% [markdown]
# The output equation is trivial in this case, yielding only the state variable $\Omega_J(t)$, for which we have already solved.
# Therefore, we have completed the analysis.

# %% [markdown]
#
# :::
# :::
#


# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="last_expr"