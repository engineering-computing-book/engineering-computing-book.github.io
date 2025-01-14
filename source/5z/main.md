First, load SymPy and define the expression:

``` python
import sympy as sp
s = sp.symbols("s", complex=True)
expr = (s + 2)*(s + 10)/(s**4 + 8*s**3 + 117*s**2 + 610*s + 500)
```

The SymPy `apart()`{.py} method can be directly applied to find the partial fraction expansion:

``` python
expr.apart()
```

::: {.output .execute_result execution_count="3"}
```{=latex}
$\displaystyle - \frac{2 \cdot \left(7 s - 136\right)}{253 \left(s^{2} + 2 s + 100\right)} + \frac{3}{92 \left(s + 5\right)} + \frac{1}{44 \left(s + 1\right)}$
```
:::
