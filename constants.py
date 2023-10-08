class Constants:
    WIDTH = 800
    HEIGHT = 800
    DISPLAY_HEIGHT = 900
    GRAY = (128, 128, 128)
    BLACK = (0, 0, 0)
    GREEN = (154, 178, 71)
    BLOCK_SIZE = 20
    NET_WIDTH = WIDTH // BLOCK_SIZE
    NET_HEIGHT = HEIGHT // BLOCK_SIZE
    FPS = 35
    UPDATE_FREQUENCY = 20


class Containers:
    def __init__(self):
        self.POSITIONS = set()

    def append_in_position(self, position):
        self.POSITIONS.add(position)

    def remove_from_position(self, position):
        if position in self.POSITIONS:
            self.POSITIONS.remove(position)

    def clear_position(self):
        self.POSITIONS.clear()

    def return_positions(self):
        return self.POSITIONS
