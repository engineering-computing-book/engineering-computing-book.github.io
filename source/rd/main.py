# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="all"
# %matplotlib inline
import sympy as sp
import numpy as np

# %% [markdown]
# Symbolic vectors and matrices can be constructed, manipulated, and operated on with SymPy.
# Basic vectors and matrices are represented with the mutable `sp.matrices.dense.MutableDenseMatrix`{.py} class and can be constructed with the `sp.Matrix`{.py} constructor, as follows:
# %%
u = sp.Matrix([[0], [1], [2]])  # $3\times 1$ column vector
v = sp.Matrix([[3, 4, 5]])  # $1\times 3$ row vector
A = sp.Matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])  # $3\times 3$ matrix

# %% [markdown]
# \noindent
# Without loss of generality, we can refer to vectors and matrices as matrices.
#
# Symbolic variables can be elements of symbolic matrices; for instance, consider the following:
# %%
x1, x2, x3 = sp.symbols("x1, x2, x3")
x = sp.Matrix([[x1], [x2], [x3]])  # $3\times 1$ vector

# %% [markdown]
# Symbolic matrix elements can be accessed with the same slicing notation as `list`{.py}s and NumPy arrays; for insance: 
# %%
A[:,0]
A[0,:]
A[1,1:]
x[0:,0]

# %% [markdown]
# As with `list`{.py}s and contrary to arrays, these slices return a copy and not a view of the original matrix.
# Elements and slices can be overwritten with the same notation as `list`{.py}s and arrays, as follows:
# %%
A[0,0] = 7; A  # A is changed
A[:,1] = sp.Matrix([[8], [8], [8]]); A  # A is changed

# %% [markdown]
# Matrix row `i`{.py} or column `j`{.py} can be deleted with the `row_del(i)`{.py} or `col_del(j)`{.py} method.
# These methods operate in place.
# For instance,
# %%
A.row_del(2); A
A.col_del(1); A

# %% [markdown]
# Conversely, a row can be inserted at index `i`{.py} or a column can be inserted at index `j`{.py} with the method `row_insert(i, row)`{.py} or  `col_insert(j, col)`{.py}.
# These methods do not operate in place.
# For instance,
# %%
A.row_insert(2, sp.Matrix([[9, 9]]))  # A is unchanged
A.col_insert(1, sp.Matrix([[9], [9]]))  # A is unchanged

# %% [markdown]
# Addition and subtraction works element-wise, in accordance with the matrix mathematics, as follows:
# %%
A = sp.Matrix([[0, 1], [2, 3]])  # $2\times 2$ matrix
B = sp.Matrix([[4, 5], [6, 7]])  # $2\times 2$ matrix
A + B
A - B

# %% [markdown]
# Matrix multiplication is in accordance with mathematical matrix multiplication (i.e., not element-wise), as follows:
# %%
A*B
B*A

# %% [markdown]
# The matrix inverse, if it exists, can be computed by raising the matrix to the power `-1`{.py}, as follows:
# %%
A**-1
B**-1

# %% [markdown]
# The matrix transpose can be accessed as an attribute `T`{.py}, which returns a transposed copy, as follows:
# %%
A.T
B.T

# %% [markdown]
# An `n`{.py}-by-`n`{.py} identity matrix can be constructed via the `eye(n)`{.py} function, as follows:
# %%
sp.eye(3)

# %% [markdown]
# An `n`{.py}-by-`m`{.py} matrix with all `0`{.py} compenents can be constructed via the `zeros(n, m)`{.py} function, as follows:
# %%
sp.zeros(2,4)

# %% [markdown]
# Similarly, an `n`{.py}-by-`m`{.py} matrix with all `1`{.py} compenents can be constructed via the `ones(n, m)`{.py} function, as follows:
# %%
sp.ones(2,8)

# %% [markdown]
# A diagonal or block-diagonal matrix can be constructed by providing the diagonal elements to the `diag()`{.py} function, as follows:
# %%
D = sp.diag(1, 2, 3); D

# %% [markdown]
# The determinant of a matrix can be computed via the `det()`{.py} method, as follows:
# %%
D.det()

# %% [markdown]
# The eigenvalues and eigenvectors of a matrix can be computed via the `eigenvects()`{.py} method, which returns a list of tuples, one for each eigenvalue, of the form `(eval, m, evec)`{.py}, where `eval`{.py} is the eigenvalue, `m`{.py} is the corresponding algebraic multiplicity of the eigenvalue, and `evec`{.py} is the corresponding eigenvector.
# For instance,
# %%
A.eigenvects()

# %% tags=["remove_input"]
# %config InteractiveShell.ast_node_interactivity="last_expr"