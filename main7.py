def t(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        sum_var = 0
        for i in range(1, n + 1):
            sum_var = sum_var + (t(i - 1) * t(n - i))
        return sum_var


def t2(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        sum_var = 0
        for i in range(1, n + 1):
            if (i - 1) > 3:
                continue
            else:
                sum_var = sum_var + (t2(i - 1) * t2(n - i))
        return sum_var


def main():
    for i in range(1, 11):
        print("n: {}".format(i))
        print("Bn: {}".format(t(i)))
        print("Vn: {}".format(t2(i)))


if __name__ == "__main__":
    main()
