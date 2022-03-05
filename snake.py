from enum import Enum
from typing import List

from consts import *


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Coord:
    x = None
    y = None
    block_size = None

    def __init__(self, x, y, size=BLOCK_SIZE):
        self.x = x
        self.y = y
        self.block_size = size

    def get_coords(self) -> tuple:
        return self.x, self.y, self.block_size, self.block_size


class Snake:
    speed: int = None
    length: int = None
    color: tuple = SNAKE_COLOR
    direction: Direction = None
    block_size: int = None
    # body -- это список Python, содержащий кортежи (или пары) координат.
    # Каждая из этих координат описывает
    # верхние левые x и y положения экрана сегмента тела или блока.
    # Мы будем добавлять (дополнять) этот список по мере роста змеи.
    # Мы также используем этот список при рисовании змеи.
    body: List[Coord] = None
    bounds = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.spawn()

    def spawn(self):
        self.length = 3  # или 4?
        self.body = [Coord(20, 20), Coord(20, 40), Coord(20, 60), Coord(20, 80)]
        self.direction = Direction.RIGHT

    def draw(self, game, window):
        for segment in self.body:
            game.draw.rect(window, self.color, segment.get_coords())

    def move(self):
        current_head = self.body[-1]

        if self.direction == Direction.LEFT:
            next_head = Coord(current_head.x - current_head.block_size, current_head.y)
            self.body.append(next_head)
        elif self.direction == Direction.RIGHT:
            next_head = Coord(current_head.x + current_head.block_size, current_head.y)
            self.body.append(next_head)
        elif self.direction == Direction.UP:
            next_head = Coord(current_head.x, current_head.y - current_head.block_size)
            self.body.append(next_head)
        elif self.direction == Direction.DOWN:
            next_head = Coord(current_head.x, current_head.y + current_head.block_size)
            self.body.append(next_head)

        if self.length < len(self.body):
            self.body.pop(0)

    def steer(self, direction: Direction):
        if self.direction == Direction.DOWN and direction != Direction.UP:
            self.direction = direction
        elif self.direction == Direction.UP and direction != Direction.DOWN:
            self.direction = direction
        elif self.direction == Direction.LEFT and direction != Direction.RIGHT:
            self.direction = direction
        elif self.direction == Direction.RIGHT and direction != Direction.LEFT:
            self.direction = direction

    def check_bounds_collision(self):
        head = self.body[-1]

        if head.x >= self.bounds[0] or head.y >= self.bounds[1]:
            return True

        if head.x < 0 or head.y < 0:
            return True

    # увеличивает допустимую длину змейки.
    # Помните, что это length свойство используется в move методе
    # для определения необходимости удаления хвостового сегмента.
    def eat(self):
        self.length += 1

    # проверяет, находится ли голова змеи над едой
    def check_for_food(self, food):
        head = self.body[-1]
        if head.x == food.x and head.y == food.y:
            food.respawn()
