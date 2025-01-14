Symbolic vectors and matrices can be constructed, manipulated, and operated on with SymPy.
Basic vectors and matrices are represented with the mutable `sp.matrices.dense.MutableDenseMatrix`{.py} class and can be constructed with the `sp.Matrix`{.py} constructor, as follows:

``` python
u = sp.Matrix([[0], [1], [2]])  # $3\times 1$ column vector
v = sp.Matrix([[3, 4, 5]])  # $1\times 3$ row vector
A = sp.Matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])  # $3\times 3$ matrix
```

\noindent
Without loss of generality, we can refer to vectors and matrices as matrices.

Symbolic variables can be elements of symbolic matrices; for instance, consider the following:

``` python
x1, x2, x3 = sp.symbols("x1, x2, x3")
x = sp.Matrix([[x1], [x2], [x3]])  # $3\times 1$ vector
```

Symbolic matrix elements can be accessed with the same slicing notation as `list`{.py}s and NumPy arrays; for insance: 

``` python
A[:,0]
A[0,:]
A[1,1:]
x[0:,0]
```

::: {.output .execute_result execution_count="4"}
```{=latex}
$\displaystyle \left[\begin{matrix}0\\3\\6\end{matrix}\right]$
```
:::

::: {.output .execute_result execution_count="4"}
```{=latex}
$\displaystyle \left[\begin{matrix}0 & 1 & 2\end{matrix}\right]$
```
:::

::: {.output .execute_result execution_count="4"}
```{=latex}
$\displaystyle \left[\begin{matrix}4 & 5\end{matrix}\right]$
```
:::

::: {.output .execute_result execution_count="4"}
```{=latex}
$\displaystyle \left[\begin{matrix}x_{1}\\x_{2}\\x_{3}\end{matrix}\right]$
```
:::

As with `list`{.py}s and contrary to arrays, these slices return a copy and not a view of the original matrix.
Elements and slices can be overwritten with the same notation as `list`{.py}s and arrays, as follows:

``` python
A[0,0] = 7; A  # A is changed
A[:,1] = sp.Matrix([[8], [8], [8]]); A  # A is changed
```

::: {.output .execute_result execution_count="5"}
```{=latex}
$\displaystyle \left[\begin{matrix}7 & 1 & 2\\3 & 4 & 5\\6 & 7 & 8\end{matrix}\right]$
```
:::

::: {.output .execute_result execution_count="5"}
```{=latex}
$\displaystyle \left[\begin{matrix}7 & 8 & 2\\3 & 8 & 5\\6 & 8 & 8\end{matrix}\right]$
```
:::

Matrix row `i`{.py} or column `j`{.py} can be deleted with the `row_del(i)`{.py} or `col_del(j)`{.py} method.
These methods operate in place.
For instance,

``` python
A.row_del(2); A
A.col_del(1); A
```

::: {.output .execute_result execution_count="6"}
```{=latex}
$\displaystyle \left[\begin{matrix}7 & 8 & 2\\3 & 8 & 5\end{matrix}\right]$
```
:::

::: {.output .execute_result execution_count="6"}
```{=latex}
$\displaystyle \left[\begin{matrix}7 & 2\\3 & 5\end{matrix}\right]$
```
:::

Conversely, a row can be inserted at index `i`{.py} or a column can be inserted at index `j`{.py} with the method `row_insert(i, row)`{.py} or  `col_insert(j, col)`{.py}.
These methods do not operate in place.
For instance,

``` python
A.row_insert(2, sp.Matrix([[9, 9]]))  # A is unchanged
A.col_insert(1, sp.Matrix([[9], [9]]))  # A is unchanged
```

::: {.output .execute_result execution_count="7"}
```{=latex}
$\displaystyle \left[\begin{matrix}7 & 2\\3 & 5\\9 & 9\end{matrix}\right]$
```
:::

::: {.output .execute_result execution_count="7"}
```{=latex}
$\displaystyle \left[\begin{matrix}7 & 9 & 2\\3 & 9 & 5\end{matrix}\right]$
```
:::

Addition and subtraction works element-wise, in accordance with the matrix mathematics, as follows:

``` python
A = sp.Matrix([[0, 1], [2, 3]])  # $2\times 2$ matrix
B = sp.Matrix([[4, 5], [6, 7]])  # $2\times 2$ matrix
A + B
A - B
```

::: {.output .execute_result execution_count="8"}
```{=latex}
$\displaystyle \left[\begin{matrix}4 & 6\\8 & 10\end{matrix}\right]$
```
:::

::: {.output .execute_result execution_count="8"}
```{=latex}
$\displaystyle \left[\begin{matrix}-4 & -4\\-4 & -4\end{matrix}\right]$
```
:::

Matrix multiplication is in accordance with mathematical matrix multiplication (i.e., not element-wise), as follows:

``` python
A*B
B*A
```

::: {.output .execute_result execution_count="9"}
```{=latex}
$\displaystyle \left[\begin{matrix}6 & 7\\26 & 31\end{matrix}\right]$
```
:::

::: {.output .execute_result execution_count="9"}
```{=latex}
$\displaystyle \left[\begin{matrix}10 & 19\\14 & 27\end{matrix}\right]$
```
:::

The matrix inverse, if it exists, can be computed by raising the matrix to the power `-1`{.py}, as follows:

``` python
A**-1
B**-1
```

::: {.output .execute_result execution_count="10"}
```{=latex}
$\displaystyle \left[\begin{matrix}- \frac{3}{2} & \frac{1}{2}\\1 & 0\end{matrix}\right]$
```
:::

::: {.output .execute_result execution_count="10"}
```{=latex}
$\displaystyle \left[\begin{matrix}- \frac{7}{2} & \frac{5}{2}\\3 & -2\end{matrix}\right]$
```
:::

The matrix transpose can be accessed as an attribute `T`{.py}, which returns a transposed copy, as follows:

``` python
A.T
B.T
```

::: {.output .execute_result execution_count="11"}
```{=latex}
$\displaystyle \left[\begin{matrix}0 & 2\\1 & 3\end{matrix}\right]$
```
:::

::: {.output .execute_result execution_count="11"}
```{=latex}
$\displaystyle \left[\begin{matrix}4 & 6\\5 & 7\end{matrix}\right]$
```
:::

An `n`{.py}-by-`n`{.py} identity matrix can be constructed via the `eye(n)`{.py} function, as follows:

``` python
sp.eye(3)
```

::: {.output .execute_result execution_count="12"}
```{=latex}
$\displaystyle \left[\begin{matrix}1 & 0 & 0\\0 & 1 & 0\\0 & 0 & 1\end{matrix}\right]$
```
:::

An `n`{.py}-by-`m`{.py} matrix with all `0`{.py} compenents can be constructed via the `zeros(n, m)`{.py} function, as follows:

``` python
sp.zeros(2,4)
```

::: {.output .execute_result execution_count="13"}
```{=latex}
$\displaystyle \left[\begin{matrix}0 & 0 & 0 & 0\\0 & 0 & 0 & 0\end{matrix}\right]$
```
:::

Similarly, an `n`{.py}-by-`m`{.py} matrix with all `1`{.py} compenents can be constructed via the `ones(n, m)`{.py} function, as follows:

``` python
sp.ones(2,8)
```

::: {.output .execute_result execution_count="14"}
```{=latex}
$\displaystyle \left[\begin{matrix}1 & 1 & 1 & 1 & 1 & 1 & 1 & 1\\1 & 1 & 1 & 1 & 1 & 1 & 1 & 1\end{matrix}\right]$
```
:::

A diagonal or block-diagonal matrix can be constructed by providing the diagonal elements to the `diag()`{.py} function, as follows:

``` python
D = sp.diag(1, 2, 3); D
```

::: {.output .execute_result execution_count="15"}
```{=latex}
$\displaystyle \left[\begin{matrix}1 & 0 & 0\\0 & 2 & 0\\0 & 0 & 3\end{matrix}\right]$
```
:::

The determinant of a matrix can be computed via the `det()`{.py} method, as follows:

``` python
D.det()
```

::: {.output .execute_result execution_count="16"}
```{=latex}
$\displaystyle 6$
```
:::

The eigenvalues and eigenvectors of a matrix can be computed via the `eigenvects()`{.py} method, which returns a list of tuples, one for each eigenvalue, of the form `(eval, m, evec)`{.py}, where `eval`{.py} is the eigenvalue, `m`{.py} is the corresponding algebraic multiplicity of the eigenvalue, and `evec`{.py} is the corresponding eigenvector.
For instance,

``` python
A.eigenvects()
```

::: {.output .execute_result execution_count="17"}
    [(3/2 - sqrt(17)/2,
      1,
      [Matrix([
       [-sqrt(17)/4 - 3/4],
       [                1]])]),
     (3/2 + sqrt(17)/2,
      1,
      [Matrix([
       [-3/4 + sqrt(17)/4],
       [                1]])])]
:::
