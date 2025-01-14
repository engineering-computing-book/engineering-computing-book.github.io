Load packages:

``` python
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
```

## Define Classes {-}
We begin by defining the parameters and functions of time as SymPy symbolic variables and unspecified functions as follows:

``` python
R, L, C = sp.symbols("R, L, C", positive=True)
v_C, i_L, v_L, V_S = sp.symbols(
    "v_C, i_L, v_L, V_S", cls=sp.Function, real=True
)  # $v_C, i_L, V_S$
t = sp.symbols("t", real=True)
```

Now we can form the symbolic matrices and vectors:

``` python
A_ = sp.Matrix([[0, 1/C], [-1/L, -R/L]])  # $\mat{A}$
B_ = sp.Matrix([[0], [1/L]])  # $\mat{B}$
C_ = sp.Matrix([[1, 0], [-1, -R]])  # $\mat{C}$
D_ = sp.Matrix([[0], [1]])  # $\mat{D}$
x = sp.Matrix([[v_C(t)], [i_L(t)]])  # $\vec{x}$
u = sp.Matrix([[V_S(t)]])  # $\vec{u}$
y = sp.Matrix([[v_C(t)], [v_L(t)]])  # $\vec{y}$
```

The input and initial conditions can be encoded as follows:

``` python
u_subs = {V_S(t): 10}
ics = {v_C(0): 0, i_L(0): 0}
```

The set of first-order ODEs comprising the state equation can be defined as follows:

``` python
odes = x.diff(t) - A_*x - B_*u
print(odes)
```

::: {.output .execute_result execution_count="7"}
```{=latex}
$\displaystyle \left[\begin{matrix}\frac{d}{d t} v_{C}{\left(t \right)} - \frac{i_{L}{\left(t \right)}}{C}\\\frac{d}{d t} i_{L}{\left(t \right)} + \frac{R i_{L}{\left(t \right)}}{L} - \frac{V_{S}{\left(t \right)}}{L} + \frac{v_{C}{\left(t \right)}}{L}\end{matrix}\right]$
```
:::

``` python
x_sol = sp.dsolve(list(odes.subs(u_subs)), list(x), ics=ics)
```

The symbolic solutions for $\bm{x}(t)$ are lengthy expressions, so we don't print them here.
Now we can compute the output $\vec{y}(t)$ from [@eq:state-space-model-output] as follows:

``` python
x_sol_dict = {}  # Initialize
for eq in x_sol:
    x_sol_dict[eq.lhs] = eq.rhs  # Make a dict of solutions for subs
y_sol = (C_*x + D_*u).subs(x_sol_dict)  # Subs into output equation

# We will graph the output for the following set of parameters:
```

``` python
params = {
    R: 50,  # (Ohms)
    L: 10e-6,  # (H)
    C: 1e-9, # (F)
}
```

Create a numerically evaluable version of each function as follows:

``` python
v_C_ = sp.lambdify(
    t, y_sol[0].subs(params).subs(u_subs), modules="numpy"
)
v_L_ = sp.lambdify(
    t, y_sol[1].subs(params).subs(u_subs), modules="numpy"
)
```

Graph each solution as follows:

``` python
t_ = np.linspace(0, 0.000002, 201)
fig, axs = plt.subplots(2, sharex=True)
axs[0].plot(t_, v_C_(t_))
axs[1].plot(t_, v_L_(t_))
axs[1].set_xlabel("Time (s)")
axs[0].set_ylabel("$v_C(t)$ (rad/s)")
axs[1].set_ylabel("$v_L(t)$ (A)")
plt.show()
```

::: {.output .execute_result execution_count="13"}
![The state response to a $10$ V step input.](source/fj/figure-0.pgf){#fig:fj-figure-0 .figure .pgf}
:::

The output equation is trivial in this case, yielding only the state variable $\Omega_J(t)$, for which we have already solved.
Therefore, we have completed the analysis.
