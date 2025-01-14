Engineering analysis regularly includes calculus.
Derivatives with respect to time and differential equations (i.e., equations including derivatives) are the key mathematical models of rigid-body mechanics (e.g., statics and dynamics), solid mechanics (e.g., mechanics of materials), fluid mechanics, heat transfer, and electromagnetism.
Integration is necessary for solving differential equations and computing important quantities of interest.
Limits and series expansions are frequently used to in the analytic process to simplify equations and to estimate unkown quantities.
In other words, calculus is central to the enterprise of engineering analysis.

## Derivatives {#derivatives h="zt"}

In SymPy, it is possible to compute the derivative of an expression using the `diff()`{.py} function and method, as follows:

``` python
x, y = sp.symbols("x, y", real=True)
expr = x**2 + x*y + y**2
expr.diff(x)  # Or sp.diff(expr, x)
expr.diff(y)  # Or sp.diff(expr, y)
```

::: {.output .execute_result execution_count="2"}
```{=latex}
$\displaystyle 2 x + y$
```
:::

::: {.output .execute_result execution_count="2"}
```{=latex}
$\displaystyle x + 2 y$
```
:::

Higher-order derivatives can be computed by adding the corresponding integer, as in the following second derivative:

``` python
expr.diff(x, 2)  # Or sp.diff(expr, x, 2)
```

::: {.output .execute_result execution_count="3"}
```{=latex}
$\displaystyle 2$
```
:::

We can see that the partial derivative is applied to a multivariate expression.
The differentiation can be mixed, as well, as in the following example:

``` python
expr = x * y**2/(x**2 + y**2)
expr.diff(x, 1, y, 2).simplify()  # $\partial^3/\partial x \partial y^2$
```

::: {.output .execute_result execution_count="4"}
```{=latex}
$\displaystyle \frac{2 x^{2} \left(- x^{4} + 14 x^{2} y^{2} - 9 y^{4}\right)}{x^{8} + 4 x^{6} y^{2} + 6 x^{4} y^{4} + 4 x^{2} y^{6} + y^{8}}$
```
:::

The option `evaluate=False`{.py} will leave the derivative unevaluated until the `doit()`{.py} method is called, as in the following example:

``` python
expr = sp.sin(x)
expr2 = expr.diff(x, evaluate=False); expr2
expr2.doit()
```

::: {.output .execute_result execution_count="5"}
```{=latex}
$\displaystyle \frac{d}{d x} \sin{\left(x \right)}$
```
:::

::: {.output .execute_result execution_count="5"}
```{=latex}
$\displaystyle \cos{\left(x \right)}$
```
:::

The derivative of an undefined function is left unevaluated, as in the following case:

``` python
f = sp.Function("f", real=True)
expr = 3*f(x) + f(x)**2
expr.diff(x)
```

::: {.output .execute_result execution_count="6"}
```{=latex}
$\displaystyle 2 f{\left(x \right)} \frac{d}{d x} f{\left(x \right)} + 3 \frac{d}{d x} f{\left(x \right)}$
```
:::

\noindent
As we can see, the chain rule of differentiation was applied automatically.

Differentiation works element-wise on matrices and vectors, just as it works mathematically.
For instance,

``` python
v = sp.Matrix([[x**2], [x*y]])
v.diff(x)
```

::: {.output .execute_result execution_count="7"}
```{=latex}
$\displaystyle \left[\begin{matrix}2 x\\y\end{matrix}\right]$
```
:::

## Integrals {#integrals h="nd"}

To a symbolic integral in SymPy, use the `integrate()`{.py} function or method.
For an indefinite integral, pass only the variable over which to integrate, as in

``` python
x, y = sp.symbols("x, y", real=True)
expr = x + y
expr.integrate(x)  # Or sp.integrate(expr, x); $\int x + y\ dx$
```

::: {.output .execute_result execution_count="8"}
```{=latex}
$\displaystyle \frac{x^{2}}{2} + x y$
```
:::

\noindent
Note that no constant of integration is added, so you may need to add your own.

The definite integral can be computed by providing a triple, as in the following example,

``` python
sp.integrate(expr, (x, 0, 3))  # $\int_0^3 x + y\ dx$
sp.integrate(expr, (x, 1, y))  # $\int_1^y x + y\ dx$
```

::: {.output .execute_result execution_count="9"}
```{=latex}
$\displaystyle 3 y + \frac{9}{2}$
```
:::

::: {.output .execute_result execution_count="9"}
```{=latex}
$\displaystyle \frac{3 y^{2}}{2} - y - \frac{1}{2}$
```
:::

Multiple integrals can be computed in a similar fashion, as in the following examples:

``` python
sp.integrate(expr, (x, 0, 4), (y, 2, 3))  # $\int_2^3 \int_0^4 x + y\ dx dy$
```

::: {.output .execute_result execution_count="10"}
```{=latex}
$\displaystyle 18$
```
:::

To create an unevaluated integral object, use the `sp.Integral()`{.py} constructor.
To evaluate an unevaluated integral, use the `doit()`{.py} method, as follows:

``` python
expr2 = sp.Integral(expr, x); expr2  # Unevaluated
expr2.doit()  # Evaluate
```

::: {.output .execute_result execution_count="11"}
```{=latex}
$\displaystyle \int \left(x + y\right)\, dx$
```
:::

::: {.output .execute_result execution_count="11"}
```{=latex}
$\displaystyle \frac{x^{2}}{2} + x y$
```
:::

Integration works over piecewise functions, as in the following example:

``` python
f = sp.Piecewise((0, x < 0), (1, x >= 0)); f
sp.integrate(f, (x, -5, 5))
```

::: {.output .execute_result execution_count="12"}
```{=latex}
$\displaystyle \begin{cases} 0 & \text{for}\: x < 0 \\1 & \text{otherwise} \end{cases}$
```
:::

::: {.output .execute_result execution_count="12"}
```{=latex}
$\displaystyle 5$
```
:::

The `integrate()`{.py} function and method is very powerful, but it may not be able to integrate some functions.
In such cases, it returns an unevaluated integral.

## Limits {#limits h="1a"}

In SymPy, a limit can be computed via the `limit()`{.py} function and method.
The $\lim_{x\rightarrow 0}$ can be computed as follows:

``` python
sp.limit(sp.tanh(x)/x, x, 0)  # $\lim_{x\rightarrow 0} \tanh(x)/x$
```

::: {.output .execute_result execution_count="13"}
```{=latex}
$\displaystyle 1$
```
:::

The limit to infinity or negative infinity can be denoted using the `sp.oo`{.py} symbol, as follows:

``` python
sp.limit(2  - x * sp.exp(-x), x, sp.oo)  # $\lim_{x\rightarrow \infty} (1 - x e^{-x})$
```

::: {.output .execute_result execution_count="14"}
```{=latex}
$\displaystyle 2$
```
:::

The limit can be left unevaluated using the `sp.Limit()`{.py} constructor, as follows:

``` python
lim = sp.Limit(2  - x * sp.exp(-x), x, sp.oo); expr  # Unevaluated
lim.doit()  # Evaluate
```

::: {.output .execute_result execution_count="15"}
```{=latex}
$\displaystyle x + y$
```
:::

::: {.output .execute_result execution_count="15"}
```{=latex}
$\displaystyle 2$
```
:::

The limit can be taken from a direction using the optional fourth argument, as follows:

``` python
expr = 1/x
lim_neg = sp.Limit(expr, x, 0, "-"); lim_neg
lim_pos = sp.Limit(expr, x, 0, "+"); lim_pos
lim_neg.doit()
lim_pos.doit()
```

::: {.output .execute_result execution_count="16"}
```{=latex}
$\displaystyle \lim_{x \to 0^-} \frac{1}{x}$
```
:::

::: {.output .execute_result execution_count="16"}
```{=latex}
$\displaystyle \lim_{x \to 0^+} \frac{1}{x}$
```
:::

::: {.output .execute_result execution_count="16"}
```{=latex}
$\displaystyle -\infty$
```
:::

::: {.output .execute_result execution_count="16"}
```{=latex}
$\displaystyle \infty$
```
:::

## Taylor Series {#taylor-series h="wm"}

A Taylor series (i.e., Taylor expansion) is an infinite power series approximation of an infinitely differentiable function near some point.
For a function $f(x)$, the Taylor series at point $x_0$ is given by
$$
\sum_{n=0}^\infty \frac{f^{(n)}}{n!} (x - x_0)^n = f(x_0) + f'(x_0) (x - x_0) + \frac{f''(x_0)}{2!} (x - x_0)^2 + \cdots.
$$
We often represent terms with power order $m$ and greater with the [big-O notation]{.keyword} $O((x-x_0)^m)$.
For instance, for an expansion about $x_0 = 0$,
$$
\sum_{n=0}^\infty \frac{f^{(n)}}{n!} (x)^n = f(0) + f'(x_0) (x - x_0) + O(x^2).
$$

In SymPy, the Taylor series can be found via the `series()`{.py} function or method.
For instance,

``` python
f = sp.sin(x)
f.series(x0=0, n=4)  # Or sp.series(f, x0=0, n=4)
```

::: {.output .execute_result execution_count="17"}
```{=latex}
$\displaystyle x - \frac{x^{3}}{6} + O\left(x^{4}\right)$
```
:::

\noindent
The `sp.O()`{.py} function, which appears in this result, automatically absorbs higher-order terms.
For instance,

``` python
x**2 + x**4 + x** 5 + sp.O(x**4)
```

::: {.output .execute_result execution_count="18"}
```{=latex}
$\displaystyle x^{2} + O\left(x^{4}\right)$
```
:::

To remove the `sp.O()`{.py} function from an expression, call the `removeO()`{.py} method, as follows:

``` python
f.series(x0=0, n=4).removeO()
```

::: {.output .execute_result execution_count="19"}
```{=latex}
$\displaystyle - \frac{x^{3}}{6} + x$
```
:::

\noindent
Removing the higher-order terms is frequently useful when we would like to use the $n$th-order [Taylor polynomial]{.keyword}, a truncated Taylor series, as an approximation of a function.
