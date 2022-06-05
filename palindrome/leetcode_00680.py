def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if is_palindrome(s, left + 1, right):
                    return True
                if is_palindrome(s, left, right - 1):
                    return True
                return False
        return True
