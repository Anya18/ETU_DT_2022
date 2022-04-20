import numpy as np

VAR = 1
LEFT_BOUND = 1 / (VAR + 1)
RIGHT_BOUND = VAR + 1


def Bayes_criterion(matrix, probabilities):
    means = (probabilities * matrix).sum(axis=1)
    print('\nМатематическое ожидание:')
    print(means.round(3))
    max_means = means.max()
    print('\nНаибольшее математическое ожидание:')
    print(max_means.round(3))
    print('\nОптимальная стратегия (индекс максимального матожидания):')
    print(np.where(max_means == means)[0][0]+1)


if __name__ == '__main__':
    matrix = np.random.uniform(low=LEFT_BOUND, high=RIGHT_BOUND, size=(10, 10))
    print('Входная матрица:')
    print(matrix.round(3))

    line = np.random.uniform(low=LEFT_BOUND, high=RIGHT_BOUND, size=10)
    probabilities = line / sum(line)
    print('\nСтрока вероятностей для критерия Байеса:')
    print(probabilities.round(3))

    Bayes_criterion(matrix, probabilities)