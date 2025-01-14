First, load SymPy as follows:

``` python
import sympy as sp
```

Now define the symbolic variables and the equation:

``` python
x = sp.symbols("x", complex=True)
a, b, c = sp.symbols("a, b, c", positive=True)
eq = a*x**2 + b*x + c/x + b**2  # == 0
```

Let's try `sp.solve()`{.py}, as follows:

``` python
sol = sp.solve(eq, x, dict=True)
print(sol)
```

::: {.output .stream .stdout}
    [{x: -(-3*b**2/a + b**2/a**2)/(3*(sqrt(-4*(-3*b**2/a + b**2/a**2)**3 + (27*c/a - 9*b**3/a**2 + 2*b**3/a**3)**2)/2 + 27*c/(2*a) - 9*b**3/(2*a**2) + b**3/a**3)**(1/3)) - (sqrt(-4*(-3*b**2/a + b**2/a**2)**3 + (27*c/a - 9*b**3/a**2 + 2*b**3/a**3)**2)/2 + 27*c/(2*a) - 9*b**3/(2*a**2) + b**3/a**3)**(1/3)/3 - b/(3*a)}, {x: -(-3*b**2/a + b**2/a**2)/(3*(-1/2 - sqrt(3)*I/2)*(sqrt(-4*(-3*b**2/a + b**2/a**2)**3 + (27*c/a - 9*b**3/a**2 + 2*b**3/a**3)**2)/2 + 27*c/(2*a) - 9*b**3/(2*a**2) + b**3/a**3)**(1/3)) - (-1/2 - sqrt(3)*I/2)*(sqrt(-4*(-3*b**2/a + b**2/a**2)**3 + (27*c/a - 9*b**3/a**2 + 2*b**3/a**3)**2)/2 + 27*c/(2*a) - 9*b**3/(2*a**2) + b**3/a**3)**(1/3)/3 - b/(3*a)}, {x: -(-3*b**2/a + b**2/a**2)/(3*(-1/2 + sqrt(3)*I/2)*(sqrt(-4*(-3*b**2/a + b**2/a**2)**3 + (27*c/a - 9*b**3/a**2 + 2*b**3/a**3)**2)/2 + 27*c/(2*a) - 9*b**3/(2*a**2) + b**3/a**3)**(1/3)) - (-1/2 + sqrt(3)*I/2)*(sqrt(-4*(-3*b**2/a + b**2/a**2)**3 + (27*c/a - 9*b**3/a**2 + 2*b**3/a**3)**2)/2 + 27*c/(2*a) - 9*b**3/(2*a**2) + b**3/a**3)**(1/3)/3 - b/(3*a)}]
:::

This is a cubic solution, so it is unwieldy.
