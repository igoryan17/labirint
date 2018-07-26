import generator
import runnability

labyrinth = generator.generate(10, 0.75)
generator.print_labyrinth(labyrinth)
print(runnability.way_exist(labyrinth))