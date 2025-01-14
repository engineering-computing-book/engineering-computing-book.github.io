# %% tags=["remove_input"]
# %matplotlib inline
import engcom
import numpy as np
import sympy as sp


# %% [markdown]
# In engineering symbolic analysis, the need to manipulate, often algebraically, mathematical expressions arises constantly.
# SymPy has several powerful tools for manipulating symbolic expressions, the most useful of which we will consider here.
#
### The `simplify()` Function and Method {#simplify-function-method h="9r"}
#
# A built-in Sympy function and method, `sp.simplify()`{.py}, is a common SymPy tool for manipulation because simplification is often what we want.
# Recall that some basic simplification occurs automatically; however, in many cases this automatic simplification is insufficient.
# Applying `sp.simplify()`{.py} typically results in an expression as simple as or simpler than its input; however, the precise meaning of "simpler" is quite vague, which can lead to frustrating cases in which a version of an expression we consider to be simpler is not chosen by the `sp.simplify()`{.py} algorithm.
# In such cases, we will often use the more manual techniques considered later in this section.
# 
# The predicates (i.e., assumptions) used to define the symbolic variables and functions that appear in a symbolic expression are respected by `sp.simplify()`{.py}.
# Consider the following example:
# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="all"
# %%
x = sp.symbols("x", real=True)
e0 = (x**2 + 2*x + 3*x)/(x**2 + 2*x); e0  # For display
e0.simplify()  # Returns simplified expression, leaves e0 unchanged

# %% [markdown]
# \noindent
# Note that `e0`{.py} was slightly simplified automatically.
# The `simplify()`{.py} method further simplified by canceling an `x`{.py}. 
# The use of the method does not affect the object, so it the same as the use of the function.
# 
# There are a few "knobs" to turn in the form of optional arguments to `sp.simplify()`{.py}:
#
# - `measure`{.py} (default: `sp.count_ops()`{.py}): A function that serves as a heuristic complexity metric. The default `sp.count_ops()`{.py} counts the operations in the expression.
# - `ratio`{.py} (default: `1.7`{.py}): The maximum ratio of the measures, output `out`{.py} over input `inp`{.py}, `measure(out)/measure(inp)`{.py}. Anything over `1`{.py} allows the output to be potentially more complex than the input, but it may still be simpler because the metric is just a heuristic.
# - `rational`{.py} (default: `False`{.py}): By default (`False`{.py}), floating-point numbers are left alone. If `rational=True`{.py}, floating-point numbers are recast as rational numbers. If `rational=None`{.py}, floating-point numbers are recast as rational numbers during simplification, but recast to floating-point numbers in the result.
# - `inverse`{.py} (default: `False`{.py}): If `True`{.py}, allows inverse functions to be cancelled in any order without knowing if the inner argument falls in the domain for which the inverse holds.[^fn:inverse-principal-branch] For instance, this allows $\arccos(\cos x) \rightarrow x$ without knowing if $x \in [0, \pi]$.
# - `force`{.py} (default: `False`{.py}): If `True`{.py}, predicates (assumptions) of the variables will be ignored.
# 
# [^fn:inverse-principal-branch]: The usual way of defining the inverse $y = \arccos x$ is to retrict $y$ in $x = \cos y$ to $[0, \pi]$. This is because $\cos$ is not one-to-one (e.g., $\cos 0 = \cos 2\pi = 1$), so its domain must be restricted for a proper inverse to exist. The conventional choice of domain restriction to $[0, \pi]$ is called the selection of a principal branch.
# 
### Polynomial and Rational Expression Manipulation {#polynomial-rational-expressions h="nv"}
# 
# Here we consider a few SymPy functions and methods that manipulate polynomials and rational expressions.
#
#### The `expand()` Function and Method
# 
# The `expand()`{.py} function and method expresses a polynomial in the canonical form of a sum of monomials.
# A monomial is a polynomial with exactly one additive term.
# For instance,
# %%
sp.expand((x + 3)**2)  ## Using the real x from above

# %% [markdown]
# We can also expand a numerator or denominator without expanding the entire expression, as follows for $(x+3)^2/(x - 2)^2$:
# %%
frac = (x + 3)**2/(x - 2)**2
frac.expand()
frac.expand(numer=True)
frac.expand(denom=True)
frac.expand(numer=True).expand(denom=True)

# %% [markdown]
# There are several additional options for `expand()`{.py}, including:
# 
# - `mul`{.py} (default: `True`{.py}): If `True`{.py}, distributes multiplication over addition (e.g., $5 (x + 1) \rightarrow 5 x + 5$.
# - `multinomial`{.py} (default: `True`{.py}): If `True`{.py}, expands multinomial (polynomial that is not a monomial) terms into sums of monomials (e.g., $(x + y)^2 \rightarrow x^2 + 2 x y + y^2$).
# - `power_exp`{.py} (default: `True`{.py}): If `True`{.py}, expands sums in exponents to products of exponentials (e.g., $e^{3 + x} \rightarrow e^3 e^x$).
# - `log`{.py} (default: `True`{.py}): If `True`{.py}, split log products into sums and extract log exponents to multiplicative constants (e.g., for $x, y > 0$, $\ln(x^3 y) \rightarrow 3\ln x + \ln y$).
# - `deep`{.py} (default: `True`{.py}): If `True`{.py}, expands all levels of the expression tree; if `False`{.py}, expands only the top level (e.g., $x (x + (y+1)^2) \rightarrow x^2 + x (y+1)^2$).
# - `complex` (default: `False`{.py}): If `True`{.py}, collect real and imaginary parts (e.g., $x + y \rightarrow \Re(x) + \Re(y) + j (\Im(x) + \Im(y))$).
# - `func`{.py} (default: `False`{.py}): If `True`{.py}, expand nonpolynomial functions (e.g., for the gamma function $\Gamma$, $\Gamma(x+2) \rightarrow x^2 \Gamma(x) + x \Gamma(x)$).
# - `trig`{.py} (default: `False`{.py}): If `True`{.py}, expand trigonometric functions (e.g., $\sin(x+y) \rightarrow \sin x \cos y -  \sin y \cos x$).
#
#### The `factor()` Function and Method
#
# The `factor()`{.py} function and method returns a factorization into irreducibles factors.
# For polynomials, this is the reverse of `expand()`{.py}.
# Irreducibility of the factors is guaranteed for polynomials.
# Consider the following polynomial example:
# %%
x, y = sp.symbols("x, y", real=True)
e0 = (x + 1)**2 * (x**2 + 2*x*y + y**2); e0
e0.expand()
e0.expand().factor()

# %% [markdown]
# Factorization can also be performed over nonpolynomial expressions, as in the following example:
# %%
e1 = sp.sin(x) * (sp.cos(x) + sp.sin(x))**2; e1  # Using above real x
e1.expand()
e1.expand().factor()

# %% [markdown]
# There are two options of note:
#
# - `deep`{.py} (default: `False`{.py}): If `True`{.py}, inner expression tree elements will also be factored (e.g., $\exp(x^2 + 4 x + 4) \rightarrow \exp((x+2)^2)$).
# - `fraction`{.py} (default: `True`{.py}): If `True`{.py}, rational expressions will be combined.
#
# \noindent
# An example of the latter option is given here:
# %% 
e2 = x - 5*sp.exp(3 - x); e2  # Using real x from above
e2.factor(deep=True)
e2.factor(deep=True, fraction=False)

# %% [markdown]
#### The `collect()` Function and Method
#
# The `collect()`{.py} function and method returns an expression with specific terms collected.
# For instance,
# %%
x, y, a, b = sp.symbols("x, y, a, b", real=True)
e3 = a * x + b * x * y + a**2 * x**2 + 3 * y**2 + x * y + 8; e3
e3.collect(x)

# %% [markdown]
# More complicated expressions can be collected as well, as in the following example:
# %% 
e4 = a*sp.cos(4*x) + b*sp.cos(4*x) + b*sp.cos(6*x) + a * sp.sin(x); e4
e4.collect(sp.cos(4*x))

# %% [markdown]
# Derivatives of an undefined symbolic function, as would appear in a differential equation, can be collected. If the function is passed to `collect()`{.py}, as in the following example, it and its derivatives are collected:
# %% 
f = sp.Function("f")(x)  ## Applied undefined function
e5 = a*f.diff(x, 2) + a**2*f.diff(x) + b**2*f.diff(x) + a**3*f; e5
e5.collect(f)

# %% [markdown]
# The `rcollect()`{.py} function (not available as a method) recursively applies `collect()`{.py}.
# For instance,
# %%
e6 = (a * x**2 + b*x*y + a*b*x)/(a*x**2 + b*x**2); e6
sp.rcollect(e6, x)  # Collects in numerator and denominator

# %% [markdown]
# Before collection, an expression may need to be expanded via `expand()`{.py}.
#
#### The `cancel()` Function and Method
#
# The `cancel()`{.py} function and method will return an expression in the form $p/q$, where $p$ and $q$ are polynomials that have been expanded and have integer leading coefficients.
# This is typically used to cancel terms that can be factored from the numerator and denominator of a rational expression, as in the following example:
# %%
e7 = (x**3 - a**3)/(x**2 - a**2); e7
e7.cancel()

# %% [markdown]
# Note that there is an implicit assumption here that $x \ne a$.
# However, the cancelation is still valid for the limit as $x\rightarrow a$.
#
#### The `apart()` and `together()` Functions and Methods
#
# The `apart()`{.py} function and method returns a [partial fraction expansion]{.keyword} of a rational expression.
# A partial fraction expansion rewrites a ratio as a sum of a polynomial and one or more ratios with irreducible denominators.
# It is of particular use for computing the inverse Laplace transform.
# The `together()`{.py} function is the complement of `apart()`{.py}.
# Here is an example of a partial fraction expansion:
# %%
s = sp.symbols("s")
e8 = (s**3 + 6*s**2 + 16*s + 16)/(s**3 + 4*s**2 + 10*s + 7); e8
e8.apart()  # Partial fraction expansion
e8.apart().together().cancel()  # Putting it back together

# %% [markdown]
### Trigonometric Expression Manipulation {#trigonometric-expressions h="bc"}
# 
# As we saw in [nv]{.hashref}, expressions including trigonometric terms can be manipulated with the SymPy functions and methods that are nominally for polynomial and rational expressions. 
# In addition to these, considered here are two important SymPy functions and methods for manipulating expressions including trigonometric terms, with a focus on the trigonometric terms themselves.
#
#### The `trigsimp()` Function and Method
#
# The `trigsimp()`{.py} function and method attempts to simplify a symbolic expression via trigonometric identities.
# For instance, it will apply the double-angle formulas, as follows:
# %%
x = sp.symbols("x", real=True)
e9 = 2 * sp.sin(x) * sp.cos(x); e9
e9.trigsimp()

# %% [markdown]
# \noindent
# Here is a more involved expression:
# %%
e10 = sp.cos(x)**4 - 2*sp.sin(x)**2*sp.cos(x)**2 + sp.sin(x)**4; e10
e10.trigsimp()

# %% [markdown]
# The hyperbolic trignometric functions are also handled by `trigsimp()`{.py}, as in the following example:
# %%
e11 = sp.cosh(x) * sp.tanh(x); e11
e11.trigsimp()

# %% [markdown]
#### The `expand_trig()` Function
# 
# The `sp.expand_trig()`{.py} function applies the double-angle or sum identity in the expansive direction, opposite the direction of `trig_simp()`{.py}; that is,
# %%
e12 = sp.cos(x + y); e12
sp.expand_trig(e12)

# %% [markdown]
### Power Expression Manipulation {#power-expression-manipulation h="2z"}
#
# There are three important power identities:
# \begin{align}
# x^a x^b &= x^{a + b} \text{ for $x \ne 0, a, b \in \mathbb{C}$} \label{eq:pow1} \\
# u^c v^c &= (u v)^c \text{ for $u, v \ge 0$ and $c \in \mathbb{R}$} \label{eq:pow2} \\
# (z^d)^n &= z^{d n} \text{ for $z, d \in \mathbb{C}$ and $n \in \mathbb{Z}$.} \label{eq:pow3}
# \end{align}
# [@Eq:pow1;@Eq:pow2;@Eq:pow3] are applied in several power expression simplification functions and methods considered here.
#
#### The `powsimp()` Function and Method
#
# The `powsimp()`{.py} function and method applies the identities of [@eq:pow1;@eq:pow2] from left-to-right (replacing the left pattern with the right).
# It will only apply the identity if it holds.
# Consider the following, applying [@eq:pow1]:
# %%
x = sp.symbols("x", complex=True, nonzero=True)
a, b = sp.symbols("a, b", complex=True)
e13 = x**a * x**b; e13
e13.powsimp()

# %% [markdown]
# Applying [@eq:pow2],
# %%
u, v = sp.symbols("u, v", nonnegative=True)
c = sp.symbols("c", real=True)
e14 = u**c * v**c; e14
e14.powsimp()

# %% [markdown]
# \noindent
# Under certain conditions (i.e., $c \in \mathbb{Q}$, a literal rational exponent), [@eq:pow2] is applied right-to-left automatically, so `powsimp()`{.py} appears to have no effect.
# For instance,
# %%
e15 = u**3 * v**3; e15
e15.powsimp()

# %% [markdown]
# For expressions for which the conditions for an identity does not hold, it can still be applied (at your own risk) via the `force=True`{.py} argument.
#
#### The `expand_power_exp()` and `expand_power_base()` Functions
#
# The `expand_power_exp()`{.py} function applies [@eq:pow1] from right-to-left (opposite of `powsimp()`{.py}), as follows:
# %%
e16 = x**(a + b); e16
sp.expand_power_exp(e16)

# %% [markdown]
# Similarly, `expand_power_base()`{.py} applies [@eq:pow2] from right-to-left (opposite of `powsimp()`{.py}, as follows:
# %%
e17 = (u * v)**c; e17
sp.expand_power_base(e17)

# %% [markdown]
# Again, the identity will not be applied if its conditions do not hold for the expression; however, with the parameter `force=True`{.py}, it will be applied in any case.
#
#### The `powdenest()` Function
#
# The `powdenest()`{.py} function applies [@eq:pow3] from left-to-right.
# For instance,
# %%
z, d = sp.symbols("z, d", complex=True)
n = sp.symbols("n", integer=True)
e18 = (z**d)**n; e18
sp.powdenest(e18)

# %% [markdown]
# \noindent
# However, as we see from `e18`{.py}, the denesting is automatically applied.
# There may be situations in which `powdenest()`{.py} must still be applied manually.
#
### Exponential and Logarithmic Expression Manipulation {#exponential-logarithmic-expression-manipulation h="2q"}
#
# For $x, y \ge 0$ and $n \in \mathbb{R}$, the following identities hold:
# \begin{align}
# \log(x y) &= \log(x) + \log(y) \label{eq:log1} \\
# \log(x^n) &= n \log(x) \label{eq:log2}
# \end{align}
# These can be applied with the `expand_log()`{.py} and `logcombine()`{.py} functions.
#
#### The `expand_log()` Function
#
# The `expand_log()`{.py} function applies [@eq:log1;@eq:log2] from left-to-right.
# In the following example, it applies [@eq:log1]:
# %%
x, y = sp.symbols("x, y", positive=True)
n = sp.symbols("n", real=True)
e19 = sp.log(x * y); e19
sp.expand_log(e19)

# %% [markdown]
# In the following example, it applies [@eq:log1]:
# %%
e20 = sp.log(x**n); e20
sp.expand_log(e20)

# %% [markdown]
#### The `logcombine()` Function
#
# The `logcombine()`{.py} function applies [@eq:log1;@eq:log2] from right-to-left.
# In the following example, it applies [@eq:log1]:
# %%
e21 = sp.log(x) + sp.log(y); e21
sp.logcombine(e21)

# %% [markdown]
# In the following example, it applies [@eq:log1]:
# %%
e22 = n * sp.log(x); e22
sp.logcombine(e22)

# %% [markdown]
### Rewriting Expressions in Terms of Other Functions {#rewriting-with-other-functions h="3e"}
#
# At times, there are identities that can translate an expression in terms of one function (or set of functions) into an expression in terms of another function (or set of functions).
# In SymPy, the `rewrite()`{.py} method can perform this translation.
# For instance, Euler's formula, $e^{j x} = \cos x + j \sin x$ can be applied:
# %%
x = sp.symbols("x", complex=True)
e23 = sp.exp(1j * x); e23
e24 = e23.rewrite(sp.cos); e24  # Apply left-to-right
e24.rewrite(sp.exp)  # Apply right-to-left

# %% [markdown]
# Here is an example with a hyperbolic trigonometric function:
# %%
e25 = sp.tanh(x); e25
e25.rewrite(sp.exp)

# %% [markdown]
# Finally, consider the following example with trigonometric functions:
# %%
x, y = sp.symbols("x, y", real=True)
e26 = sp.tan(x + y)**2; e26
e26.rewrite(sp.cos)

# %% [markdown]
### Substituting and Replacing Expressions {#substituting-replacing-expressions h="kn"}
#
# One expression can be substituted for another via a few different methods, the two most useful of which are considered here.
#
#### The `subs()` Method
#
# The `subs()`{.py} method returns a copy of an expression with specific subexpressions replaced.
# There are three ways to specify substitutions for an expression `expr`{.py}:
# 
# - `expr.subs(old, new)`{.py}, in which `old`{.py} is replaced with `new`{.py}
# - `expr.subs(iterable)`{.py}, in which `iterable`{.py} (e.g., a `list`{.py}) contains `old`{.py}/`new`{.py} pairs like `[(old0, new0), (old1, new1), ...]`{.py}
# - `expr.subs(dictionary)`{.py}, in which `dictionary`{.py} contains `old`{.py}/`new`{.py} pairs like `{old0: new0, old1: new1, ...}`{.py}
#
# Consider the following simple examples:
# %%
x, y, z = sp.symbols("x, y, z")
sp.sqrt(x + y).subs(x, 5)
(x + y**2 + z).subs({x: z, y: 2*z})

# %% [markdown]
# By default, when an ordered iterable like a `list`{.py} or `tuple`{.py} is provided, substitutions are performed in the order given, as in the following example:
# %%
(x + y).subs(((x, y), (y, z)))

# %% [markdown]
# \noindent
# We see that the second substitution $y \rightarrow z$ is applied after the first, $x \rightarrow y$.
# The parameter `simultaneous`{.py}, by default `False`{.py}, can be passed as `True`{.py} so that new subexpressions are ignored by later substitutions, as in the following example:
# %%
(x + y).subs(((x, y), (y, z)), simultaneous=True)

# %% [markdown]
# For dictionary substitutions, which are unordered, a canonical ordering based on the number of operations is used for reproducibility.
# We do not recommend relying on this canonical ordering, so if the order of substitutions is important, we recommend using an ordered iterable.
# 
# If the substitutions result in a numerical value, it will by default remain a symbolic expression:
# %%
sp.srepr((x + y).subs(((x, 1), (y, 3))))

# %% [markdown]
# To get a numeric type from the result, the `evalf()`{.py} method can be used:
# %%
(1/y).subs(y, 3.0).evalf(n=20)  # subs() first (20 decimal places)
(1/y).evalf(subs={y: 3.0}, n=20)  # evalfr() subs (20 decimal places)

# %% [markdown]
# Note that passing the substitutions to through `evalf()`{.py} can result in a more accurate representation, so this technique is preferred.
# We will later [TODO: ref] return to more powerful techniques for numerical evaluation that convert SymPy expressions to numerically evaluable functions.
#
#### The `replace()` Method
#
# The `replace()`{.py} method is similar to `subs()`{.py}, but it has matching capabilities.
# Common usage of the `replace()`{.py} method uses [wildcard variables]{.keyword} of class `sp.core.symbol.Wild`{.py} that match anything in a pattern.
# For instance,
# %%
w = sp.symbols("w", cls=sp.Wild)
expr = sp.sin(x) + sp.sin(3*x)**2; expr
expr.replace(sp.sin(w), sp.cos(w)/w)

# %% [markdown]
# Note that the wildcard variable `w`{.py} was able to match both `x`{.py} and `3*x`{.py}, and that the the wildcard could be used in the new expression as well.
# In this example, and in general, these replacement rules are applied without head to their validity, so they must be used with caution.
# For more advanced usage, see the documentation on wildcard matching, [sympycore]{.plaincite post="§ 6 Symbol (\mpy{sympy.core.symbol}, \mpy{Wild} class)"} and the documentation for replacement, [sympycore]{.plaincite post="§ Basic (\mpy{sympy.core.basic.Basic}, \mpy{replace()} method)"}.

# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="last_expr"