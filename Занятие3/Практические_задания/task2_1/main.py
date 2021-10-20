def pow_func(base, pow_=2):
    # base ** pow_ -> реализовать через цикл while
    res = 1
    base = base * base
    # while True:
    #     res = res * base
    #     pow_ = pow_ - 1
    #     if pow_ == 0:
    #         break

    while pow_ > 0:
        res = res * base
        pow_ = pow_ - 1

    return res


if __name__ == "__main__":
    a = 5
    n = 3

    print(pow_func(a, n))
