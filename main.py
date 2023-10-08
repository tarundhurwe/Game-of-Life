import pygame
import random
from constants import Constants, Containers
from grid import DrawGrid
from handle_events import HandleEvents


class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Conway's game of life simulation")
        self.constant = Constants()
        self.grid = DrawGrid()
        self.handle_events = HandleEvents()
        self.container = Containers()
        self.screen = pygame.display.set_mode(
            (self.constant.WIDTH + 20, self.constant.HEIGHT + 20))
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False
        self.count = 0

    def start_game_of_life(self):
        try:
            while self.running:
                if self.playing:
                    self.count += 1

                if self.count >= self.constant.UPDATE_FREQUENCY:
                    self.count = 0
                    self.container.POSITIONS = self.handle_events.rebuild_grid(
                        self.container.return_positions())

                self.clock.tick(self.constant.FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.handle_events.create_life(self.container)

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_g:
                            self.container.clear_position()
                            self.handle_events.generate_life(self.container)

                        elif event.key == pygame.K_c:
                            self.container.clear_position()

                        elif event.key == pygame.K_SPACE:
                            self.playing = not self.playing
                            pygame.display.set_caption(
                                f"Conway's game of life simulation : {'Playing' if self.playing else 'Paused'}")
                        elif event.key == pygame.K_q:
                            self.running = False

                self.screen.fill(self.constant.GRAY)
                self.grid.draw_grid(screen=self.screen,
                                    positions=self.container.return_positions())
                pygame.display.update()
            pygame.quit()
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    game = Main()
    game.start_game_of_life()
