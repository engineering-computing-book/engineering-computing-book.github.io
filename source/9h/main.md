Load the NumPy package:

``` python
import numpy as np
```

## Define Classes {-}
The following `Screwdriver`{.py} class meets the requirements:

``` python
class Screwdriver:
    """Represents a screwdriver tool"""
    operates_on = "Screw"  # Class data attributes
    operated_by = "Hand"
    
    def __init__(self, head, length):
        self.head = head  # Instance data attributes
        self.length = length
    
    def drive(self, screw, angle):  # Method definition
        """Returns a screw object turned by the given angle"""
        if screw.head != self.head:
            raise TypeError(f"{self.head} screwdriver "
                f"can't turn a {screw.head} screw.")
        screw.turn(angle)
        return screw
```

The following `Screw`{.py} class meets the requirements:

``` python
class Screw:
    """Represents a screw fastener"""
    def __init__(self, head, pitch, depth=0, angle=0, handed="Right"):
        self.head = head
        self.pitch = pitch
        self.depth = depth
        self.angle = angle
        self.handed = handed
        
    def turn(self, angle):
        """Mutates angle and depth for a turn of angle rad"""
        if self.handed == "Right":
            handed_sign = 1
        else:
            handed_sign = -1
        self.angle += angle
        self.depth += handed_sign * self.pitch * angle / (2*np.pi)
```

The following `MetricScrew`{.py} class meets the requirements:

``` python
class MetricScrew(Screw):
    """Represents a metric screw fastener"""
    kind = "Metric"
    # No constructor necessary because we aren't 
    # changing instance attributes
```

## Test the New Features {-}
Create a `MetricScrew`{.py} instance as follows:

``` python
ms1 = MetricScrew(head="Flat", pitch=2)
```

Create a flathead screwdriver instance:

``` python
sd1 = Screwdriver(head="Flat", length=6)
```

Turn the screw $5$ complete clockwise revolutions with the screwdriver and print the resulting angle and depth as follows:

``` python
sd1.drive(ms1, 5*2*np.pi)
print(f"Angle: {ms1.angle:.3g} rad \nDepth: {ms1.depth} mm")
```

::: {.output .execute_result execution_count="8"}
    <__main__.MetricScrew at 0x11d678750>
:::

::: {.output .stream .stdout}
    Angle: 31.4 rad 
    Depth: 10.0 mm
:::

Turn the screw $3$ complete counterclockwise revolutions with the screwdriver and print the resulting angle and depth as follows:

``` python
sd1.drive(ms1, -3*2*np.pi)
print(f"Angle: {ms1.angle:.3g} rad \nDepth: {ms1.depth} mm")
```

::: {.output .execute_result execution_count="9"}
    <__main__.MetricScrew at 0x11d678750>
:::

::: {.output .stream .stdout}
    Angle: 12.6 rad 
    Depth: 4.0 mm
:::

Create a left-handed `MetricScrew`{.py} instance as follows:

``` python
ms2 = MetricScrew(head="Flat", pitch=2, handed="Left")
```

Turn the `ms2`{.py} screw $4$ complete counterclockwise revolutions with the `sd1`{.py} screwdriver and print the resulting angle and depth of `ms2`{.py} as follows:

``` python
sd1.drive(ms2, -3*2*np.pi)
print(f"Angle: {ms2.angle:.3g} rad \nDepth: {ms2.depth} mm")
```

::: {.output .execute_result execution_count="11"}
    <__main__.MetricScrew at 0x11d67a1d0>
:::

::: {.output .stream .stdout}
    Angle: -18.8 rad 
    Depth: 6.0 mm
:::

Turn the `ms2`{.py} screw $2$ complete clockwise revolutions with the `sd1`{.py} screwdriver and print the resulting angle and depth of `ms2`{.py} as follows:

``` python
sd1.drive(ms2, 2*2*np.pi)
print(f"Angle: {ms2.angle:.3g} rad \nDepth: {ms2.depth} mm")
```

::: {.output .execute_result execution_count="12"}
    <__main__.MetricScrew at 0x11d67a1d0>
:::

::: {.output .stream .stdout}
    Angle: -6.28 rad 
    Depth: 2.0 mm
:::

Create an instance `sd2`{.py} of `Screwdriver`{.py} with a hex head and try to turn the `sd1`{.py} screw and catch and print the exception as follows:

``` python
sd2 = Screwdriver(head="Hex", length=6)
try:
    sd2.drive(ms1, 1)  # Should raise an exception
except Exception as err:
    print(f"Unexpected {type(err)}: {err}")  # Print the exception
```

::: {.output .stream .stdout}
    Unexpected <class 'TypeError'>: Hex screwdriver can't turn a Flat screw.
:::
