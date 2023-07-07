def is_isogram(string):
    if not len(string):
        return True
    encountered = []
    for char in string.lower():
        if char in encountered:
            return False
        encountered.append(char)
    return True
