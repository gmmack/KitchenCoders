import main
import settings


class Debug(main.pygame.sprite.Sprite):
    def __init__(self):
        super(Debug, self).__init__()
        self.debug_on = False
        self.line_number = -1
        # Could also have list of strings with names of blocks from the error line

    # Draws debug info for when player has incorrect code
    def draw_debug(self):
        text = "Oops! Looks like that didn't quite work.\n Check line " + self.line_number + " for the error."
        debugSurf = settings.BACKGROUNDSFONT.render(text, True, settings.WHITE)
        debugRect = debugSurf.get_rect()
        debugRect.midtop = (0, 0)  # TODO: Need to figure out position
        settings.DISPLAYSURF.blit(debugSurf, debugRect)

