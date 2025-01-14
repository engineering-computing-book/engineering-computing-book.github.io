def which_number(x):
    """Identifies which type of number the argument is.

    Args:
        x: A number
        
    Returns:
        A string "int", "float", or "complex", or None.
    """
    t = type(x)
    if t == int:
        return "int"
    elif t == float:
        return "float"
    elif t == complex:
        return "complex"
    else:
        return None

# Test which_number()
test_args = [42, 3.92, complex(2, -3), "3.92", [2, 0]]
for arg in test_args:
    r = which_number(arg)
    # Print with repr() so that strings are displayed quoted
    print(f"which_number({repr(arg)}) => {repr(r)}")