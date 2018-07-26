def way_exist(labyrinth, width):
    n = len(labyrinth)
    count = int(n / width)
    entries = set()
    exits = set()
    for i in range(len(labyrinth)):
        if labyrinth[i][0] == 0:
            entries.add(i)
    if count > 0:
        for i in range(count):
            border = {'left_border': i * width,
                      'right_border': (i + 1) * width}
            if i == (count - 1):
                border['right_border'] = len(labyrinth)
            for row in entries:
                check_way(labyrinth, border, {'current_row': row,
                                              'current_column': i * width,
                                              'old_row': row,
                                              'old_column': i * width
                                              }, exits)
                print('iteration number ' + str(i) +
                      ' left border is ' + str(border['left_border']) + ' right border is ' + str(border['right_border']))
                print(exits)
            entries = exits.copy()
            exits.clear()
    return len(entries) > 0


def check_way(labyrinth, border, position, entries):
    up_row = position['current_row'] - 1
    n = len(labyrinth)
    current_row = position['current_row']
    current_column = position['current_column']
    old_row = position['old_row']
    old_column = position['old_column']
    left_border = border['left_border']
    right_border = border['right_border']
    if up_row >= 0 and not (up_row == old_row and current_column == old_column):
        if labyrinth[up_row][current_column] == 0:
            if current_column == right_border - 1:
                entries.add(up_row)
            else:
                print('from [' + str(current_row) + '][' + str(current_column) + ']'
                      + ' to [' + str(up_row) + '][' + str(current_column) + ']')
                labyrinth[current_row][current_column] = 1
                check_way(labyrinth, border, {
                    'current_row': up_row,
                    'current_column': current_column,
                    'old_row': current_row,
                    'old_column': current_column
                }, entries)

    down_row = current_row + 1
    if down_row <= (n - 1) and not (down_row == old_row and current_column == old_column):
        if labyrinth[down_row][current_column] == 0:
            if current_column == n - 1:
                entries.add(down_row)
            else:
                print('from [' + str(current_row) + '][' + str(current_column) + ']'
                      + ' to [' + str(down_row) + '][' + str(current_column) + ']')
                labyrinth[current_row][current_column] = 1
                check_way(labyrinth, border, {
                    'current_row': down_row,
                    'current_column': current_column,
                    'old_row': current_row,
                    'old_column': current_column
                }, entries)

    left_column = current_column - 1
    if left_column >= left_border and not (current_row == old_row and left_column == old_column):
        if labyrinth[current_row][left_column] == 0:
            print('from [' + str(current_row) + '][' + str(current_column) + ']'
                  + ' to [' + str(current_row) + '][' + str(left_column) + ']')
            labyrinth[current_row][current_column] = 1
            check_way(labyrinth, border, {
                'current_row': current_row,
                'current_column': left_column,
                'old_row': old_row,
                'old_column': old_column
            }, entries)

    right_column = current_column + 1
    if right_column <= right_border and not (current_row == old_row and right_column == old_column):
        if labyrinth[current_row][right_column] == 0:
            if right_column == right_border - 1:
                entries.add(current_row)
            else:
                print('from [' + str(current_row) + '][' + str(current_column) + ']'
                      + ' to [' + str(current_row) + '][' + str(right_column) + ']')
                labyrinth[current_row][current_column] = 1
                check_way(labyrinth, border, {
                    'current_row': current_row,
                    'current_column': right_column,
                    'old_row': old_row,
                    'old_column': old_column
                }, entries)
