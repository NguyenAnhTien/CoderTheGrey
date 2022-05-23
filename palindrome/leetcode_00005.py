def is_palidrome(text, left, right):
    left_ = left
    right_ = right
    while left_ >= 0 and right_ < len(text) and text[left_] == text[right_]:
        left_ -= 1
        right_ += 1
    length = right_ - left_ - 1
    return length, left_ + 1, right_ - 1

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        for index in range(len(s)):
            odd_len, odd_left, odd_right = is_palidrome(s, index, index)
            even_len, even_left, even_right = is_palidrome(s, index, index + 1)

            start_ = even_left
            end_ = even_right

            if odd_len > even_len:
                start_ = odd_left
                end_ = odd_right

            # print(end - start)
            if (end - start) < (end_ - start_):
                start = start_
                end = end_

        return s[start : end + 1]
