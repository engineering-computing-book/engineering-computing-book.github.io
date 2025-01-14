def float_list(l):
    """Return a list with all elements converted to floats.

    Args:
        l: A list
    
    Returns:
        New list with elements of l that could be converted to floats
    """
    if type(l) != list:
        return []
    r = [] # Initialize return list
    for li in l:
        if type(li) == float or type(li) == complex:
            r.append(li)
        else:
            try: # converting to a float
                li_float = float(li) # If this throws exception then
                r.append(li_float)   # ... this will not execute
            except:
                continue
    return r

# Test float_list()
test_args = [
    [1.1, 0.2, 4.2, -30.2],
    [3, 42, -32, 0, 3],
    [1-3j, 2, 0.3],
    ["1.2", "8", "-3.9"],
    ["0.4", "dog", None, 8],
    3.4,
]
for arg in test_args:
    r = float_list(arg)
    print(f"float_list({repr(arg)}) => {repr(r)}")