import main
import time


class Timer(main.pygame.sprite.Sprite):
    def __init__(self):
        super(Timer, self).__init__()
        self.start = 0

    def set_start(self):
        self.start = time.time()

    def get_elapsed(self):
        return time.time() - self.start

    # Returns true if the elapsed time is greater than or equal to 1 second
    def show_tooltip(self):
        return self.get_elapsed() >= 1
