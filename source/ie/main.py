# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="all"
# %matplotlib inline
import engcom

# %% [markdown]
# First, load SymPy as follows:
# %%
import sympy as sp

# %% [markdown]
# Unfortunately, the SymPy `trigsimp()`{.py} method doesn't combine 
# the cosine and sine terms that share an argument.
# However, we can define a functions `trig_two_to_one()`{.py} for 
# performing the two-to-one conversion.
# The identities we will use are as follows:
# \begin{align*}
# a \cos u + b \sin u &= \sqrt{a^2 + b^2} \sin(u + \arctan(a/b)) \\
# &= \sqrt{a^2 + b^2} \cos(u - \arctan(b/a)).
# \end{align*}
# We begin by defining two functions, each of which returns a 
# dictionary of replacement rules for sin(u) in the identities above.
# %%

def _trig_two_to_one_sin_rule(a, b, u):
	"""Replacement rule for sin(u) in a cos(u) + b sin(u) for 
	converting to a single sin term with a phase
	
	The identity applied is:
		a cos u + b sin u = sqrt(a^2 + b^2) sin(u + atan(a/b))
	Returns: A dictionary for replacing sin(u)
	"""
	identity = a*sp.cos(u) + b*sp.sin(u) + \
		- sp.sqrt(a**2 + b**2)*sp.sin(u + sp.atan(a/b))
	sol = sp.solve(identity, [sp.sin(u)], dict=True)
	return sol[0]

def _trig_two_to_one_cos_rule(a, b, u):
	"""Replacement rule for sin(u) in a cos(u) + b sin(u) for 
	converting to a single cos term with a phase
	
	The identity applied is:
		a cos u + b sin u = sqrt(a^2 + b^2) cos(u - atan(b/a))
	Returns: A dictionary for replacing sin(u)
	"""
	identity = a*sp.cos(u) + b*sp.sin(u) + \
		- sp.sqrt(a**2 + b**2)*sp.cos(u - sp.atan(b/a))
	sol = sp.solve(identity, [sp.sin(u)], dict=True)
	return sol[0]

# %% [markdown]
# Now we can write a function to perform the trigonometric 
# simplification, as follows:
# %%
def trig_two_to_one(expr: sp.Expr, to: str = "sin"):
	"""Rewrites sin and cos terms that share arguments to single sin 
	or cos terms
	
	Applies the following identity:
		a cos u + b sin u = sqrt(a^2 + b^2) sin(u + atan(a/b))
	or
		a cos u + b sin u = sqrt(a^2 + b^2) cos(u - atan(b/a))
	depending on the ``to`` argument.
	
	Args:
		expr: The symbolic expression containing sin(u) and cos(u)
		to: Rewrite with "sin" (default) or "cos"
	"""
	expr = expr.simplify()
	# Identify sin terms
	w1 = sp.Wild("w1", exclude=[1])
	w2 = sp.Wild("w2")
	sin_terms = expr.find(w1*sp.sin(w2))
	sin_arg_amps = {}  # To be: {sin argument: sine amplitude}
	for term in sin_terms:
		arg_amp_rules = term.match(w1*sp.sin(w2))
		sin_arg_amps[arg_amp_rules[w2]] = arg_amp_rules[w1]
	# Identify cos terms
	cos_terms = expr.find(w1*sp.cos(w2))
	cos_arg_amps = {}  # To be: {sin argument: sine amplitude}
	for term in cos_terms:
		arg_amp_rules = term.match(w1*sp.cos(w2))
		cos_arg_amps[arg_amp_rules[w2]] = arg_amp_rules[w1]
	# Replace with wildcard rule
	for sin_arg, sin_amp in sin_arg_amps.items():
		if to == "sin":
			if sin_arg in cos_arg_amps.keys():
				cos_amp = cos_arg_amps[sin_arg]
				sin_rule = _trig_two_to_one_sin_rule(
					cos_amp, sin_amp, sin_arg
				)
				expr = expr.subs(sin_rule)
		elif to == "cos":
			if sin_arg in cos_arg_amps.keys():
				cos_amp = cos_arg_amps[sin_arg]
				cos_rule = _trig_two_to_one_cos_rule(
					cos_amp, sin_amp, sin_arg
				)
				expr = expr.subs(cos_rule)
	return expr.simplify()

# %% [markdown]
# The expression of interest in the problem is defined here:
# %%
x, a1, a2, a3, a4 = sp.symbols("x, a1, a2, a3, a4", real=True)
expr = a1*sp.sin(x) + a2*sp.cos(x) + a3*sp.sin(2*x) + a4*sp.cos(2*x)

# %% [markdown]
# Apply the function to the expression, rewriting in terms of sine (first) and cosine (second):
# %%
trig_two_to_one(expr, to="sin")
trig_two_to_one(expr, to="cos")

# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="last_expr"