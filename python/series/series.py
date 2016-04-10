def slices(series, length):
    if not 1 <= length <= len(series):
        raise ValueError("Invalid slice length: " + str(length))

    numbers = [int(c) for c in series]
    return [numbers[i:i + length]
            for i in range(0, len(series) - length + 1)]


if __name__ == '__main__':
    s = "9876"
    print(slices(s, 2))
