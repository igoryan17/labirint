import random


def generate(n, wall_ratio):
    labyrinth = [[0] * n] * n
    for i in range(int(wall_ratio * n)):
        row = random.randint(0, n - 1)
        column = random.randint(0, n - 1)
        labyrinth[row][column] = 1
    return labyrinth


def print_labyrinth(labyrinth):
    for row in labyrinth:
        for column in row:
            print(column, end=" ")
        print()
