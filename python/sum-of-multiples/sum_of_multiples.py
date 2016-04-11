'''
Write a program that, given a number, can find the sum of all
the multiples of particular numbers up to but not including that
number.
'''


def sum_of_multiples(limit, numbers=None):
    if not numbers:
        numbers = [3, 5]

    multiples = set()
    for m in numbers:
        if m:
            for i in range(m, limit, m):
                multiples.add(i)
    return sum(multiples)


if __name__ == '__main__':
    print(sum_of_multiples(4))
    print(sum_of_multiples(20, [0, 3, 5]))
