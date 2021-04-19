board_list = list(range(1, 10))
win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
       (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def draw_board(board):
    """Функция рисования доски"""
    for i in range(3):
        print(f"|{board[i * 3]}|{board[i * 3 + 1]}|{board[i * 3 + 2]}|")


def check_data(count, x0):
    """Функция проверки введённых данных"""
    error_text = "Ошибка! Необходимо ввести число от 1 до 9"

    while True:
        data = input(f"Ход {count}-го игрока. Введите номер клетки:")
        try:
            data = int(data)
        except ValueError:
            print(error_text)
            continue

        if 1 <= data <= 9:
            if str(board_list[data - 1]) in "X0":
                print("Поле уже занято")
            else:
                board_list[int(data) - 1] = x0
                break
        else:
            print(error_text)
            continue


def bot():
    print("Ход компьютера. ")
    for i in range(len(board_list) - 1):
        if str(board_list[i]) not in "X0":
            board_list[int(i)] = "0"
            break
        else:
            continue


def check_win():
    """Функция проверки победителя"""
    for w in win:
        if board_list[w[0]] == board_list[w[1]] == board_list[w[2]]:
            return board_list[w[0]]


def main(board):
    """Основная функция"""
    print("-" * 3, "Игра крестики нолики для двух игроков", "-" * 3)

    counter = 0
    while True:
        draw_board(board)
        if counter % 2 == 0:
            check_data(1, "X")
        elif counter > 8:
            print("Ничья!")
            break
        else:
            # check_data(2, "0")
            bot()

        win_game = check_win()
        if win_game:
            print(f"Выиграл игрок -> {win_game} <-!")
            break

        counter += 1


main(board_list)
