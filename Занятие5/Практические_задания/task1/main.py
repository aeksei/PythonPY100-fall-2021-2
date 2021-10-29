if __name__ == "__main__":

    matrix = [
        [i * j for j in range(1, 10)]
        for i in range(1, 10)
    ]

    for row in range(9):
        for col in range(9):
            ceil = matrix[row][col]
            print(f"{ceil:_>2}", end=" ")
        print()

