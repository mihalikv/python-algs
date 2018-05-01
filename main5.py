matrix = []
matrix_dynamic = []


def main():
    global matrix
    global matrix_dynamic
    f = open('IIIII-ADS.txt', 'r')
    lines = f.readlines()
    for line in lines:
        matrix.append([int(i) for i in line.split(' ')])
    matrix_dynamic.append(matrix[0])
    for index, line_in_matrix in enumerate(matrix):
        if index == 0:
            continue
        tmp = []
        for colmun_index, pixel in enumerate(line_in_matrix):
            if colmun_index == 0:
                min_demage = min(matrix_dynamic[index - 1][colmun_index], matrix_dynamic[index - 1][colmun_index + 1])
            elif colmun_index == len(line_in_matrix) - 1:
                min_demage = min(matrix_dynamic[index - 1][colmun_index - 1], matrix_dynamic[index - 1][colmun_index])
            else:
                min_demage = min(matrix_dynamic[index - 1][colmun_index - 1], matrix_dynamic[index - 1][colmun_index], matrix_dynamic[index - 1][colmun_index + 1])
            tmp.append(pixel + min_demage)
        matrix_dynamic.append(tmp)
    print(min(matrix_dynamic[999]))


if __name__ == "__main__":
    main()
