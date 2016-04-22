def prime_factors(n):
    primes = []
    candidate = 2
    while n > 1:
        while n % candidate == 0:
            primes.append(candidate)
            n //= candidate
        candidate += 1
    return primes


if __name__ == '__main__':
    for n in range(2, 25):
        print(n, ': ', prime_factors(n))
