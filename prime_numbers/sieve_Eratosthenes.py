"""
"""
def sieve_primes(max_num):
    primes = [True] * (max_num + 1)
    primes[0] = False
    primes[1] = False
    for number in range(2, max_num + 1):
        if primes[number] == True:
            factor = 2
            while number * factor <= max_num:
                primes[number * factor] = False
                factor += 1
    results = []
    for number in range(2, max_num + 1):
        if primes[number] == True:
            results.append(number)
    return results

if __name__ == '__main__':
    results = sieve_primes(100)
    print(results)