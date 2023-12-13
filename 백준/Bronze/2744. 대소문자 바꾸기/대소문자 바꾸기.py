upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

for c in list(input()):
    if c in upper:
        print(c.lower(), end="")
    else:
        print(c.upper(), end="")