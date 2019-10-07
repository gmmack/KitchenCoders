import main
import settings


class CookButton(main.pygame.sprite.Sprite):
    def __init__(self, size):
        super(CookButton, self).__init__()
        self.size = size
        image_path = 'images/stove.png'
        self.image = settings.get_image(image_path).convert_alpha()
        self.image = main.pygame.transform.scale(self.image, (size, size))
        self.image_rect = self.image.get_rect()
        self.image_rect.topleft = (2 * settings.WINDOWWIDTH / 3, settings.WINDOWHEIGHT - size)

    def draw(self):
        settings.DISPLAYSURF.blit(self.image, self.image_rect)

    # Returns true if the cook button was pressed
    def button_pressed(self, point):
        if self.image_rect.bottomright[0] > point[0] > self.image_rect.topleft[0] and \
                self.image_rect.topleft[1] < point[1] < self.image_rect.bottomright[1]:
            return True
        return False
