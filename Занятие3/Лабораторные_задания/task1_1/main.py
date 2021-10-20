def task_1_1():
    max_sum = 500
    current_sum = 0
    n = 1
    while True:
        current_value = n ** 2
        if current_sum + current_value > max_sum:
            return n
        else:
            current_sum += current_value
            return n
            # n = n + 1
            # print(n, current_sum)


if __name__ == "__main__":
    print(task_1_1())
