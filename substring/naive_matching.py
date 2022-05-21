"""
@author: Coder The Grey
@desc:
    - Naive Solution of Substring Matching
"""
def search(pattern, text):
    """
    @return:
        offset: the leftmost ocurrence of pattern in the text
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

def search_v2(pattern, text):
    p_len = len(pattern)
    t_len = len(text)

    for offset in range(t_len - p_len + 1):
        #python string slice
        if text[offset : offset + p_len] == pattern:
            return offset
    return -1

if __name__ == '__main__':
    text = 'AAAABAAAB'
    pattern = 'AAB'
    offset = search_v2(pattern, text)
    print(f"Offset: {offset}")
