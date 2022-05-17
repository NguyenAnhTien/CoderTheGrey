
def search(pattern, text):
    M = len(pattern)
    N = len(text)
    i = 0
    j = 0
    while i < N and j < M:
        if pattern[j] == text[i]:
            j += 1
        else:
            i -= j
            j = 0
        i += 1
    if j == M:
        return (i - M)
    return -1

if __name__ == '__main__':
    text = 'AAAABAAAB'
    pattern = 'AAB'
    pos = search(pattern, text)
    print(pos)
