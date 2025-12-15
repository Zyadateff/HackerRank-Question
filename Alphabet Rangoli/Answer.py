def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    width = 4 * size - 3
    lines = []

    for i in range(size):
        left = alpha[size-1: size-1-i: -1]
        right = alpha[size-1-i: size]
        s = "-".join(left + right)
        lines.append(s.center(width, "-"))
    full_rangoli = lines + lines[-2::-1]

    print("\n".join(full_rangoli))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
