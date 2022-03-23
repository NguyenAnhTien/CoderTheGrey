"""
@date: 2022-03-18
@author: Coder The Grey
@desc: Find the square root of a integer number.
"""

def find_square_root(number):
    low = 0
    right = number
    while low <= right:
        guess = (low + right) // 2
        if guess * guess == number:
            return guess
        if guess * guess < number:
            low = guess + 1
        else:
            right = guess - 1
    return None

if __name__ == '__main__':
    number = 5
    result = find_square_root(number)
    print(result)
