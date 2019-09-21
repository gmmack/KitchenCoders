import main
import settings


class Recycle(main.pygame.sprite.Sprite):
    def __init__(self, size):
        super(Recycle, self).__init__()
        self.size = size
        image_path = 'images/recycle.png'
        #self.image = main.pygame.image.load(image_path).convert_alpha()
        self.image = settings.get_image(image_path).convert_alpha()
        self.image = main.pygame.transform.scale(self.image, (size, size))
        self.image_rect = self.image.get_rect()
        self.image_rect.bottomright = (settings.WINDOWWIDTH, settings.WINDOWHEIGHT)

    def draw(self):
        settings.DISPLAYSURF.blit(self.image, self.image_rect)

