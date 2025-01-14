def capital_only(l):
    """Return a list with only the strings from l that begin with
    capital letters.

    Args:
        l: A list of strings
    
    Returns:
        A new list of strings sans non-capitalized elements of l
        
    Raises:
        ValueError: If not all elements of l are strings
    """
    r = [] # Initialize return list
    for li in l:
        if type(li) == str:
            letter_start = li[0].isalpha() # First character is letter
            capitalized = li[0].capitalize() == li[0] # First is cap
            if letter_start and capitalized:
                    r.append(li)
        else:
            raise ValueError("All elements must be strings")
    return r

# Test capital_only()
test_args = [
    ["Foo", "Bar", "Baz"],
    ["Foo", "bar", "Baz"],
    ["Foo", 0, 1, "Bar", 2],
]
for arg in test_args:
    try:
        r = capital_only(arg)
        print(f"capital_only({repr(arg)}) => {repr(r)}")
    except ValueError as e: # Handle ValueError exception
        print(f"capital_only({repr(arg)}) => {type(e)}: {e}")