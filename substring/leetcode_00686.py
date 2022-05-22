def search(pattern, text):
    """
    @return:
        -) offset: the leftmost ocurrence of pattern in the text
    """
    p_len = len(pattern)
    t_len = len(text)

    for offset in range(t_len - p_len + 1):
        pointer = 0 #j
        while pointer < p_len:
            if text[offset + pointer] != pattern[pointer]:
                #mismatch
                break
            pointer += 1
        if pointer == p_len:
            return offset
    return -1

def repeatedStringMatch(a, b):
    low = 1
    high = (len(b) + len(a)) * 2
    while low < high:
        mid = (low + high) // 2
        text = a * mid
        offset = search(b, text)
        import ipdb
        # ipdb.set_trace()
        if offset == -1:
            low = mid + 1
        else:
            high = mid

    offset = search(b, a * low)
    if offset != -1:
        return low
    return -1

a = "abcd"
b = "cdabcdab"

repeatedStringMatch(a, b)
