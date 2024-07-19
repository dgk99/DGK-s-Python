import random

# 색상
RED = ((255, 0, 0))
BLACK = ((0, 0, 0))
YELLOW = ((255, 255, 0))
GREEN = ((0, 255, 0))
BLUE = ((0, 0, 255))
color_list = [RED, BLACK, YELLOW, GREEN, BLUE]
rand_color = random.randint(0, 4)
print(color_list[rand_color])

