def on_square(square):
    return 2**(square - 1)


def total_after(square):
    return sum(on_square(n + 1) for n in range(square))


if __name__ == '__main__':
    print(on_square(2))
    print(total_after(2))
