if __name__ == "__main__":
    cart = {
        "apple": 80,
        "orange": 65,
        "banana": 40
    }

    sum_ = 0
    for fruit in cart:
        sum_ += cart[fruit]
    print(sum_)  # получаем значение по ключу

    sum(cart.values())
    cart.items()
