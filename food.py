# В этом файле мы создадим Food класс
# для управления положением и отрисовкой еды на сетке.

# В игре «Змейка» после того, как пищевой блок съеден,
# в случайном месте на сетке появляется еще один.
# Это означает, что нам понадобится генератор случайных чисел,
# чтобы определить местонахождение еды.

import random


# Обратите внимание на общность со Snake классом.
# У них обоих есть draw метод и respawn метод.
# Как правило, в играх большинство объектов имеют эту функциональность.

class Food:
    block_size = None
    color = (0, 0, 255)
    x = 100
    y = 100
    bounds = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds

    def draw(self, game, window):
        game.draw.rect(window, self.color, (self.x, self.y, self.block_size, self.block_size))

    def respawn(self):
        blocks_in_x = (self.bounds[0]) / self.block_size
        blocks_in_y = (self.bounds[1]) / self.block_size
        self.x = random.randint(0, blocks_in_x - 1) * self.block_size
        self.y = random.randint(0, blocks_in_y - 1) * self.block_size
