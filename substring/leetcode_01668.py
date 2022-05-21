"""
@author: Coder The Grey
@date: 2022-05-21
"""
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

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        t_len = len(sequence)
        w_len = len(word)

        result = 0
        max_repeat = t_len // w_len
        for num_repeat in range(max_repeat, 0, -1):
            pattern = word * num_repeat
            offset = search(pattern, sequence)
            if offset != -1:
                return num_repeat
        return 0
