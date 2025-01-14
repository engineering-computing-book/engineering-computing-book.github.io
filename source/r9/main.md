Load packages:

``` python
import numpy as np
import matplotlib.pyplot as plt
```

## Define the Class {-}

Here is a basic `Polygon`{.py} class definition:

``` python
class Polygon:
    """A polygon defined by its vertices."""
    def __init__(self, vertices: list):
        self.vertices = vertices  # Vertices attribute
```

This can be initialized with a list of vertex tuples.
Now let's add a `plot()`{.py} method as follows:

``` {.python .nosamepage}
class Polygon:
    """A polygon defined by its vertices."""
    def __init__(self, vertices: list):
        self.vertices = vertices  # Vertices attribute
        self.n = len(vertices)  # Number of vertices
    
    def plot(self, R: tuple | None = None, ax=None):
        """Plot the polygon as a closed curve and a point R"""
        vertices_a = np.array(self.vertices).T
        # Initialize and fill most of the x, y arrays
        x = np.full(self.n + 1, np.nan)  # +1 to repeat the first point
        x[0:self.n] = vertices_a[0]
        y = np.full(self.n + 1, np.nan)  # +1 to repeat the first point
        y[0:self.n] = vertices_a[1]
        # Add the first point to the end
        x[-1] = x[0]
        y[-1] = y[0]
        # Plot
        if ax is None:
            fig, ax = plt.subplots()
        ax.plot(x, y)
        if R is not None:
            ax.scatter(R[0], R[1])
            ax.annotate(
                "$R$", R, 
                xytext=(5, 5), textcoords='offset points'
            )
        return ax
        
    def vectors(self, R:tuple) -> list:
        """Returns the vectors from R to vertices of the polygon"""
        rs = []
        for p in self.vertices:
            rs.append(np.array(p) - np.array(R))  # Difference in x, y
        return rs
    
    def winding_number(self, R: tuple) -> int:
        """Returns the winding number for point R"""
        rs = self.vectors(R)  # Vectors from R to each P vertex
        thetas = np.full(self.n, np.nan)  # Initialize
        for i in range(self.n):
            j = (i+1) % self.n  # Wrap i+1 back to 0
            phi_i = np.arctan2(rs[i][1], rs[i][0])  # Angle of $\vec{r}_i$
            phi_j = np.arctan2(rs[j][1], rs[j][0])  # Angle of $\vec{r}_{i+1}$
            if phi_j - phi_i < -np.pi:  # Handle 2*pi wrapping
                thetas[i] = phi_j - phi_i + 2*np.pi  # $\theta_i$
            elif phi_j - phi_i > np.pi:  # Handle 2*pi wrapping
                thetas[i] = phi_j - phi_i - 2*np.pi  # $\theta_i$
            else:
                thetas[i] = phi_j - phi_i  # $\theta_i$
        omega = np.round(1/(2*np.pi) * np.sum(thetas))
        return omega
    
    def is_inside(self, R: tuple) -> bool:
        """Returns True if R in polygon, False otherwise"""
        omega = self.winding_number(R)
        if omega == 0:
            return False
        else:
            return True
```

## Test the Class {-}

Create the test polygons and points as follows:

``` python
polygons = [
    Polygon([
        (5, 1), (2, 3), (-2, 3.5), (-4, 1), (-2, 1.5), 
        (-2, -2), (-5, -3), (2, -2.5), (5.5, -1)
    ]),
    Polygon([
        (4, 1), (1, 2), (-1, 1), (-4, 2), (-5, -2), 
        (-3, -2), (-5, -3), (2, -2), (5, -2)
    ]),
]
points = [(0, 0), (-4, 0)]
```

Graph the polygons and points as follows:

``` {.python .remove-output}
places = []
fig, axs = plt.subplots(2, 2)
for i, poly in enumerate(polygons):
    for j, R in enumerate(points):
        poly.plot(R, ax=axs[i, j])
        if poly.is_inside(R):
            places.append(f"R = {R} is inside polygon {i}")
        else:
            places.append(f"R = {R} is outside polygon {i}")
plt.show()
```

::: {.output .execute_result .remove-input execution_count="7"}
![The polygons and points.](source/r9/figure-0.pgf){#fig:r9-figure-0 .figure .pgf}
:::

Print the test results from `is_inside()`{.py} as follows:

``` python
for place in places:
    print(place)
```

::: {.output .stream .stdout}
    R = (0, 0) is inside polygon 0
    R = (-4, 0) is outside polygon 0
    R = (0, 0) is inside polygon 1
    R = (-4, 0) is inside polygon 1
:::
