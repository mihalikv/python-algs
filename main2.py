matrix = [[], []]


def main():
    global matrix
    f = open('I-ADS.txt', 'r')
    line = list(f.readlines()[0])
    numbers = [int(x) for x in line]
    # print(numbers)

    # optimal_solution = [0 for x in range(len(numbers))]
    splitted = []
    half = int(len(numbers) / 2)
    for i in range(1, half + 1):
        splitted.append(numbers[half - i:half + i])
    for index, array in enumerate(splitted):
        l, r = test(index, array)
        matrix[0].append(l)
        matrix[1].append(r)
    print(matrix[0][499])
    print(matrix[1][499])


def test(index, array):
    global matrix
    if len(array) == 2:
        return array[0], array[1]
    else:
        return array[0] + matrix[1][index-1], array[-1] + matrix[0][index-1]


if __name__ == "__main__":
    main()
