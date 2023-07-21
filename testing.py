arr = ["a", "b", "a", "c", "c"]

new = []
for n in arr:
    if n not in new:
        new.append(n)

print(new)
