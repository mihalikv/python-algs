MAX_WEIGHT = 2000


def main():
    values = []
    weights = []
    f = open('ADS.txt', 'r')
    for line in f.readlines():
        splitted = line.split(',')
        values.append([int(splitted[0]), int(splitted[2])])
        weights.append([int(splitted[1]), int(splitted[3])])

    print(values)
    print(weights)
    new_values, new_weights = preparation(values, weights)
    print(knapsac(new_values, new_weights))


def preparation(values, weights):
    better_values, better_weights = [], []
    for i in range(len(values)):
        if (values[i][0] * weights[i][0]) > (values[i][1] * weights[i][1]):
            better_values.append(values[i][0])
            better_weights.append(weights[i][0])
        else:
            better_values.append(values[i][1])
            better_weights.append(weights[i][1])
    return better_values, better_weights


def knapsac(values, weights):
    matrix = [[0 for x in range(MAX_WEIGHT + 1)] for y in range(len(values) + 1)]
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            matrix[i][j] = matrix[i - 1][j]
            if weights[i - 1] > j:
                continue
            candidate = matrix[i - 1][j - weights[i - 1]] + values[i - 1]
            if candidate > matrix[i][j]:
                matrix[i][j] = candidate

    return matrix[len(values)][MAX_WEIGHT]


if __name__ == "__main__":
    main()
