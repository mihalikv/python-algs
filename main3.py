matrix = []
bound = 2000


def main():
    global matrix
    f = open('II-ADS.txt', 'r')
    lines = [int(i) for i in f.readlines()]
    for index, k in enumerate(lines):
        tmp = []
        for index_b, B in enumerate(range(bound+1)):
            if index_b == 0:
                tmp.append(True)
            elif B == k:
                tmp.append(True)
            else:
                tmp.append(False)
        matrix.append(tmp)

    for index, k in enumerate(lines):
        if index == 0:
            continue
        for index_b, B in enumerate(range(bound+1)):
            if index_b == 0:
                continue
            if B < k:
                matrix[index][index_b] = matrix[index - 1][index_b]
            else:
                matrix[index][index_b] = matrix[index - 1][index_b] or matrix[index - 1][index_b - k]
            if index_b == bound and matrix[index][index_b]:
                print(index)
                return


    print(matrix[len(lines) - 1][bound])


if __name__ == "__main__":
    main()
