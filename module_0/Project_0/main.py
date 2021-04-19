import numpy as np


def game_core_v3(number):
    """Функция поиска загаданного числа с помощью
    алгоритма бинарного поиска"""
    first = 1
    last = 100
    count = 1
    predict = (first + last) // 2

    while number != predict:    # цикл проверки загаданного числа
        predict = (first + last) // 2

        if number > predict:
            first = predict + 1
        elif number < predict:
            last = predict - 1

        count += 1
    return count


def score_game(game_core):
    """Функция генерации списка рандомных чисел и
    подсчёт среднего числа попыток их отгадывания"""
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return score


score_game(game_core_v3)
