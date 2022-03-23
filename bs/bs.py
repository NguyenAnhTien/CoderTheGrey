"""
@desc:
    - Implement Binary Search
@author:
    - Coder The Grey
@date:
    - 2022/03/18
"""
def search(arrs, target):
    left = 0
    right = len(arrs) - 1
    while left <= right:
        mid = (left + right) // 2
        if arrs[mid] == target:
            return mid
        if arrs[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 

if __name__ == "__main__":
    arrs = [1, 2, 3, 3, 3, 7, 9, 13, 17, 17]
    target = 3
    index = search(arrs, target)
    print(index)
