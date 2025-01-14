# %% tags=["remove_input"]
# %matplotlib inline
import engcom
import numpy as np
import sympy as sp


# %% [markdown]
# In SymPy, a [symbolic expression]{.keyword} is comprised of SymPy objects.
# Unlike numerical expressions, these are not automatically evaluated to integer
# or floating-point numbers. For instance, using the standard library `math`{.py}
# module, the expression `math.sqrt(3)/2`{.py} immediately evaulates to the
# floating-point approximation of about `0.866`{.py}.
# However, in SymPy, something else happens:[^fn:pretty]
# %%
sp.sqrt(3) / 2

# %% [markdown]
#
# \noindent
# This is an _exact_ representation of the mathematical expression, as opposed to
# the approximation obtained previously.
#
# [^fn:pretty]: We are pretty printing results that are mathematical expressions.
#
# A symbolic expression can be represented as an [expression tree]{.keyword}:
# %%
sp.srepr(sp.sqrt(3) / 2)  # Show expression tree representation

# %% [markdown]
# \noindent
# This can be visualized as a tree graph like that shown in [@fig:symbolic-expression-tree].
#
# ![A symbolic expression tree for `sp.sqrt(3)/2`{.py}.](figures/symbolic-expression-tree/symbolic-expression-tree){#fig:symbolic-expression-tree .figure .standalone}
#
### Symbolic Variables {#symbolic-variables h="i5"}
#
# Mathematical variables can be represented as [symbolic variables]{.keyword} that
# stand in for an unspecified number.
# In SymPy, symbolic variables can be created as follows:
# %%
x, y = sp.symbols("x, y", real=True)  # Create two real variables

# %% [markdown]
# The string passed to `sp.symbols()`{.py} can separate variables with commas and/or whitespace.
# The type of unspecified number being represented by the symbolic variables listed is assumed
# to be `complex`{.py} unless an optional argument is passed declaring otherwise.
# Here we have declared that `x`{.py} and `y`{.py} are real with the [predicate]{.keyword} `real`{.py}.
# Other common predicates include the following:
#
# - Integers: `integer`{.py}, `noninteger`{.py}, `even`{.py}, and `odd`{.py}
# - Real numbers: `real`{.py}, `positive`{.py}, `nonnegative`{.py}, `nonzero`{.py}, `nonpositive`{.py}, and `negative`{.py}
# - Complex numbers: `complex`{.py} (default) and `imaginary`{.py}
#
# The predicate of a symbolic variable determines the assumptions SymPy will make about it
# when it appears in a symbolic expression.
# For instance, consider the following symbolic expressions:
# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="all"
# %%
z = sp.symbols("z")  # Complex
p = sp.symbols("p", positive=True)
sp.sqrt(z**2)
sp.sqrt(x**2)  # Using real x from above
sp.sqrt(p**2)

# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="last_expr"

# %% [markdown]
# \noindent
# We see that the expression automatically simplifies based on the predicates provided for each variable.
# This will prove especially useful once we begin using the symbolic expression manipulation techniques described in the following sections.
#
### Symbolic Functions {#symbolic-functions h="a6"}
#
# A mathematical function can be represented in SymPy by a [symbolic function]{.keyword}.
# There are a few different ways to create these, and we will consider only the simplest and most common cases here.
# An [undefined function]{.keyword} $f$ that should be treated as monolithic and as having no special properties can be defined as follows:
# %%
f = sp.Function("f")  # Type: sp.core.function.UndefinedFunction
f(x) + 3 * f(x)  # Using x from above

# %% [markdown]
# Predicates can be applied to functions, as well; for instance,
# %%
g = sp.Function("g", real=True)
f(x) + g(x, y) * g(3, -3)

# %% [markdown]
# An [applied undefined function]{.keyword} is an undefined function that has been given an argument.
# For instance,
# %%
h = sp.Function("h")(x)  # Types: h, sp.core.function.AppliedUndef
3 * h  ## Leave off the argument


# %% [markdown]
# Undefined functions are never evaluated.
# At times we want to define a function that is always to be evaluated; in SymPy such a function is called a [fully evaluated function]{.keyword}.
# A fully evaluated function can be created as a regular Python function, as in the following case:
# %%
def F(x):
    return x**2 - 4
F(x)**2

# %% [markdown]
# For [piecewise functions]{.keyword}, regular Python functions with `if`{.py} statements will work, but it is preferable to use the `sp.Piecewise()`{.py} function.
# For instance, 
# %%
G = sp.Piecewise(
    (x**2, x <= 0),  # $x^2$ for $x \le 0$
    (3*x, True)  # $3 x$ for $x > 0$
)

# %% [markdown]
# Many common mathematical functions are built in to SymPy, including those shown in [@tbl:sympy-math-functions].
# 
# ```{=latex}
# \begin{table}[H]
# \centering
# \caption{Elementary mathematical functions in SymPy.}
# \label{tbl:sympy-math-functions}
# \begin{tabular}{ll}
# \toprule
# Kind                  & SymPy Functions (\mpy{sp.} prefix suppressed)                                                                       \\ 
# \midrule
# Complex               & \mpy{Abs()}, \mpy{arg()}, \mpy{conjugate()}, \mpy{im()}, \mpy{re()}, \mpy{sign()}                    \\ 
# Trigonmetric          & \mpy{sin()}, \mpy{cos()}, \mpy{tan()}, \mpy{sec()}, \mpy{csc()}, \mpy{cot()}                         \\ 
# Inverse Trigonometric & \mpy{asin()}, \mpy{acos()}, \mpy{atan()}, \mpy{atan2()}, \mpy{asec()}, \mpy{acsc()}, \mpy{acot()} \\ 
# Hyperbolic            & \mpy{sinh()}, \mpy{cosh()}, \mpy{tanh()}, \mpy{coth()}, \mpy{sech()}, \mpy{csch()}                   \\ 
# Inverse Hyperbolic    & \mpy{asinh()}, \mpy{acosh()}, \mpy{atanh()}, \mpy{acoth()}, \mpy{asech()}                               \\ 
# Integer               & \mpy{ceiling()}, \mpy{floor()}, \mpy{frac()} \mpy{get_integer_part()}                                    \\ 
# Exponential           & \mpy{exp()}, \mpy{log()}                                                                                         \\ 
# Miscellaneous         & \mpy{Min()}, \mpy{Max()}, \mpy{root()}, \mpy{sqrt()}                                                       \\ 
# \bottomrule
# \end{tabular}
# \end{table}
# ```
# 
# ```{=markdown}
# | Kind                  | SymPy Functions (`sp.`{.py} prefix suppressed)                                                           |
# |-----------------------|----------------------------------------------------------------------------------------------------------|
# | Complex               | `Abs()`{.py}, `arg()`{.py}, `conjugate()`{.py}, `im()`{.py}, `re()`{.py}, `sign()`{.py}                  |
# | Trigonmetric          | `sin()`{.py}, `cos()`{.py}, `tan()`{.py}, `sec()`{.py}, `csc()`{.py}, `cot()`{.py}                       |
# | Inverse Trigonometric | `asin()`{.py}, `acos()`{.py}, `atan()`{.py}, `atan2()`{.py}, `asec()`{.py}, `acsc()`{.py}, `acot()`{.py} |
# | Hyperbolic            | `sinh()`{.py}, `cosh()`{.py}, `tanh()`{.py}, `coth()`{.py}, `sech()`{.py}, `csch()`{.py}                 |
# | Inverse Hyperbolic    | `asinh()`{.py}, `acosh()`{.py}, `atanh()`{.py}, `acoth()`{.py}, `asech()`{.py}                           |
# | Integer               | `ceiling()`{.py}, `floor()`{.py}, `frac()`{.py}, `get_integer_part()`{.py}                                |
# | Exponential           | `exp()`{.py}, `log()`{.py}                                                                               |
# | Miscellaneous         | `Min()`{.py}, `Max()`{.py}, `root()`{.py}, `sqrt()`{.py}                                                 |
#
# : Elementary mathematical functions in SymPy. {#tbl:sympy-math-functions}
# 
# ```
# 
# In rare cases, we must define a [custom function]{.keyword}; that is, a subclass of the `sp.Function`{.py} class.
# Such a function needs to have its behavior thoroughly defined.
# Once it is completed, it should behave just as built-in functions like `sp.sin()`{.py}.
# For a tutorial on writing custom functions, see [sp2023a]{.plaincite}.