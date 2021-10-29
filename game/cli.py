from logic import init_field, is_empty_cell, set_cell, is_win, is_available_cell


def is_win_cli(field, player_symbol):
    if is_win(field):
        print(f"Победил игрок {player_symbol}")
        return True
    else:
        return False


def step_first_player(field: list, player_symbol: str):
    row_index, col_index = get_step(field, player_symbol)
    set_cell(field, row_index, col_index, player_symbol)
    print_field(field)


def step_second_player(field: list, player_symbol: str):
    step_first_player(field, player_symbol)


def print_field(field: list) -> None:
    for row in field:
        for cell in row:
            print(cell, end=" ")
        print()


def get_step(field: list, player_symbol: str) -> tuple[int, int]:
    while True:
        step = input(f"Игрок {player_symbol} "
                     f"введите две координаты через пробел: ")
        coords = step.split()
        if len(coords) < 2:
            print("Введено слишком мало координат")
            continue
        elif len(coords) > 2:
            print("Введено слишком много координат")
            continue

        x_str: str
        y_str: str
        x_str, y_str = coords

        if not x_str.isdigit():
            print("Координата x не число")
            continue

        if not y_str.isdigit():
            print("Координата y не число")
            continue

        x, y = int(x_str), int(y_str)

        if not 1 <= x <= 3:
            print("Неверная координата x")
            continue

        if not 1 <= y <= 3:
            print("Неверная координата y")
            continue

        return x-1, y-1


def main():
    size_field = 3
    field = init_field(size_field)
    print_field(field)

    first_player, second_player = "X", "O"

    while True:
        step_first_player(field, first_player)

        if is_win_cli(field, first_player):
            break

        if not is_available_cell(field):
            print("Ничья")
            break

        step_second_player(field, second_player)

        if is_win_cli(field, second_player):
            break

        if not is_available_cell(field):
            print("Ничья")
            break





if __name__ == '__main__':
    main()
