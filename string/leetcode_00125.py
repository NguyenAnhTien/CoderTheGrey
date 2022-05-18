class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""
        for char in s:
            if not char.isalpha() and not char.isnumeric():
                continue
            clean_str += char.lower()
        left = 0
        right = len(clean_str) - 1
        while left < right:
            if clean_str[left] != clean_str[right]:
                return False
            left += 1
            right -=1
        return True
