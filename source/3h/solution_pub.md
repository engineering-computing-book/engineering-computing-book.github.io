::: {#239ac260 .cell .code execution_count="1" execution="{\"iopub.execute_input\":\"2024-03-10T05:37:38.439625Z\",\"iopub.status.busy\":\"2024-03-10T05:37:38.439474Z\",\"iopub.status.idle\":\"2024-03-10T05:37:38.512195Z\",\"shell.execute_reply\":\"2024-03-10T05:37:38.493661Z\"}"}
``` python
""""Solution to Chapter 3 problem 3H"""
import numpy as np
```
:::

::: {#8925e2c3 .cell .markdown lines_to_next_cell="0"}
# Introduction

This program defines matrices A and B and vectors x and y. It then
computes several quantities that require matrix operations.
:::

::: {#2ae930ab .cell .markdown lines_to_next_cell="0"}
# a. Define Arrays {#a-define-arrays}
:::

::: {#8f2b7dd3 .cell .code execution_count="2" execution="{\"iopub.execute_input\":\"2024-03-10T05:37:38.519726Z\",\"iopub.status.busy\":\"2024-03-10T05:37:38.518750Z\",\"iopub.status.idle\":\"2024-03-10T05:37:38.528251Z\",\"shell.execute_reply\":\"2024-03-10T05:37:38.526855Z\"}" lines_to_next_cell="0"}
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
:::

::: {#8fc45fa9 .cell .markdown lines_to_next_cell="0"}
# b. Compute and Print Quantitites {#b-compute-and-print-quantitites}

## i. $B A$ {#i-b-a}
:::

::: {#838dbafa .cell .code execution_count="3" execution="{\"iopub.execute_input\":\"2024-03-10T05:37:38.533637Z\",\"iopub.status.busy\":\"2024-03-10T05:37:38.533191Z\",\"iopub.status.idle\":\"2024-03-10T05:37:38.538615Z\",\"shell.execute_reply\":\"2024-03-10T05:37:38.537675Z\"}" lines_to_next_cell="0"}
``` python
print("B A = \n", B @ A)
```

::: {.output .stream .stdout}
    B A = 
     [[  3  -9 -26  31]
     [ -7   1  33 -12]
     [ -3   1  10  -7]]
:::
:::

::: {#048a01d1 .cell .markdown lines_to_next_cell="0"}
## ii. $A^\top B - 6 J_{4\times 3}$ {#ii-atop-b---6-j_4times-3}
:::

::: {#95d7ecf5 .cell .code execution_count="4" execution="{\"iopub.execute_input\":\"2024-03-10T05:37:38.544541Z\",\"iopub.status.busy\":\"2024-03-10T05:37:38.544135Z\",\"iopub.status.idle\":\"2024-03-10T05:37:38.550461Z\",\"shell.execute_reply\":\"2024-03-10T05:37:38.549328Z\"}" lines_to_next_cell="0"}
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
:::

::: {#5dedd9b3 .cell .markdown lines_to_next_cell="0"}
## iii. $B \bm{x} + \bm{y}^\top$ {#iii-b-bmx--bmytop}
:::

::: {#2187a031 .cell .code execution_count="5" execution="{\"iopub.execute_input\":\"2024-03-10T05:37:38.555654Z\",\"iopub.status.busy\":\"2024-03-10T05:37:38.555053Z\",\"iopub.status.idle\":\"2024-03-10T05:37:38.560004Z\",\"shell.execute_reply\":\"2024-03-10T05:37:38.559014Z\"}" lines_to_next_cell="0"}
``` python
print("B x + y.T = \n", B @ x + y.T)
```

::: {.output .stream .stdout}
    B x + y.T = 
     [[ 4]
     [-2]
     [-2]]
:::
:::

::: {#3c1ff6b6 .cell .markdown lines_to_next_cell="0"}
## iv. $\bm{x} \bm{y} + B$ {#iv-bmx-bmy--b}
:::

::: {#cd6f0ead .cell .code execution_count="6" execution="{\"iopub.execute_input\":\"2024-03-10T05:37:38.564861Z\",\"iopub.status.busy\":\"2024-03-10T05:37:38.564394Z\",\"iopub.status.idle\":\"2024-03-10T05:37:38.570462Z\",\"shell.execute_reply\":\"2024-03-10T05:37:38.569283Z\"}" lines_to_next_cell="0"}
``` python
print("x y + B = \n", x @ y + B)
```

::: {.output .stream .stdout}
    x y + B = 
     [[ 3  9 -2]
     [ 1  0  3]
     [-3 -1  2]]
:::
:::

::: {#65cc1c83 .cell .markdown lines_to_next_cell="0"}
## v. $\bm{y} \bm{x}$ {#v-bmy-bmx}
:::

::: {#c65eb4d8 .cell .code execution_count="7" execution="{\"iopub.execute_input\":\"2024-03-10T05:37:38.575741Z\",\"iopub.status.busy\":\"2024-03-10T05:37:38.575043Z\",\"iopub.status.idle\":\"2024-03-10T05:37:38.580840Z\",\"shell.execute_reply\":\"2024-03-10T05:37:38.579950Z\"}" lines_to_next_cell="0"}
``` python
print("y x = \n", y @ x)
```

::: {.output .stream .stdout}
    y x = 
     [[4]]
:::
:::

::: {#d7420fa0 .cell .markdown lines_to_next_cell="0"}
## vi. $\bm{y} B^{-1} \bm{x}$ {#vi-bmy-b-1-bmx}
:::

::: {#18cb0ef9 .cell .code execution_count="8" execution="{\"iopub.execute_input\":\"2024-03-10T05:37:38.586258Z\",\"iopub.status.busy\":\"2024-03-10T05:37:38.585528Z\",\"iopub.status.idle\":\"2024-03-10T05:37:38.592681Z\",\"shell.execute_reply\":\"2024-03-10T05:37:38.591732Z\"}" lines_to_next_cell="0"}
``` python
print("y B^-1 x = \n", y @ np.linalg.inv(B) @ x)
```

::: {.output .stream .stdout}
    y B^-1 x = 
     [[10.]]
:::
:::

::: {#1c691b9f .cell .markdown lines_to_next_cell="0"}
## vii. $C B$ {#vii-c-b}
:::

::: {#db67fd62 .cell .code execution_count="9" execution="{\"iopub.execute_input\":\"2024-03-10T05:37:38.599065Z\",\"iopub.status.busy\":\"2024-03-10T05:37:38.598892Z\",\"iopub.status.idle\":\"2024-03-10T05:37:38.603211Z\",\"shell.execute_reply\":\"2024-03-10T05:37:38.601784Z\"}"}
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
:::

::: {#99e6490b .cell .raw tags="[\"active-py\"]"}
```{=ipynb}
import sys

sys.path.append("../")
import engcom.engcom as engcom

pub = engcom.Publication(title="Problem 3H", author="Rico Picone")
pub.write(to="md")
```
:::
