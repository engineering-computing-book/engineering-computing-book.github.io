import time  # Built-in module

with open("hamlet.txt", mode="r") as f:
    contents = f.read().splitlines()  # List of lines
for line in contents:
    print(line)
    time.sleep(3)
