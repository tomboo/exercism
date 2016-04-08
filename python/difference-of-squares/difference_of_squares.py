def square_of_sum(n):
    sum = ((n + 1) * n) / 2
    squared = sum**2
    return squared


def sum_of_squares(n):
    sum = 0
    for i in range(n + 1):
        sum += i**2
    return sum


def difference(n):
    return square_of_sum(n) - sum_of_squares(n)


if __name__ == '__main__':
    print(difference(10))
