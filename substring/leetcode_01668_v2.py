def search(pattern, text):
    t_len = len(text)
    p_len = len(pattern)

    i = 0
    j = 0

    while i < t_len and j < p_len: #O((N - M)M)
        if pattern[j] == text[i]:
            j += 1
        else:
            i -= j #reset
            j = 0
        i += 1
    if j == p_len:
        return (i - p_len)
    return -1

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        word = "ab"
        --> 2-repeating: abab

        "aaabaaaab aaaba aaaba aaaba aaaba aaaba"
        "aaaba"

        --> output = 5
        """

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
