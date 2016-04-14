def slices(series, length):
    if not 1 <= length <= len(series):
        raise ValueError("Invalid slice length: " + str(length))

    numbers = [int(digit) for digit in series]
    return [numbers[i:i + length]
            for i in range(0, len(series) - length + 1)]


def product(lst):
    result = 1
    for n in lst:
        result *= n
    return result


def largest_product(series, length):
    if length == 0:
        return 1
    return max(product(slice) for slice in slices(series, length))


if __name__ == '__main__':
    print(largest_product("0123456789", 2))
