::: {#9e0a0edb .cell .code execution_count="1" execution="{\"iopub.execute_input\":\"2024-03-10T05:37:40.955757Z\",\"iopub.status.busy\":\"2024-03-10T05:37:40.955625Z\",\"iopub.status.idle\":\"2024-03-10T05:37:41.564338Z\",\"shell.execute_reply\":\"2024-03-10T05:37:41.564009Z\"}"}
``` python
""""Solution to Chapter 3 problem Y1"""
import numpy as np
import matplotlib.pyplot as plt
import engcom.data
```
:::

::: {#26003d84 .cell .markdown lines_to_next_cell="0"}
# Introduction

This program loads ideal gas data with the engcom.data.ideal_gas()
function. It computes the work done by the gas over the given volume.
Finally, it charts the work for each temperature.
:::

::: {#33243530 .cell .markdown lines_to_next_cell="0"}
# Load the Data

Load the pressure-volume-temperature data as follows:
:::

::: {#07dd6822 .cell .code execution_count="2" execution="{\"iopub.execute_input\":\"2024-03-10T05:37:41.566367Z\",\"iopub.status.busy\":\"2024-03-10T05:37:41.566206Z\",\"iopub.status.idle\":\"2024-03-10T05:37:41.569152Z\",\"shell.execute_reply\":\"2024-03-10T05:37:41.568831Z\"}" lines_to_next_cell="1"}
``` python
d = engcom.data.ideal_gas(
    V=np.linspace(0.1, 2.1, 16),  # (m^3) Volume values
    T=np.array([300, 400, 500]),  # (K) Temperature values
)
```
:::

::: {#46dc1e51 .cell .markdown lines_to_next_cell="0"}
# Define and Compute the Work

Define a function to compute the work and apply the function.
:::

::: {#50e2bacd .cell .code execution_count="3" execution="{\"iopub.execute_input\":\"2024-03-10T05:37:41.570689Z\",\"iopub.status.busy\":\"2024-03-10T05:37:41.570575Z\",\"iopub.status.idle\":\"2024-03-10T05:37:41.572611Z\",\"shell.execute_reply\":\"2024-03-10T05:37:41.572346Z\"}"}
``` python
def W(P: np.ndarray, V: np.ndarray, axis: int = -1) -> float:
    """Use trapezoidal integration to estimate the work from P(V)"""
    return np.trapz(P, V, axis=0)
work = W(P=d["pressure"], V=d["volume"])
```
:::

::: {#5014df7f .cell .markdown}
# Plot

Create a bar chart of work for each temperature
:::

::: {#eae1a523 .cell .code execution="{\"iopub.execute_input\":\"2024-03-10T05:37:41.574066Z\",\"iopub.status.busy\":\"2024-03-10T05:37:41.573952Z\",\"iopub.status.idle\":\"2024-03-10T05:37:41.701072Z\",\"shell.execute_reply\":\"2024-03-10T05:37:41.699721Z\"}" tags="[\"remove_output\"]"}
``` python
x = np.arange(len(work))
labels = np.char.add(d["temperature"].flatten().astype(dtype=str), " K")
fig, ax = plt.subplots()
ax.bar(x, work / 1e6)
ax.set_xticks(x, labels=labels)
ax.set_ylabel("Work (MJ)")
plt.show()
```
:::

::: {#7bc2a354 .cell .code execution_count="5" execution="{\"iopub.execute_input\":\"2024-03-10T05:37:41.708184Z\",\"iopub.status.busy\":\"2024-03-10T05:37:41.707670Z\",\"iopub.status.idle\":\"2024-03-10T05:37:43.093715Z\",\"shell.execute_reply\":\"2024-03-10T05:37:43.093377Z\"}" tags="[\"remove_input\"]" transient="{\"remove_source\":true}"}
::: {.output .execute_result execution_count="5"}
![](source/y1/figure-0.pgf){#fig:y1-figure-0 .figure .pgf}
:::
:::
