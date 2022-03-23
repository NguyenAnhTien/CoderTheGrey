
"""
@desc:
    - Finding the position of the first ocurrence of an element.
@author:
    - Coder The Grey
@date:
    - 2022/03/18
"""
def search(arrs, target):
    left = 0
    right = len(arrs) - 1
    pos = -1
    while left <= right:
        mid = (left + right) // 2
        if arrs[mid] == target:
            pos = mid
            right = mid - 1
        elif arrs[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return pos 

if __name__ == "__main__":
    arrs = [1, 2, 3, 3, 3, 3, 9, 13, 17, 17]
    target = 3
    index = search(arrs, target)
    print(index)
