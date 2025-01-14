# a. Define list l
l = [32, 41, 58, 34, 24, 53, 46, 41]

# b. Mean
m = sum(l)/len(l)
print(f"Mean: {m}")

# c. Max and min
max_ = max(l)
min_ = min(l)
print(f"Max: {max_}; Min: {min_}")

# d. Indices of max and min
# Note: If there is duplication of max or min, the first index is found
print(f"Max Index (first): {l.index(max_)}")
print(f"Min Index (first): {l.index(min_)}")

# e. Sort
l.sort() # Mutates l itself (returns None)
print(f"Sorted: {l}")