from constants import Constants
import pygame


class DrawGrid:
    def __init__(self):
        self.constant = Constants()

    def draw_grid(self, screen, positions=None):
        if positions:
            for position in positions:
                col, row = position
                top_left = (col * self.constant.BLOCK_SIZE,
                            row * self.constant.BLOCK_SIZE)
                bottom_right = (self.constant.BLOCK_SIZE,
                                self.constant.BLOCK_SIZE)
                pygame.draw.rect(screen, self.constant.GREEN,
                                 (*top_left, *bottom_right))

        for row in range(self.constant.NET_HEIGHT + 2):
            pygame.draw.line(screen, self.constant.BLACK, (0, row * self.constant.BLOCK_SIZE),
                             (self.constant.WIDTH + self.constant.BLOCK_SIZE, row * self.constant.BLOCK_SIZE))

        for col in range(self.constant.NET_WIDTH + 2):
            pygame.draw.line(screen, self.constant.BLACK, (col * self.constant.BLOCK_SIZE,
                             0), (col * self.constant.BLOCK_SIZE, self.constant.HEIGHT + self.constant.BLOCK_SIZE))
