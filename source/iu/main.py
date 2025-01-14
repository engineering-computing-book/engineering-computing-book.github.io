# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="all"
# %matplotlib inline
import sympy as sp
import numpy as np

# %% [markdown]
# Engineering analysis regularly includes calculus.
# Derivatives with respect to time and differential equations (i.e., equations including derivatives) are the key mathematical models of rigid-body mechanics (e.g., statics and dynamics), solid mechanics (e.g., mechanics of materials), fluid mechanics, heat transfer, and electromagnetism.
# Integration is necessary for solving differential equations and computing important quantities of interest.
# Limits and series expansions are frequently used to in the analytic process to simplify equations and to estimate unkown quantities.
# In other words, calculus is central to the enterprise of engineering analysis.
#
### Derivatives {#derivatives h="zt"}
#
# In SymPy, it is possible to compute the derivative of an expression using the `diff()`{.py} function and method, as follows:
# %%
x, y = sp.symbols("x, y", real=True)
expr = x**2 + x*y + y**2
expr.diff(x)  # Or sp.diff(expr, x)
expr.diff(y)  # Or sp.diff(expr, y)

# %% [markdown]
# Higher-order derivatives can be computed by adding the corresponding integer, as in the following second derivative:
# %%
expr.diff(x, 2)  # Or sp.diff(expr, x, 2)

# %% [markdown]
# We can see that the partial derivative is applied to a multivariate expression.
# The differentiation can be mixed, as well, as in the following example:
# %%
expr = x * y**2/(x**2 + y**2)
expr.diff(x, 1, y, 2).simplify()  # $\partial^3/\partial x \partial y^2$

# %% [markdown]
# The option `evaluate=False`{.py} will leave the derivative unevaluated until the `doit()`{.py} method is called, as in the following example:
# %%
expr = sp.sin(x)
expr2 = expr.diff(x, evaluate=False); expr2
expr2.doit()

# %% [markdown]
# The derivative of an undefined function is left unevaluated, as in the following case:
# %%
f = sp.Function("f", real=True)
expr = 3*f(x) + f(x)**2
expr.diff(x)

# %% [markdown]
# \noindent
# As we can see, the chain rule of differentiation was applied automatically.
#
# Differentiation works element-wise on matrices and vectors, just as it works mathematically.
# For instance,
# %%
v = sp.Matrix([[x**2], [x*y]])
v.diff(x)

# %% [markdown]
### Integrals {#integrals h="nd"}
#
# To a symbolic integral in SymPy, use the `integrate()`{.py} function or method.
# For an indefinite integral, pass only the variable over which to integrate, as in
# %%
x, y = sp.symbols("x, y", real=True)
expr = x + y
expr.integrate(x)  # Or sp.integrate(expr, x); $\int x + y\ dx$

# %% [markdown]
# \noindent
# Note that no constant of integration is added, so you may need to add your own.
#
# The definite integral can be computed by providing a triple, as in the following example,
# %%
sp.integrate(expr, (x, 0, 3))  # $\int_0^3 x + y\ dx$
sp.integrate(expr, (x, 1, y))  # $\int_1^y x + y\ dx$

# %% [markdown]
# Multiple integrals can be computed in a similar fashion, as in the following examples:
# %%
sp.integrate(expr, (x, 0, 4), (y, 2, 3))  # $\int_2^3 \int_0^4 x + y\ dx dy$

# %% [markdown]
# To create an unevaluated integral object, use the `sp.Integral()`{.py} constructor.
# To evaluate an unevaluated integral, use the `doit()`{.py} method, as follows:
# %%
expr2 = sp.Integral(expr, x); expr2  # Unevaluated
expr2.doit()  # Evaluate

# %% [markdown]
# Integration works over piecewise functions, as in the following example:
# %%
f = sp.Piecewise((0, x < 0), (1, x >= 0)); f
sp.integrate(f, (x, -5, 5))

# %% [markdown]
# The `integrate()`{.py} function and method is very powerful, but it may not be able to integrate some functions.
# In such cases, it returns an unevaluated integral.
#
### Limits {#limits h="1a"}
#
# In SymPy, a limit can be computed via the `limit()`{.py} function and method.
# The $\lim_{x\rightarrow 0}$ can be computed as follows:
# %%
sp.limit(sp.tanh(x)/x, x, 0)  # $\lim_{x\rightarrow 0} \tanh(x)/x$

# %% [markdown]
# The limit to infinity or negative infinity can be denoted using the `sp.oo`{.py} symbol, as follows:
# %%
sp.limit(2  - x * sp.exp(-x), x, sp.oo)  # $\lim_{x\rightarrow \infty} (1 - x e^{-x})$

# %% [markdown]
# The limit can be left unevaluated using the `sp.Limit()`{.py} constructor, as follows:
# %%
lim = sp.Limit(2  - x * sp.exp(-x), x, sp.oo); expr  # Unevaluated
lim.doit()  # Evaluate

# %% [markdown]
# The limit can be taken from a direction using the optional fourth argument, as follows:
# %%
expr = 1/x
lim_neg = sp.Limit(expr, x, 0, "-"); lim_neg
lim_pos = sp.Limit(expr, x, 0, "+"); lim_pos
lim_neg.doit()
lim_pos.doit()

# %% [markdown]
### Taylor Series {#taylor-series h="wm"}
#
# A Taylor series (i.e., Taylor expansion) is an infinite power series approximation of an infinitely differentiable function near some point.
# For a function $f(x)$, the Taylor series at point $x_0$ is given by
# $$
# \sum_{n=0}^\infty \frac{f^{(n)}}{n!} (x - x_0)^n = f(x_0) + f'(x_0) (x - x_0) + \frac{f''(x_0)}{2!} (x - x_0)^2 + \cdots.
# $$
# We often represent terms with power order $m$ and greater with the [big-O notation]{.keyword} $O((x-x_0)^m)$.
# For instance, for an expansion about $x_0 = 0$,
# $$
# \sum_{n=0}^\infty \frac{f^{(n)}}{n!} (x)^n = f(0) + f'(x_0) (x - x_0) + O(x^2).
# $$
#
# In SymPy, the Taylor series can be found via the `series()`{.py} function or method.
# For instance,
# %%
f = sp.sin(x)
f.series(x0=0, n=4)  # Or sp.series(f, x0=0, n=4)

# %% [markdown]
# \noindent
# The `sp.O()`{.py} function, which appears in this result, automatically absorbs higher-order terms.
# For instance,
# %%
x**2 + x**4 + x** 5 + sp.O(x**4)

# %% [markdown]
# To remove the `sp.O()`{.py} function from an expression, call the `removeO()`{.py} method, as follows:
# %%
f.series(x0=0, n=4).removeO()

# %% [markdown]
# \noindent
# Removing the higher-order terms is frequently useful when we would like to use the $n$th-order [Taylor polynomial]{.keyword}, a truncated Taylor series, as an approximation of a function.

# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="last_expr"