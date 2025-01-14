An engineering analysis typically requires that a symbolic solution be applied via the substitution of numbers into a symbolic expression.
In [kn]{.hashref}, we considered how to subsitute numerical values into expressions using SymPy's `evalf()`{.py} method.
This is fine for a single value, but frequently an expression is to be evaluated at an array of numerical values.
Looping through the array and applying `evalf()`{.py} is cumbersome and computationally slow.
An easier and computationally efficient technique using the `sp.lambdify()`{.py} function is introduced in this section.
The function `sp.lambdify()`{.py} creates an efficient, numerically evaluable function from a SymPy expression.
The basic usage of the function is as follows:

``` python
x = sp.symbols("x", real=True)
expr = x**2 + 7
f = sp.lambdify(x, expr)
f(2)
```

::: {.output .execute_result execution_count="2"}
    11
:::

By default, if NumPy is present, `sp.lambdify()`{.py} vectorizes the function such that the function can be provided with NumPy array arguments and return NumPy array values.
However, it is best to avoid relying on the function's implicit behavior, which can change when different modules are present, it is best to provide the numerical module explicitly, as follows:

``` python
f = sp.lambdify(x, expr, modules="numpy")
f(np.array([1, 2, 3.5]))
```

::: {.output .execute_result execution_count="3"}
    array([ 8.  , 11.  , 19.25])
:::

Multiple arguments are supported, as in the following example:

``` python
x, y = sp.symbols("x, y", real=True)
expr = sp.cos(x) * sp.sin(y)
f = sp.lambdify([x, y], expr, modules="numpy")
f(3, 4)
```

::: {.output .execute_result execution_count="4"}
    0.7492287917633428
:::

\noindent
All the usual NumPy broadcasting rules will apply for the function.
For instance,

``` python
X = np.array([[1], [2]])  # 2x1 matrix
Y = np.array([[1, 2, 3]])  # 1x3 matrix
f(X, Y)
```

::: {.output .execute_result execution_count="5"}
    array([[ 0.45464871,  0.4912955 ,  0.07624747],
           [-0.35017549, -0.37840125, -0.05872664]])
:::

::: {.example h="5j"}

You are designing the circuit shown in [@fig:ur-circuit].
Treat the source voltage $V_S$, the source resistance $R_S$, and the overall circuit topology as known constants.
The circuit design requires the selection of resistances $R_1$, $R_2$, and $R_3$ such that the voltage across $R_3$, $v_{R_3} = V_{R_3}$, and the current through $R_1$, $i_{R_1} = I_{R_1}$, where $V_{R_3}$ and $I_{R_1}$ are known constants (i.e., design requirements).
Proceed through the following steps:

#. Solve for all the resistor voltages $v_{R_k}$ and currents $i_{R_k}$ in terms of known constants and $R_1$, $R_2$, and $R_3$ using circuit laws
#. Apply the constraints $v_{R_3} = V_{R_3}$ and $i_{R_1} = I_{R_1}$ to obtain two equations relating $R_1$, $R_2$, and $R_3$
#. Solve for $R_2$ and $R_3$ as functions of $R_1$ and known constants
#. Create a design graph for the selection of $R_1$, $R_2$, and $R_3$ given the following design parameters: $V_S = 10$ V, $R_S = 50$ $\Omega$, $V_{R_3} = 1$ V, and $I_{R_1} = 20$ mA.

![A resistor circuit design for [5j]{.hashref}.](figures/ur-circuit/ur-circuit){#fig:ur-circuit .figure .standalone .nofloat}

::: {.example-solution}

### Solve for the Resistor Voltages and Currents {-}

Each resistor has an unknown voltage and current.
We will develop and solve a system of equations using circuit laws.
Begin by defining symbolic variables as follows:

``` python
v_RS, i_RS, v_R1, i_R1, v_R2, i_R2, v_R3, i_R3 = sp.symbols(
	"v_RS, i_RS, v_R1, i_R1, v_R2, i_R2, v_R3, i_R3", real=True
)
viR_vars = [v_RS, i_RS, v_R1, i_R1, v_R2, i_R2, v_R3, i_R3]
R1, R2, R3 = sp.symbols("R1, R2, R3", positive=True)
V_S, R_S, V_R3, I_R1 = sp.symbols("V_S, R_S, V_R3, I_R1", real=True)
```

There are $4$ resistors, so there are $2\cdot 4 = 8$ unknown voltages and currents;
therefore, we need $8$ independent equations.
The first circuit law we apply is Ohm's law, which states that the ratio of voltage over current for a resistor is approximately constant.
Applying this to each resistor, we obtain the following $4$ equations:

``` python
Ohms_law = [
	v_RS - R_S*i_RS,  # == 0
	v_R1 - R1*i_R1,  # == 0
	v_R2 - R2*i_R2,  # == 0
	v_R3 - R3*i_R3,  # == 0
]
```

The second circuit law we apply is Kirchhoff's current law (KCL), which states that the sum of the current into a node must equal $0$.
Applying this to the upper-middle and upper-right nodes, we obtain the following $2$ equations:

``` python
KCL = [
	i_RS - i_R1 - i_R2,  # == 0
	i_R2 - i_R3,  # == 0
]
```

The third circuit law we apply is Kirchhoff's voltage law (KVL), which states that the sum of the voltage around a closed loop must equal $0$.
Applying this to the left and right inner loops, we obtain the following $2$ equations:

``` python
KVL = [
	V_S - v_R1 - v_RS,  # == 0
	v_R1 - v_R3 - v_R2, # == 0
]
```

Our collection of $8$ equations are independent because none can be derived from another.
They make a linear system of equations, which can be solved simultaneously as follows:

``` python
viR_sol = sp.solve(Ohms_law + KCL + KVL, viR_vars, dict=True)[0]
print(viR_sol)
```

::: {.output .execute_result execution_count="11"}
```{=latex}
$\displaystyle i_{R1} = \frac{V_{S} \left(R_{2} + R_{3}\right)}{R_{1} R_{2} + R_{1} R_{3} + R_{1} R_{S} + R_{2} R_{S} + R_{3} R_{S}}$
```
:::

::: {.output .execute_result execution_count="11"}
```{=latex}
$\displaystyle i_{R2} = \frac{R_{1} V_{S}}{R_{1} R_{2} + R_{1} R_{3} + R_{1} R_{S} + R_{2} R_{S} + R_{3} R_{S}}$
```
:::

::: {.output .execute_result execution_count="11"}
```{=latex}
$\displaystyle i_{R3} = \frac{R_{1} V_{S}}{R_{1} R_{2} + R_{1} R_{3} + R_{1} R_{S} + R_{2} R_{S} + R_{3} R_{S}}$
```
:::

::: {.output .execute_result execution_count="11"}
```{=latex}
$\displaystyle i_{RS} = \frac{V_{S} \left(R_{1} + R_{2} + R_{3}\right)}{R_{1} R_{2} + R_{1} R_{3} + R_{1} R_{S} + R_{2} R_{S} + R_{3} R_{S}}$
```
:::

::: {.output .execute_result execution_count="11"}
```{=latex}
$\displaystyle v_{R1} = \frac{R_{1} V_{S} \left(R_{2} + R_{3}\right)}{R_{1} R_{2} + R_{1} R_{3} + R_{1} R_{S} + R_{2} R_{S} + R_{3} R_{S}}$
```
:::

::: {.output .execute_result execution_count="11"}
```{=latex}
$\displaystyle v_{R2} = \frac{R_{1} R_{2} V_{S}}{R_{1} R_{2} + R_{1} R_{3} + R_{1} R_{S} + R_{2} R_{S} + R_{3} R_{S}}$
```
:::

::: {.output .execute_result execution_count="11"}
```{=latex}
$\displaystyle v_{R3} = \frac{R_{1} R_{3} V_{S}}{R_{1} R_{2} + R_{1} R_{3} + R_{1} R_{S} + R_{2} R_{S} + R_{3} R_{S}}$
```
:::

::: {.output .execute_result execution_count="11"}
```{=latex}
$\displaystyle v_{RS} = \frac{R_{S} V_{S} \left(R_{1} + R_{2} + R_{3}\right)}{R_{1} R_{2} + R_{1} R_{3} + R_{1} R_{S} + R_{2} R_{S} + R_{3} R_{S}}$
```
:::

### Apply the Requirement Constraints {-}

The requirements that $v_{R_3} = V_{R_3}$ and $i_{R_1} = I_{R_1}$ can be encoded symbolically as two equations as follows:

``` python
constraints = {v_R3: V_R3, i_R1: I_R1}  # Design constraints
constraint_equations = [
	sp.Eq(v_R3.subs(constraints), v_R3.subs(viR_sol)),
	sp.Eq(i_R1.subs(constraints), i_R1.subs(viR_sol)),
]
print(constraint_equations)
```

::: {.output .execute_result execution_count="13"}
```{=latex}
$\displaystyle V_{R3} = \frac{R_{1} R_{3} V_{S}}{R_{1} R_{2} + R_{1} R_{3} + R_{1} R_{S} + R_{2} R_{S} + R_{3} R_{S}}$
```
:::

::: {.output .execute_result execution_count="13"}
```{=latex}
$\displaystyle I_{R1} = \frac{R_{2} V_{S} + R_{3} V_{S}}{R_{1} R_{2} + R_{1} R_{3} + R_{1} R_{S} + R_{2} R_{S} + R_{3} R_{S}}$
```
:::

### Solve for Resistances {-}

The system of $2$ constraint equations and $3$ unkowns ($R_1$, $R_2$, and $R_3$) is underdetermined, which means there are infinite solutions.
The two equations can be solved for $R_1$ and $R_2$ in terms of $R_3$ and parameters as follows:

``` python
constraints_sol = sp.solve(
	constraint_equations, [R1, R2], dict=True
)[0]
print(constraints_sol)
```

::: {.output .execute_result execution_count="15"}
```{=latex}
$\displaystyle R_{1} = - R_{S} + \frac{V_{S}}{I_{R1}} - \frac{R_{S} V_{R3}}{I_{R1} R_{3}}$
```
:::

::: {.output .execute_result execution_count="15"}
```{=latex}
$\displaystyle R_{2} = \frac{- R_{3} \left(I_{R1} R_{S} + V_{R3} - V_{S}\right) - R_{S} V_{R3}}{V_{R3}}$
```
:::

### Create a Design Graph {-}

Applying the design parameters and defining numerically evaluable functions for $R_1$ and $R_2$ as functions of $R_3$,

``` python
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
```

And now we are ready to create the design graph, as follows:

``` python
R3_ = np.linspace(10, 100, 101)  # Values of $R_3$
fig, ax = plt.subplots()
ax.plot(R3_, R1_fun(R3_), label="$R_1$ ($\\Omega$)")
ax.plot(R3_, R2_fun(R3_), label="$R_2$ ($\\Omega$)")
ax.set_xlabel("$R_3$ ($\\Omega$)")
ax.legend()
ax.grid()
plt.show()
```

::: {.output .execute_result execution_count="18"}
![A design graph for resistors $R_1$, $R_2$, and $R_3$.](source/ur/figure-0.pgf){#fig:ur-figure-0 .figure .pgf}
:::

:::
:::
