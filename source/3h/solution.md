``` python
""""Solution to Chapter 3 problem 3H"""
import numpy as np
```

# Introduction
This program defines matrices A and B and vectors x and y. It then
computes several quantities that require matrix operations.
# a. Define Arrays

``` python
A = np.array(
    [
        [2, 1, 9, 0],
        [0, -1, -2, 3],
        [-3, 0, 8, -4],
    ]
)
B = np.array(
    [
        [0, 9, -1],
        [1, 0, 3],
        [0, -1, 1],
    ]
)
x = np.array([[1], [0], [-1]])
y = np.array([[3, 0, -1]])
```

# b. Compute and Print Quantitites

## i. $B A$

``` python
print("B A = \n", B @ A)
```

::: {.output .stream .stdout}
    B A = 
     [[  3  -9 -26  31]
     [ -7   1  33 -12]
     [ -3   1  10  -7]]
:::

## ii. $A^\top B - 6 J_{4\times 3}$

``` python
print("A.T B - 6 J_4x3 = \n", A.T @ B - 6 * np.ones((4, 3)))
```

::: {.output .stream .stdout}
    A.T B - 6 J_4x3 = 
     [[ -6.  15. -11.]
     [ -7.   3. -10.]
     [ -8.  67. -13.]
     [ -3.  -2.  -1.]]
:::

## iii. $B \bm{x} + \bm{y}^\top$

``` python
print("B x + y.T = \n", B @ x + y.T)
```

::: {.output .stream .stdout}
    B x + y.T = 
     [[ 4]
     [-2]
     [-2]]
:::

## iv. $\bm{x} \bm{y} + B$

``` python
print("x y + B = \n", x @ y + B)
```

::: {.output .stream .stdout}
    x y + B = 
     [[ 3  9 -2]
     [ 1  0  3]
     [-3 -1  2]]
:::

## v. $\bm{y} \bm{x}$

``` python
print("y x = \n", y @ x)
```

::: {.output .stream .stdout}
    y x = 
     [[4]]
:::

## vi. $\bm{y} B^{-1} \bm{x}$

``` python
print("y B^-1 x = \n", y @ np.linalg.inv(B) @ x)
```

::: {.output .stream .stdout}
    y B^-1 x = 
     [[10.]]
:::

## vii. $C B$

``` python
C = A[:, :3]  # First 3 columns of A (view)
print("C B = \n", C @ B)
```

::: {.output .stream .stdout}
    C B = 
     [[  1   9  10]
     [ -1   2  -5]
     [  0 -35  11]]
:::

```{=ipynb}
import sys

sys.path.append("../")
import engcom.engcom as engcom

pub = engcom.Publication(title="Problem 3H", author="Rico Picone")
pub.write(to="md")
```
