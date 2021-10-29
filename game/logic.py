EMPTY_CELL = "-"


def init_field(size=3):
    field = [
        [EMPTY_CELL for _ in range(size)]
        for _ in range(size)
    ]

    return field


def get_cell(field: list, row_index: int, col_index: int):
    return field[row_index][col_index]


def set_cell(field: list, row_index: int, col_index: int,
             symbol) -> None:
    field[row_index][col_index] = symbol


def is_win(field) -> bool:
    win_combinations = [
        [(1, 1), (1, 2), (1, 3)],
        [(2, 1), (2, 2), (2, 3)],
        [(3, 1), (3, 2), (3, 3)],

        [(1, 1), (2, 1), (3, 1)],
        [(1, 2), (2, 2), (3, 2)],
        [(1, 3), (2, 3), (3, 3)],

        [(1, 1), (2, 2), (3, 3)],
        [(1, 3), (2, 2), (3, 1)],
    ]

    for win_comb in win_combinations:
        cell_1 = get_cell(field,
                          row_index=win_comb[0][0]-1,
                          col_index=win_comb[0][1]-1)
        cell_2 = get_cell(field,
                          row_index=win_comb[1][0]-1,
                          col_index=win_comb[1][1]-1)
        cell_3 = get_cell(field,
                          row_index=win_comb[2][0]-1,
                          col_index=win_comb[2][1]-1)

        win_condition = cell_1 == cell_2 == cell_3 != EMPTY_CELL
        if win_condition:
            return True

    return False


def is_available_cell(field) -> bool:
    for row in field:
        for cell in row:
            if cell == EMPTY_CELL:
                return True
    return False


def is_empty_cell(field: list, x: int, y: int) -> bool:
    cell = field[x][y]
    return True if cell == EMPTY_CELL else False
