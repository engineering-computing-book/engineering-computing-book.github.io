The formula for the power of each element is given, so we are ready to define `power()`{.py} as follows:

``` python
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
```

The formula for the energy stored or dissipated by each element is given, so we are ready to write `energy()`{.py} as follows:

``` python
def energy(F, G):
	"""Returns the energy stored for vectors F and G"""
	P = power(F, G)
	E = sp.integrate(P, (t, 0, t))
	return E
```

Apply these functions to the given $\bm{F}$ and $\bm{G}$.
First, define $\bm{F}$ and $\bm{G}$ as follows:

``` python
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
```

Now compute the energy:

``` python
E = energy(F, G).simplify()
print(E)
```

::: {.output .execute_result execution_count="6"}
```{=latex}
$\displaystyle \left[\begin{matrix}\frac{1}{2} - \frac{e^{- 2 t}}{2}\\\frac{1}{2} - \frac{e^{- 2 t}}{2}\\t - \frac{3}{2} + 2 e^{- t} - \frac{e^{- 2 t}}{2}\\\frac{1}{2} - e^{- t} + \frac{e^{- 2 t}}{2}\end{matrix}\right]$
```
:::
