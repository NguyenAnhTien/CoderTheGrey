
def search(pattern, text):
    m = len(pattern)
    n = len(text)
    
    for index in range(n - m + 1):
        j = 0
        while j < m: #be careful with for in Python, not same as in C/C++
            if text[index + j] != pattern[j]:
                break
            j += 1
        if (j == m):
            return index
    return -1

if __name__ == '__main__':
    text = 'AAAABAAAB'
    pattern = 'AAB'
    pos = search(pattern, text)
    print(pos)