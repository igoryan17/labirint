def way_exist(labyrinth):
    n = len(labyrinth)
    for i in range(n):
        if labyrinth[i][0] == 0:
            result = check_way(labyrinth, i, 0, i, 0)
            if result:
                return True
    return False


def check_way(labyrinth, current_row, current_column, old_row, old_column):
    up_row = current_row - 1
    n = len(labyrinth)
    result = False
    if up_row >= 0 and not (up_row == old_row and current_column == old_column):
        if labyrinth[up_row][current_column] == 0:
            if current_column == n - 1:
                result = True
            else:
                result = check_way(labyrinth, up_row, current_column, current_row, current_column)
    down_row = current_row + 1
    if not result and down_row <= (n - 1) and not (down_row == old_row and current_column == old_column):
        if labyrinth[down_row][current_column] == 0:
            if current_column == n - 1:
                result = True
            else:
                result = check_way(labyrinth, down_row, current_column, current_row, current_column)
    left_column = current_column - 1
    if not result and left_column >= 0 and not (current_row == old_row and left_column == old_column):
        if labyrinth[current_row][left_column] == 0:
            result = check_way(labyrinth, current_row, left_column, current_row, current_column)
    right_column = current_column + 1
    if not result and right_column <= (n - 1) and not (current_row == old_row and right_column == old_column):
        if labyrinth[current_row][right_column] == 0:
            if right_column == n - 1:
                result = True
            else:
                result = check_way(labyrinth, current_row, right_column, current_row, current_column)
    return result
