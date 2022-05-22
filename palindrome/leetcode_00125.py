
def isPalindrome(s):
    clean_str = ""
    for char in s:
        if char.isalpha() or char.isnumeric():
            clean_str += char.lower()

    center = (0 + len(clean_str)) // 2
    left = center
    right = center
    while left <= 0 and right < len(clean_str) and clean_str[left] == clean_str[right]:
        left -= 1
        right += 1

    if (right - left -1) != len(clean_str):
        return True
    return False

if __name__ == '__main__':
    s = "race a car"
    print(isPalindrome(s))
