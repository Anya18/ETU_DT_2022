if __name__ == '__main__':
    matrix = [[4,  8, -1, -2],
              [5,  9,  3,  2],
              [5, -7, -2,  4]]
    min_els = []
    for line in matrix:
        min_els.append(min(line))
        print('Минимальное в строке', len(min_els), ': ', min_els[-1])

    alfa = max(min_els)
    print('alfa : ', alfa)

    max_els = []
    for i in range(0, len(matrix[0])):
        max_els.append(matrix[0][i])
        for j in range(0, len(matrix)):
            if matrix[j][i] > max_els[-1]:
                max_els[-1] = matrix[j][i]
        print('Максимальное в столбце', len(max_els), ': ', max_els[-1])

    beta = min(max_els)
    print('beta : ', beta)

