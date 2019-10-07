import main
import settings


class Tooltip(main.pygame.sprite.Sprite):
    def __init__(self, path):
        super(Tooltip, self).__init__()
        size = 0
        self.image = settings.get_image(path).convert_alpha()
        self.image = main.pygame.transform.scale(self.image, (size, size))
        self.image_rect = self.image.get_rect()

    def draw(self):
        settings.DISPLAYSURF.blit(self.image, self.image_rect)
