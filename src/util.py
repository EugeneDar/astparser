def nth_substring(string, substring, n):
    val = -1
    for i in range(0, n):
        val = string.find(substring, val + 1)
    return val
