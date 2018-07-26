import generator
import runnability

labyrinth = [
    [1, 1, 1, 1, 1],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0]
]
generator.print_labyrinth(labyrinth)
print(runnability.way_exist(labyrinth, 2))
