def sieve(limit):
    prime = [True] * (limit + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, limit + 1, i):
                prime[j] = False

    return [i for i, val in enumerate(prime) if val]


if __name__ == '__main__':
    print(sieve(10))
