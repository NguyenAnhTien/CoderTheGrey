"""
https://leetcode.com/problems/sqrtx/
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        """
        x = 8 ==> result = 2.828... ==> 2
        """
        low = 0
        high = x
        answer = None
        while low <= high:
            guess = (low + high) // 2
            if guess * guess == x:
                return guess
            if guess * guess < x:
                low = guess + 1
                answer = guess
            else:
                high = guess - 1
        return answer