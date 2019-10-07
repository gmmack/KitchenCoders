import main
import settings


class Debug(main.pygame.sprite.Sprite):
    def __init__(self):
        super(Debug, self).__init__()
        self.debug_on = False
        self.line_number = -1
        # Could also have list of strings with names of blocks from the error line

    # Draws debug info for when player has incorrect code
    def draw_debug(self, size):
        if self.line_number is not -1:
            text1 = "Check line " + str(self.line_number) + " for the error."
            text2 = "Oops! That didn't work."
        else:
            text1 = "you try to run your code!"
            text2 = "Drag some blocks before"
        text_height = settings.BACKGROUNDSFONT.get_height()

        debug1Surf = settings.BACKGROUNDSFONT.render(text1, True, settings.RED)
        debug1Rect = debug1Surf.get_rect()
        debug1Rect.midbottom = (5*settings.WINDOWWIDTH/6, settings.WINDOWHEIGHT - size)
        settings.DISPLAYSURF.blit(debug1Surf, debug1Rect)

        debug2Surf = settings.BACKGROUNDSFONT.render(text2, True, settings.RED)
        debug2Rect = debug2Surf.get_rect()
        debug2Rect.midbottom = (5 * settings.WINDOWWIDTH / 6, settings.WINDOWHEIGHT - size - text_height)
        settings.DISPLAYSURF.blit(debug2Surf, debug2Rect)

