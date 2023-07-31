def isValid(self, s: str) -> bool:
    table = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if table[c] != stack[-1]:
                return False
    return True
