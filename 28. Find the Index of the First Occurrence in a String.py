def strStr(haystack, needle):
    for i in range(len(haystack)):
        if needle == haystack:
            return 0
        for i in range(len(haystack)):
            k = i + len(needle)
            if k > len(haystack):
                break
            if haystack[i:k] == needle:
                return i
        return -1

