Load SymPy as follows:

``` python
import sympy as sp
```

Now define the symbolic variables:

``` python
w, x, y, z = sp.symbols("w, x, y, z", complex=True)
```

Define the set of equations:

``` python
S = [
	8*w - 6*x + 5*y + 4*z + 20,  # == 0
	2*y - 2*z - 10,  # == 0
	2*w - x + 4*y + z,  # == 0
	w + 4*x - 2*y + 8*z - 4, # == 0
]
```

Let's try `sp.solve()`{.py}, as follows:

``` python
sol = sp.solve(S, [w, x, y, z], dict=True)
print(sol)
```

::: {.output .stream .stdout}
    [{w: 564/85, x: 773/85, y: 14/85, z: -411/85}]
:::
