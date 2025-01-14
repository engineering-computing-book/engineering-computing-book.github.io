In engineering symbolic analysis, the need to manipulate, often algebraically, mathematical expressions arises constantly.
SymPy has several powerful tools for manipulating symbolic expressions, the most useful of which we will consider here.

## The `simplify()` Function and Method {#simplify-function-method h="9r"}

A built-in Sympy function and method, `sp.simplify()`{.py}, is a common SymPy tool for manipulation because simplification is often what we want.
Recall that some basic simplification occurs automatically; however, in many cases this automatic simplification is insufficient.
Applying `sp.simplify()`{.py} typically results in an expression as simple as or simpler than its input; however, the precise meaning of "simpler" is quite vague, which can lead to frustrating cases in which a version of an expression we consider to be simpler is not chosen by the `sp.simplify()`{.py} algorithm.
In such cases, we will often use the more manual techniques considered later in this section.

The predicates (i.e., assumptions) used to define the symbolic variables and functions that appear in a symbolic expression are respected by `sp.simplify()`{.py}.
Consider the following example:

``` python
x = sp.symbols("x", real=True)
e0 = (x**2 + 2*x + 3*x)/(x**2 + 2*x); e0  # For display
e0.simplify()  # Returns simplified expression, leaves e0 unchanged
```

::: {.output .execute_result execution_count="3"}
```{=latex}
$\displaystyle \frac{x^{2} + 5 x}{x^{2} + 2 x}$
```
:::

::: {.output .execute_result execution_count="3"}
```{=latex}
$\displaystyle \frac{x + 5}{x + 2}$
```
:::

\noindent
Note that `e0`{.py} was slightly simplified automatically.
The `simplify()`{.py} method further simplified by canceling an `x`{.py}. 
The use of the method does not affect the object, so it the same as the use of the function.

There are a few "knobs" to turn in the form of optional arguments to `sp.simplify()`{.py}:

- `measure`{.py} (default: `sp.count_ops()`{.py}): A function that serves as a heuristic complexity metric. The default `sp.count_ops()`{.py} counts the operations in the expression.
- `ratio`{.py} (default: `1.7`{.py}): The maximum ratio of the measures, output `out`{.py} over input `inp`{.py}, `measure(out)/measure(inp)`{.py}. Anything over `1`{.py} allows the output to be potentially more complex than the input, but it may still be simpler because the metric is just a heuristic.
- `rational`{.py} (default: `False`{.py}): By default (`False`{.py}), floating-point numbers are left alone. If `rational=True`{.py}, floating-point numbers are recast as rational numbers. If `rational=None`{.py}, floating-point numbers are recast as rational numbers during simplification, but recast to floating-point numbers in the result.
- `inverse`{.py} (default: `False`{.py}): If `True`{.py}, allows inverse functions to be cancelled in any order without knowing if the inner argument falls in the domain for which the inverse holds.[^fn:inverse-principal-branch] For instance, this allows $\arccos(\cos x) \rightarrow x$ without knowing if $x \in [0, \pi]$.
- `force`{.py} (default: `False`{.py}): If `True`{.py}, predicates (assumptions) of the variables will be ignored.

[^fn:inverse-principal-branch]: The usual way of defining the inverse $y = \arccos x$ is to retrict $y$ in $x = \cos y$ to $[0, \pi]$. This is because $\cos$ is not one-to-one (e.g., $\cos 0 = \cos 2\pi = 1$), so its domain must be restricted for a proper inverse to exist. The conventional choice of domain restriction to $[0, \pi]$ is called the selection of a principal branch.

## Polynomial and Rational Expression Manipulation {#polynomial-rational-expressions h="nv"}

Here we consider a few SymPy functions and methods that manipulate polynomials and rational expressions.

### The `expand()` Function and Method

The `expand()`{.py} function and method expresses a polynomial in the canonical form of a sum of monomials.
A monomial is a polynomial with exactly one additive term.
For instance,

``` python
sp.expand((x + 3)**2)  ## Using the real x from above
```

::: {.output .execute_result execution_count="4"}
```{=latex}
$\displaystyle x^{2} + 6 x + 9$
```
:::

We can also expand a numerator or denominator without expanding the entire expression, as follows for $(x+3)^2/(x - 2)^2$:

``` python
frac = (x + 3)**2/(x - 2)**2
frac.expand()
frac.expand(numer=True)
frac.expand(denom=True)
frac.expand(numer=True).expand(denom=True)
```

::: {.output .execute_result execution_count="5"}
```{=latex}
$\displaystyle \frac{x^{2}}{x^{2} - 4 x + 4} + \frac{6 x}{x^{2} - 4 x + 4} + \frac{9}{x^{2} - 4 x + 4}$
```
:::

::: {.output .execute_result execution_count="5"}
```{=latex}
$\displaystyle \frac{x^{2} + 6 x + 9}{\left(x - 2\right)^{2}}$
```
:::

::: {.output .execute_result execution_count="5"}
```{=latex}
$\displaystyle \frac{\left(x + 3\right)^{2}}{x^{2} - 4 x + 4}$
```
:::

::: {.output .execute_result execution_count="5"}
```{=latex}
$\displaystyle \frac{x^{2} + 6 x + 9}{x^{2} - 4 x + 4}$
```
:::

There are several additional options for `expand()`{.py}, including:

- `mul`{.py} (default: `True`{.py}): If `True`{.py}, distributes multiplication over addition (e.g., $5 (x + 1) \rightarrow 5 x + 5$.
- `multinomial`{.py} (default: `True`{.py}): If `True`{.py}, expands multinomial (polynomial that is not a monomial) terms into sums of monomials (e.g., $(x + y)^2 \rightarrow x^2 + 2 x y + y^2$).
- `power_exp`{.py} (default: `True`{.py}): If `True`{.py}, expands sums in exponents to products of exponentials (e.g., $e^{3 + x} \rightarrow e^3 e^x$).
- `log`{.py} (default: `True`{.py}): If `True`{.py}, split log products into sums and extract log exponents to multiplicative constants (e.g., for $x, y > 0$, $\ln(x^3 y) \rightarrow 3\ln x + \ln y$).
- `deep`{.py} (default: `True`{.py}): If `True`{.py}, expands all levels of the expression tree; if `False`{.py}, expands only the top level (e.g., $x (x + (y+1)^2) \rightarrow x^2 + x (y+1)^2$).
- `complex` (default: `False`{.py}): If `True`{.py}, collect real and imaginary parts (e.g., $x + y \rightarrow \Re(x) + \Re(y) + j (\Im(x) + \Im(y))$).
- `func`{.py} (default: `False`{.py}): If `True`{.py}, expand nonpolynomial functions (e.g., for the gamma function $\Gamma$, $\Gamma(x+2) \rightarrow x^2 \Gamma(x) + x \Gamma(x)$).
- `trig`{.py} (default: `False`{.py}): If `True`{.py}, expand trigonometric functions (e.g., $\sin(x+y) \rightarrow \sin x \cos y -  \sin y \cos x$).

### The `factor()` Function and Method

The `factor()`{.py} function and method returns a factorization into irreducibles factors.
For polynomials, this is the reverse of `expand()`{.py}.
Irreducibility of the factors is guaranteed for polynomials.
Consider the following polynomial example:

``` python
x, y = sp.symbols("x, y", real=True)
e0 = (x + 1)**2 * (x**2 + 2*x*y + y**2); e0
e0.expand()
e0.expand().factor()
```

::: {.output .execute_result execution_count="6"}
```{=latex}
$\displaystyle \left(x + 1\right)^{2} \left(x^{2} + 2 x y + y^{2}\right)$
```
:::

::: {.output .execute_result execution_count="6"}
```{=latex}
$\displaystyle x^{4} + 2 x^{3} y + 2 x^{3} + x^{2} y^{2} + 4 x^{2} y + x^{2} + 2 x y^{2} + 2 x y + y^{2}$
```
:::

::: {.output .execute_result execution_count="6"}
```{=latex}
$\displaystyle \left(x + 1\right)^{2} \left(x + y\right)^{2}$
```
:::

Factorization can also be performed over nonpolynomial expressions, as in the following example:

``` python
e1 = sp.sin(x) * (sp.cos(x) + sp.sin(x))**2; e1  # Using above real x
e1.expand()
e1.expand().factor()
```

::: {.output .execute_result execution_count="7"}
```{=latex}
$\displaystyle \left(\sin{\left(x \right)} + \cos{\left(x \right)}\right)^{2} \sin{\left(x \right)}$
```
:::

::: {.output .execute_result execution_count="7"}
```{=latex}
$\displaystyle \sin^{3}{\left(x \right)} + 2 \sin^{2}{\left(x \right)} \cos{\left(x \right)} + \sin{\left(x \right)} \cos^{2}{\left(x \right)}$
```
:::

::: {.output .execute_result execution_count="7"}
```{=latex}
$\displaystyle \left(\sin{\left(x \right)} + \cos{\left(x \right)}\right)^{2} \sin{\left(x \right)}$
```
:::

There are two options of note:

- `deep`{.py} (default: `False`{.py}): If `True`{.py}, inner expression tree elements will also be factored (e.g., $\exp(x^2 + 4 x + 4) \rightarrow \exp((x+2)^2)$).
- `fraction`{.py} (default: `True`{.py}): If `True`{.py}, rational expressions will be combined.

\noindent
An example of the latter option is given here:

``` python
e2 = x - 5*sp.exp(3 - x); e2  # Using real x from above
e2.factor(deep=True)
e2.factor(deep=True, fraction=False)
```

::: {.output .execute_result execution_count="8"}
```{=latex}
$\displaystyle x - 5 e^{3 - x}$
```
:::

::: {.output .execute_result execution_count="8"}
```{=latex}
$\displaystyle \left(x e^{x} - 5 e^{3}\right) e^{- x}$
```
:::

::: {.output .execute_result execution_count="8"}
```{=latex}
$\displaystyle x - 5 e^{3} e^{- x}$
```
:::

### The `collect()` Function and Method

The `collect()`{.py} function and method returns an expression with specific terms collected.
For instance,

``` python
x, y, a, b = sp.symbols("x, y, a, b", real=True)
e3 = a * x + b * x * y + a**2 * x**2 + 3 * y**2 + x * y + 8; e3
e3.collect(x)
```

::: {.output .execute_result execution_count="9"}
```{=latex}
$\displaystyle a^{2} x^{2} + a x + b x y + x y + 3 y^{2} + 8$
```
:::

::: {.output .execute_result execution_count="9"}
```{=latex}
$\displaystyle a^{2} x^{2} + x \left(a + b y + y\right) + 3 y^{2} + 8$
```
:::

More complicated expressions can be collected as well, as in the following example:

``` python
e4 = a*sp.cos(4*x) + b*sp.cos(4*x) + b*sp.cos(6*x) + a * sp.sin(x); e4
e4.collect(sp.cos(4*x))
```

::: {.output .execute_result execution_count="10"}
```{=latex}
$\displaystyle a \sin{\left(x \right)} + a \cos{\left(4 x \right)} + b \cos{\left(4 x \right)} + b \cos{\left(6 x \right)}$
```
:::

::: {.output .execute_result execution_count="10"}
```{=latex}
$\displaystyle a \sin{\left(x \right)} + b \cos{\left(6 x \right)} + \left(a + b\right) \cos{\left(4 x \right)}$
```
:::

Derivatives of an undefined symbolic function, as would appear in a differential equation, can be collected. If the function is passed to `collect()`{.py}, as in the following example, it and its derivatives are collected:

``` python
f = sp.Function("f")(x)  ## Applied undefined function
e5 = a*f.diff(x, 2) + a**2*f.diff(x) + b**2*f.diff(x) + a**3*f; e5
e5.collect(f)
```

::: {.output .execute_result execution_count="11"}
```{=latex}
$\displaystyle a^{3} f{\left(x \right)} + a^{2} \frac{d}{d x} f{\left(x \right)} + a \frac{d^{2}}{d x^{2}} f{\left(x \right)} + b^{2} \frac{d}{d x} f{\left(x \right)}$
```
:::

::: {.output .execute_result execution_count="11"}
```{=latex}
$\displaystyle a^{3} f{\left(x \right)} + a \frac{d^{2}}{d x^{2}} f{\left(x \right)} + \left(a^{2} + b^{2}\right) \frac{d}{d x} f{\left(x \right)}$
```
:::

The `rcollect()`{.py} function (not available as a method) recursively applies `collect()`{.py}.
For instance,

``` python
e6 = (a * x**2 + b*x*y + a*b*x)/(a*x**2 + b*x**2); e6
sp.rcollect(e6, x)  # Collects in numerator and denominator
```

::: {.output .execute_result execution_count="12"}
```{=latex}
$\displaystyle \frac{a b x + a x^{2} + b x y}{a x^{2} + b x^{2}}$
```
:::

::: {.output .execute_result execution_count="12"}
```{=latex}
$\displaystyle \frac{a x^{2} + x \left(a b + b y\right)}{x^{2} \left(a + b\right)}$
```
:::

Before collection, an expression may need to be expanded via `expand()`{.py}.

### The `cancel()` Function and Method

The `cancel()`{.py} function and method will return an expression in the form $p/q$, where $p$ and $q$ are polynomials that have been expanded and have integer leading coefficients.
This is typically used to cancel terms that can be factored from the numerator and denominator of a rational expression, as in the following example:

``` python
e7 = (x**3 - a**3)/(x**2 - a**2); e7
e7.cancel()
```

::: {.output .execute_result execution_count="13"}
```{=latex}
$\displaystyle \frac{- a^{3} + x^{3}}{- a^{2} + x^{2}}$
```
:::

::: {.output .execute_result execution_count="13"}
```{=latex}
$\displaystyle \frac{a^{2} + a x + x^{2}}{a + x}$
```
:::

Note that there is an implicit assumption here that $x \ne a$.
However, the cancelation is still valid for the limit as $x\rightarrow a$.

### The `apart()` and `together()` Functions and Methods

The `apart()`{.py} function and method returns a [partial fraction expansion]{.keyword} of a rational expression.
A partial fraction expansion rewrites a ratio as a sum of a polynomial and one or more ratios with irreducible denominators.
It is of particular use for computing the inverse Laplace transform.
The `together()`{.py} function is the complement of `apart()`{.py}.
Here is an example of a partial fraction expansion:

``` python
s = sp.symbols("s")
e8 = (s**3 + 6*s**2 + 16*s + 16)/(s**3 + 4*s**2 + 10*s + 7); e8
e8.apart()  # Partial fraction expansion
e8.apart().together().cancel()  # Putting it back together
```

::: {.output .execute_result execution_count="14"}
```{=latex}
$\displaystyle \frac{s^{3} + 6 s^{2} + 16 s + 16}{s^{3} + 4 s^{2} + 10 s + 7}$
```
:::

::: {.output .execute_result execution_count="14"}
```{=latex}
$\displaystyle \frac{s + 2}{s^{2} + 3 s + 7} + 1 + \frac{1}{s + 1}$
```
:::

::: {.output .execute_result execution_count="14"}
```{=latex}
$\displaystyle \frac{s^{3} + 6 s^{2} + 16 s + 16}{s^{3} + 4 s^{2} + 10 s + 7}$
```
:::

## Trigonometric Expression Manipulation {#trigonometric-expressions h="bc"}

As we saw in [nv]{.hashref}, expressions including trigonometric terms can be manipulated with the SymPy functions and methods that are nominally for polynomial and rational expressions. 
In addition to these, considered here are two important SymPy functions and methods for manipulating expressions including trigonometric terms, with a focus on the trigonometric terms themselves.

### The `trigsimp()` Function and Method

The `trigsimp()`{.py} function and method attempts to simplify a symbolic expression via trigonometric identities.
For instance, it will apply the double-angle formulas, as follows:

``` python
x = sp.symbols("x", real=True)
e9 = 2 * sp.sin(x) * sp.cos(x); e9
e9.trigsimp()
```

::: {.output .execute_result execution_count="15"}
```{=latex}
$\displaystyle 2 \sin{\left(x \right)} \cos{\left(x \right)}$
```
:::

::: {.output .execute_result execution_count="15"}
```{=latex}
$\displaystyle \sin{\left(2 x \right)}$
```
:::

\noindent
Here is a more involved expression:

``` python
e10 = sp.cos(x)**4 - 2*sp.sin(x)**2*sp.cos(x)**2 + sp.sin(x)**4; e10
e10.trigsimp()
```

::: {.output .execute_result execution_count="16"}
```{=latex}
$\displaystyle \sin^{4}{\left(x \right)} - 2 \sin^{2}{\left(x \right)} \cos^{2}{\left(x \right)} + \cos^{4}{\left(x \right)}$
```
:::

::: {.output .execute_result execution_count="16"}
```{=latex}
$\displaystyle \frac{\cos{\left(4 x \right)}}{2} + \frac{1}{2}$
```
:::

The hyperbolic trignometric functions are also handled by `trigsimp()`{.py}, as in the following example:

``` python
e11 = sp.cosh(x) * sp.tanh(x); e11
e11.trigsimp()
```

::: {.output .execute_result execution_count="17"}
```{=latex}
$\displaystyle \cosh{\left(x \right)} \tanh{\left(x \right)}$
```
:::

::: {.output .execute_result execution_count="17"}
```{=latex}
$\displaystyle \sinh{\left(x \right)}$
```
:::

### The `expand_trig()` Function

The `sp.expand_trig()`{.py} function applies the double-angle or sum identity in the expansive direction, opposite the direction of `trig_simp()`{.py}; that is,

``` python
e12 = sp.cos(x + y); e12
sp.expand_trig(e12)
```

::: {.output .execute_result execution_count="18"}
```{=latex}
$\displaystyle \cos{\left(x + y \right)}$
```
:::

::: {.output .execute_result execution_count="18"}
```{=latex}
$\displaystyle - \sin{\left(x \right)} \sin{\left(y \right)} + \cos{\left(x \right)} \cos{\left(y \right)}$
```
:::

## Power Expression Manipulation {#power-expression-manipulation h="2z"}

There are three important power identities:
\begin{align}
x^a x^b &= x^{a + b} \text{ for $x \ne 0, a, b \in \mathbb{C}$} \label{eq:pow1} \\
u^c v^c &= (u v)^c \text{ for $u, v \ge 0$ and $c \in \mathbb{R}$} \label{eq:pow2} \\
(z^d)^n &= z^{d n} \text{ for $z, d \in \mathbb{C}$ and $n \in \mathbb{Z}$.} \label{eq:pow3}
\end{align}
[@Eq:pow1;@Eq:pow2;@Eq:pow3] are applied in several power expression simplification functions and methods considered here.

### The `powsimp()` Function and Method

The `powsimp()`{.py} function and method applies the identities of [@eq:pow1;@eq:pow2] from left-to-right (replacing the left pattern with the right).
It will only apply the identity if it holds.
Consider the following, applying [@eq:pow1]:

``` python
x = sp.symbols("x", complex=True, nonzero=True)
a, b = sp.symbols("a, b", complex=True)
e13 = x**a * x**b; e13
e13.powsimp()
```

::: {.output .execute_result execution_count="19"}
```{=latex}
$\displaystyle x^{a} x^{b}$
```
:::

::: {.output .execute_result execution_count="19"}
```{=latex}
$\displaystyle x^{a + b}$
```
:::

Applying [@eq:pow2],

``` python
u, v = sp.symbols("u, v", nonnegative=True)
c = sp.symbols("c", real=True)
e14 = u**c * v**c; e14
e14.powsimp()
```

::: {.output .execute_result execution_count="20"}
```{=latex}
$\displaystyle u^{c} v^{c}$
```
:::

::: {.output .execute_result execution_count="20"}
```{=latex}
$\displaystyle \left(u v\right)^{c}$
```
:::

\noindent
Under certain conditions (i.e., $c \in \mathbb{Q}$, a literal rational exponent), [@eq:pow2] is applied right-to-left automatically, so `powsimp()`{.py} appears to have no effect.
For instance,

``` python
e15 = u**3 * v**3; e15
e15.powsimp()
```

::: {.output .execute_result execution_count="21"}
```{=latex}
$\displaystyle u^{3} v^{3}$
```
:::

::: {.output .execute_result execution_count="21"}
```{=latex}
$\displaystyle u^{3} v^{3}$
```
:::

For expressions for which the conditions for an identity does not hold, it can still be applied (at your own risk) via the `force=True`{.py} argument.

### The `expand_power_exp()` and `expand_power_base()` Functions

The `expand_power_exp()`{.py} function applies [@eq:pow1] from right-to-left (opposite of `powsimp()`{.py}), as follows:

``` python
e16 = x**(a + b); e16
sp.expand_power_exp(e16)
```

::: {.output .execute_result execution_count="22"}
```{=latex}
$\displaystyle x^{a + b}$
```
:::

::: {.output .execute_result execution_count="22"}
```{=latex}
$\displaystyle x^{a} x^{b}$
```
:::

Similarly, `expand_power_base()`{.py} applies [@eq:pow2] from right-to-left (opposite of `powsimp()`{.py}, as follows:

``` python
e17 = (u * v)**c; e17
sp.expand_power_base(e17)
```

::: {.output .execute_result execution_count="23"}
```{=latex}
$\displaystyle \left(u v\right)^{c}$
```
:::

::: {.output .execute_result execution_count="23"}
```{=latex}
$\displaystyle u^{c} v^{c}$
```
:::

Again, the identity will not be applied if its conditions do not hold for the expression; however, with the parameter `force=True`{.py}, it will be applied in any case.

### The `powdenest()` Function

The `powdenest()`{.py} function applies [@eq:pow3] from left-to-right.
For instance,

``` python
z, d = sp.symbols("z, d", complex=True)
n = sp.symbols("n", integer=True)
e18 = (z**d)**n; e18
sp.powdenest(e18)
```

::: {.output .execute_result execution_count="24"}
```{=latex}
$\displaystyle z^{d n}$
```
:::

::: {.output .execute_result execution_count="24"}
```{=latex}
$\displaystyle z^{d n}$
```
:::

\noindent
However, as we see from `e18`{.py}, the denesting is automatically applied.
There may be situations in which `powdenest()`{.py} must still be applied manually.

## Exponential and Logarithmic Expression Manipulation {#exponential-logarithmic-expression-manipulation h="2q"}

For $x, y \ge 0$ and $n \in \mathbb{R}$, the following identities hold:
\begin{align}
\log(x y) &= \log(x) + \log(y) \label{eq:log1} \\
\log(x^n) &= n \log(x) \label{eq:log2}
\end{align}
These can be applied with the `expand_log()`{.py} and `logcombine()`{.py} functions.

### The `expand_log()` Function

The `expand_log()`{.py} function applies [@eq:log1;@eq:log2] from left-to-right.
In the following example, it applies [@eq:log1]:

``` python
x, y = sp.symbols("x, y", positive=True)
n = sp.symbols("n", real=True)
e19 = sp.log(x * y); e19
sp.expand_log(e19)
```

::: {.output .execute_result execution_count="25"}
```{=latex}
$\displaystyle \log{\left(x y \right)}$
```
:::

::: {.output .execute_result execution_count="25"}
```{=latex}
$\displaystyle \log{\left(x \right)} + \log{\left(y \right)}$
```
:::

In the following example, it applies [@eq:log1]:

``` python
e20 = sp.log(x**n); e20
sp.expand_log(e20)
```

::: {.output .execute_result execution_count="26"}
```{=latex}
$\displaystyle \log{\left(x^{n} \right)}$
```
:::

::: {.output .execute_result execution_count="26"}
```{=latex}
$\displaystyle n \log{\left(x \right)}$
```
:::

### The `logcombine()` Function

The `logcombine()`{.py} function applies [@eq:log1;@eq:log2] from right-to-left.
In the following example, it applies [@eq:log1]:

``` python
e21 = sp.log(x) + sp.log(y); e21
sp.logcombine(e21)
```

::: {.output .execute_result execution_count="27"}
```{=latex}
$\displaystyle \log{\left(x \right)} + \log{\left(y \right)}$
```
:::

::: {.output .execute_result execution_count="27"}
```{=latex}
$\displaystyle \log{\left(x y \right)}$
```
:::

In the following example, it applies [@eq:log1]:

``` python
e22 = n * sp.log(x); e22
sp.logcombine(e22)
```

::: {.output .execute_result execution_count="28"}
```{=latex}
$\displaystyle n \log{\left(x \right)}$
```
:::

::: {.output .execute_result execution_count="28"}
```{=latex}
$\displaystyle \log{\left(x^{n} \right)}$
```
:::

## Rewriting Expressions in Terms of Other Functions {#rewriting-with-other-functions h="3e"}

At times, there are identities that can translate an expression in terms of one function (or set of functions) into an expression in terms of another function (or set of functions).
In SymPy, the `rewrite()`{.py} method can perform this translation.
For instance, Euler's formula, $e^{j x} = \cos x + j \sin x$ can be applied:

``` python
x = sp.symbols("x", complex=True)
e23 = sp.exp(1j * x); e23
e24 = e23.rewrite(sp.cos); e24  # Apply left-to-right
e24.rewrite(sp.exp)  # Apply right-to-left
```

::: {.output .execute_result execution_count="29"}
```{=latex}
$\displaystyle e^{1.0 i x}$
```
:::

::: {.output .execute_result execution_count="29"}
```{=latex}
$\displaystyle i \sin{\left(1.0 x \right)} + \cos{\left(1.0 x \right)}$
```
:::

::: {.output .execute_result execution_count="29"}
```{=latex}
$\displaystyle e^{1.0 i x}$
```
:::

Here is an example with a hyperbolic trigonometric function:

``` python
e25 = sp.tanh(x); e25
e25.rewrite(sp.exp)
```

::: {.output .execute_result execution_count="30"}
```{=latex}
$\displaystyle \tanh{\left(x \right)}$
```
:::

::: {.output .execute_result execution_count="30"}
```{=latex}
$\displaystyle \frac{e^{x} - e^{- x}}{e^{x} + e^{- x}}$
```
:::

Finally, consider the following example with trigonometric functions:

``` python
x, y = sp.symbols("x, y", real=True)
e26 = sp.tan(x + y)**2; e26
e26.rewrite(sp.cos)
```

::: {.output .execute_result execution_count="31"}
```{=latex}
$\displaystyle \tan^{2}{\left(x + y \right)}$
```
:::

::: {.output .execute_result execution_count="31"}
```{=latex}
$\displaystyle \frac{\cos^{2}{\left(x + y - \frac{\pi}{2} \right)}}{\cos^{2}{\left(x + y \right)}}$
```
:::

## Substituting and Replacing Expressions {#substituting-replacing-expressions h="kn"}

One expression can be substituted for another via a few different methods, the two most useful of which are considered here.

### The `subs()` Method

The `subs()`{.py} method returns a copy of an expression with specific subexpressions replaced.
There are three ways to specify substitutions for an expression `expr`{.py}:

- `expr.subs(old, new)`{.py}, in which `old`{.py} is replaced with `new`{.py}
- `expr.subs(iterable)`{.py}, in which `iterable`{.py} (e.g., a `list`{.py}) contains `old`{.py}/`new`{.py} pairs like `[(old0, new0), (old1, new1), ...]`{.py}
- `expr.subs(dictionary)`{.py}, in which `dictionary`{.py} contains `old`{.py}/`new`{.py} pairs like `{old0: new0, old1: new1, ...}`{.py}

Consider the following simple examples:

``` python
x, y, z = sp.symbols("x, y, z")
sp.sqrt(x + y).subs(x, 5)
(x + y**2 + z).subs({x: z, y: 2*z})
```

::: {.output .execute_result execution_count="32"}
```{=latex}
$\displaystyle \sqrt{y + 5}$
```
:::

::: {.output .execute_result execution_count="32"}
```{=latex}
$\displaystyle 4 z^{2} + 2 z$
```
:::

By default, when an ordered iterable like a `list`{.py} or `tuple`{.py} is provided, substitutions are performed in the order given, as in the following example:

``` python
(x + y).subs(((x, y), (y, z)))
```

::: {.output .execute_result execution_count="33"}
```{=latex}
$\displaystyle 2 z$
```
:::

\noindent
We see that the second substitution $y \rightarrow z$ is applied after the first, $x \rightarrow y$.
The parameter `simultaneous`{.py}, by default `False`{.py}, can be passed as `True`{.py} so that new subexpressions are ignored by later substitutions, as in the following example:

``` python
(x + y).subs(((x, y), (y, z)), simultaneous=True)
```

::: {.output .execute_result execution_count="34"}
```{=latex}
$\displaystyle y + z$
```
:::

For dictionary substitutions, which are unordered, a canonical ordering based on the number of operations is used for reproducibility.
We do not recommend relying on this canonical ordering, so if the order of substitutions is important, we recommend using an ordered iterable.

If the substitutions result in a numerical value, it will by default remain a symbolic expression:

``` python
sp.srepr((x + y).subs(((x, 1), (y, 3))))
```

::: {.output .execute_result execution_count="35"}
    'Integer(4)'
:::

To get a numeric type from the result, the `evalf()`{.py} method can be used:

``` python
(1/y).subs(y, 3.0).evalf(n=20)  # subs() first (20 decimal places)
(1/y).evalf(subs={y: 3.0}, n=20)  # evalfr() subs (20 decimal places)
```

::: {.output .execute_result execution_count="36"}
```{=latex}
$\displaystyle 0.33333333333333331483$
```
:::

::: {.output .execute_result execution_count="36"}
```{=latex}
$\displaystyle 0.33333333333333333333$
```
:::

Note that passing the substitutions to through `evalf()`{.py} can result in a more accurate representation, so this technique is preferred.
We will later [TODO: ref] return to more powerful techniques for numerical evaluation that convert SymPy expressions to numerically evaluable functions.

### The `replace()` Method

The `replace()`{.py} method is similar to `subs()`{.py}, but it has matching capabilities.
Common usage of the `replace()`{.py} method uses [wildcard variables]{.keyword} of class `sp.core.symbol.Wild`{.py} that match anything in a pattern.
For instance,

``` python
w = sp.symbols("w", cls=sp.Wild)
expr = sp.sin(x) + sp.sin(3*x)**2; expr
expr.replace(sp.sin(w), sp.cos(w)/w)
```

::: {.output .execute_result execution_count="37"}
```{=latex}
$\displaystyle \sin{\left(x \right)} + \sin^{2}{\left(3 x \right)}$
```
:::

::: {.output .execute_result execution_count="37"}
```{=latex}
$\displaystyle \frac{\cos{\left(x \right)}}{x} + \frac{\cos^{2}{\left(3 x \right)}}{9 x^{2}}$
```
:::

Note that the wildcard variable `w`{.py} was able to match both `x`{.py} and `3*x`{.py}, and that the the wildcard could be used in the new expression as well.
In this example, and in general, these replacement rules are applied without head to their validity, so they must be used with caution.
For more advanced usage, see the documentation on wildcard matching, [sympycore]{.plaincite post="§ 6 Symbol (\mpy{sympy.core.symbol}, \mpy{Wild} class)"} and the documentation for replacement, [sympycore]{.plaincite post="§ Basic (\mpy{sympy.core.basic.Basic}, \mpy{replace()} method)"}.
