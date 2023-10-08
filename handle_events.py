import pygame
from constants import Constants
import random


class HandleEvents:
    def __init__(self):
        self.constant = Constants()

    def create_life(self, container):
        pos_x, pos_y = pygame.mouse.get_pos()
        row = pos_x // self.constant.BLOCK_SIZE
        col = pos_y // self.constant.BLOCK_SIZE
        if (row, col) not in container.return_positions():
            container.append_in_position((row, col))
        else:
            container.remove_from_position((row, col))

    def generate_life(self, container):
        random_life = random.randrange(10, 500)
        for i in range(random_life):
            x = random.randrange(0, self.constant.WIDTH)
            y = random.randrange(0, self.constant.HEIGHT)
            row = x // self.constant.BLOCK_SIZE
            col = y // self.constant.BLOCK_SIZE
            if (row, col) not in container.return_positions() and row < self.constant.NET_HEIGHT and col < self.constant.NET_WIDTH:
                container.append_in_position((row, col))

    def get_neighbors(self, pos):
        x, y = pos
        neighbors = []

        for dx in [-1, 0, 1]:
            if x + dx < 0 or x + dx > self.constant.NET_WIDTH:
                continue

            for dy in [-1, 0, 1]:
                if y + dy < 0 or y + dy > self.constant.NET_HEIGHT:
                    continue

                if dx == 0 and dy == 0:
                    continue

                neighbors.append((x + dx, y + dy))

        return list(set(neighbors))

    def rebuild_grid(self, positions):
        all_neighbors = set()
        new_positions = set()

        for position in positions:
            neighbors = self.get_neighbors(position)
            all_neighbors.update(neighbors)
            k = []
            for neighbor in neighbors:
                if neighbor in positions:
                    k.append(neighbor)
            neighbors = set(k.copy())

            if len(neighbors) in (2, 3):
                new_positions.add(position)

        for position in all_neighbors:
            neighbors = self.get_neighbors(position)
            neighbors = list(filter(lambda x: x in positions, neighbors))

            if len(neighbors) == 3:
                new_positions.add(position)
        return new_positions
