\noindent
Data attributes can be defined via the usual variable assignment syntax and generally follow the docstring.
Method definitions follow data attributes.
Consider the following class definition to represent a screwdriver tool (perhaps in the context of a robot's inventory of available tools):

``` python
class Screwdriver:
    """Represents a screwdriver tool"""
    operates_on = "Screw"  # Class data attributes
    operated_by = "Hand"
    
    def drive(self, screw, angle):  # Method definition
        """Returns a screw object turned by the given angle"""
        return screw.turn(angle)
```

Any object that is an instance of the class `Screwdriver`{.py} will have the class attributes defined above.
To create an instance (i.e., instantiate), call the class name as if it were a function with no arguments, as follows:

``` python
sd1 = Screwdriver()  # Create an instance of the Screwdriver class
sd2 = Screwdriver()  # Another instance
sd1.operates_on  # Access class attributes
sd1.operated_by
```

::: {.output .execute_result execution_count="3"}
    'Screw'
:::

::: {.output .execute_result execution_count="3"}
    'Hand'
:::

In many cases, we will define a special [constructor method]{.keyword} named `__init__()`{.py}, which will be called at instatiation and passed any arguments provided as follows (we remove docstrings for brevity):

``` python
class Screwdriver:
    operates_on = "Screw"  # Class data attributes
    operated_by = "Hand"
    
    def __init__(self, head, length):
        self.head = head  # Instance data attributes
        self.length = length
    
    def drive(self, screw, angle):  # Method definition
        return screw.turn(angle)
```

\noindent
The attributes assigned to `self`{.py} in the `__init__()`{.py} method are called [instance data attributes]{.keyword}.
The arguments `head`{.py} and `length`{.py} are required positional arguments that are assigned to the instance data attributes `head`{.py} and `length`{.py}.

Consider the following instances:

``` python
sd1 = Screwdriver(head="Phillips", length=7)
sd2 = Screwdriver(head="Flat", length=8)
print(f"sd1 is a {sd1.head}head operated by {sd1.operated_by}")
print(f"sd2 is a {sd2.head}head operated by {sd2.operated_by}")
```

::: {.output .stream .stdout}
    sd1 is a Phillipshead operated by Hand
    sd2 is a Flathead operated by Hand
:::

\noindent
So we see that instances can have different instance data attributes but they share the same class data attributes.

Note that every method has as its first argument `self`{.py}, which is the conventional name given to the first argument, which is always the instance object that includes the method.
When calling a method of an instance, we do not provide the `self`{.py} argument because it is provided automatically.
Before we can call the `Screwdriver`{.py} method `drive()`{.py}, we should define a `Screw`{.py} class as follows:

``` python
class Screw:
    """Represents a screw fastener"""
    def __init__(self, head, angle=0, handed="Right"):
        self.head = head 
        self.angle = angle
        self.handed = handed
        
    def turn(self, angle):
        """Mutates angle attribute by adding angle"""
        self.angle += angle
```

Instances of the `Screw`{.py} class have $3$ instance attributes, `head`{.py}, `angle`{.py}, and `handed`{.py}.
Let's instantiate a screw and give it a turn as follows:

``` python
s1 = Screw(head="Phillips")
print(f"Initial angle: {s1.angle}")
sd1.drive(screw=s1, angle=3)  # Turn the screw 3 units
print(f"Mutated angle: {s1.angle}")
sd1.drive(screw=s1, angle=6)  # Turn the screw 6 units
print(f"Mutated angle: {s1.angle}")
```

::: {.output .stream .stdout}
    Initial angle: 0
    Mutated angle: 3
    Mutated angle: 9
:::

As we have seen in this example, instance data attributes can represent the [state]{.keyword} of an object and methods can mutate or [transition]{.keyword} that state.
This opens up a vast number of possibilities for the engineer, for we often need to keep track of the states and state transitions of objects in engineering systems.

## Derived Classes {#derived-classes h="5p"}

A [derived class]{.keyword} (also called a subclass) is a class that uses another class as its basis.
A class that is a derived class's basis is called a [base class]{.keyword} for the derived class.
A derived class [inherits]{.keyword} all of the class data attributes and methods of its base class, and it typically has additional class data attributes or methods of its own.

Continuing the screw and screwdriver example from above, let's define a derived class for representing set screws[^fn:set-screws] as follows:

``` python
class SetScrew(Screw):
    """Represents a set screw fastener"""
    def __init__(self, head, tip, angle=0, handed="Right"):
        self.tip = tip  # Add instance attribute
        super().__init__(head, angle, handed)  # Call base constructor
```

[^fn:set-screws]: A set screw is a screw that holds an object in place via a force applied by its tip.

\noindent
The base class was specified by placing it in parentheses in `SetScrew(Screw)`{.py}.
It is not necessary to define a new constructor, but to we did so to add the instance attribute `tip`{.py}.
Rather than duplicating the rest of the base class's constructor, the base constructor was called via `super().__init__()`{.py}, to which its relevant arguments were passed straight through.
Trying out the subclass,

``` python
sd3 = Screwdriver(head="Hex", length=5)
ss1 = SetScrew(head="Hex", tip="Nylon")
sd3.drive(ss1, 2)  # Drive the set screw
print(f"Set screw angle: {ss1.angle}")
```

::: {.output .stream .stdout}
    Set screw angle: 2
:::

\noindent
Note what has occurred: the `Screwdriver`{.py} instance `sd3`{.py} used its `drive()`{.py} method to call the `turn()`{.py} method of `SetScrew`{.py} instance `ss1`{.py}.
This `turn()`{.py} method was inherited from the `Screw`{.py} class, so we didn't have to repeat the definition of `turn()`{.py} in the subclass definition of `SetScrew`{.py}.
