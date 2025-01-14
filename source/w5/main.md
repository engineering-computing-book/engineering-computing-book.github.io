A constant steady-state, $\bm{x}' = \bm{0}$ implies, from the state [@eq:state-space-model-state],
\begin{align}
\bm{0} &= A \overline{\bm{x}} + B \overline{\bm{u}} \Rightarrow \\
\overline{\bm{x}} &= -A^{-1} B \overline{\bm{u}}.
\end{align}
We are now ready to define `steady_state()`{.py} as follows:

``` python
def steady_state(A, B, u_const):
	"""Returns the symbolic constant steady state vector"""
	A = sp.Matrix(A)  # In case A isn't symbolic
	B = sp.Matrix(B)  # In case B isn't symbolic
	u_const = sp.Matrix(u_const)  # In case u_const isn't symbolic
	x_const = -A**-1 * B * u_const
	return x_const
```

The state-space output equation [@eq:state-space-model-output] is already solved for the output, so we are ready to write `steady_output()`{.py} as follows:

``` python
def steady_output(C, D, u_const, x_const):
	"""Returns the symbolic constant steady-state output vector"""
	C = sp.Matrix(C)  # In case C isn't symbolic
	D = sp.Matrix(D)  # In case D isn't symbolic
	u_const = sp.Matrix(u_const)  # In case u_const isn't symbolic
	x_const = sp.Matrix(x_const)  # In case x_const isn't symbolic
	y_const = C*x_const + D*u_const
	return y_const
```

Apply these functions to the given state-space model.
First, define the symbolic variables as follows:

``` python
R, L, C1 = sp.symbols("R, L, C1", positive=True)
VS_ = sp.symbols("VS_", real=True)  # Constant voltage source input
```

Now define the system and the constant input as follows:

``` python
A = sp.Matrix([[0, 1/C1], [-1/L, -R/L]])  # $A$
B = sp.Matrix([[0], [1/L]])  # $B$
C = sp.Matrix([[1, 0], [-1, -R]])  # $C$
D = sp.Matrix([[0], [1]])  # $D$
u_const = sp.Matrix([[VS_]])  # $\overline{\bm{u}}$
```

Find the constant steady state $\overline{\bm{x}}$ as follows:

``` python
x_const = steady_state(A, B, u_const)
print(x_const)
```

::: {.output .execute_result execution_count="7"}
```{=latex}
$\displaystyle \left[\begin{matrix}VS_{}\\0\end{matrix}\right]$
```
:::

Find the constant steady-state output $\overline{\bm{y}}$ as follows:

``` python
y_const = steady_output(C, D, u_const, x_const)
print(y_const)
```

::: {.output .execute_result execution_count="9"}
```{=latex}
$\displaystyle \left[\begin{matrix}VS_{}\\0\end{matrix}\right]$
```
:::
