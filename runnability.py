def way_exist(labyrinth):
    n = len(labyrinth)
    for i in range(n):
        if labyrinth[i, 0] == 0:

    return False

def check_way(labyrinth, current_row, current_column, old_row, old_column):
    up_row = current_row - 1
    n = len(labyrinth)
    if up_row >= 0 and not (up_row == old_row and current_column == old_column):
        if labyrinth[up_row][current_column] == 0:
            if current_column == n - 1:
                return True
            check_way(labyrinth, up_row, current_column, current_row, current_column)
    down_row = current_row + 1
    if down_row <= (n -1) and not (down_row == old_row and current_column == old_column):
        if labyrinth[down_row][current_column] == 0:
            if current_column == n - 1:
                return True
            check_way(labyrinth, down_row, current_column, current_row, current_column)
    left_column = current_column - 1
    if left_column >= 0 and not (current_row == old_row and left_column == old_column):
        if labyrinth[current_row][left_column] == 0:
            check_way(labyrinth, current_row, left_column, )