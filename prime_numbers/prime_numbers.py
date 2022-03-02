
def is_prime(number):
    if number <= 1:
        return False
    for factor in range(2, int(number ** 0.5) + 1):
        if number % factor == 0:
            return False
    return True

if __name__ == '__main__':
    number = int(input())
    print(f"{number} is Prime Number. True or False? {is_prime(number)}")
