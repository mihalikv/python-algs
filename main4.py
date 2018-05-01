matrix = []
bound = 2000


def main():
    global matrix
    f = open('IIII-ADS.txt', 'r')
    lines = f.readlines()
    matrix_size = int(lines[0])
    for i in range(1, matrix_size + 1):
        matrix.append([int(i) for i in lines[i].split(' ')])
    all_vertex = [i for i in range(matrix_size)]
    print(cost(all_vertex, 1))


def cost(S: list, i: int) -> int:
    global matrix
    if len(S) == 2:
        return matrix[0][i]
    else:
        S.remove(i)
        required = None
        for j in S:
            if required is None:
                required = cost(S, j) + matrix[i][j]
            else:
                required = min(required, cost(S, j) + matrix[i][j])
        return required

if __name__ == "__main__":
    main()
