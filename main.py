def main():

    matrix = [
        [2, 4, 32, 5, 43],
        [3, 4, 32, 7, 53],
        [3, 15, 42, 99, 50],
        [6, 34, 33, 56, 47],
        [3, 5, 7, 24, 73]
    ]
    print("Початковий масив:")
    for row in matrix:
        row_str = " ".join(map(str, row))
        print(row_str)

    sums = []
    for row in matrix:
        row_sum = 0
        for element in row:
            row_sum += element
        sums.append(row_sum)

    n = len(matrix)
    for i in range(n):
        for j in range(n - 1):
            if sums[j] > sums[j + 1]:
                sums[j], sums[j + 1] = sums[j + 1], sums[j]
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]

    print("Відсортований масив:")
    for row in matrix:
        row_str = " ".join(map(str, row))
        print(row_str)


if __name__ == "__main__":
    main()
