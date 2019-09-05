import sys

import pygame
from pygame.locals import *

from Level1 import *
from settings import *

"""
CURRENTLY UNUSED: SAVE FOR LATER
# Function to display images
_image_library = {}

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image
"""


def main():
    pygame.display.set_caption('Kitchen Coders')
    showStartScreen()
    level = Level1()
    while level != -1:
        runGame(level)  # Will eventually want level = runGame(level)
        # showGameOverScreen()


def runGame(level):
    while True:  # main game loop
        for event in pygame.event.get():  # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                pressed = pygame.key.get_pressed()
                if event.key == K_ESCAPE:
                    terminate()
            elif event.type == MOUSEBUTTONDOWN:  # Mouse clicked down
                if event.button == 1:
                    mousePoint = pygame.mouse.get_pos()
                    for function in level.functions:
                        level.handleMouseDown(mousePoint, function)
                    for ingredient in level.ingredients:
                        level.handleMouseDown(mousePoint, ingredient)
            elif event.type == MOUSEBUTTONUP:  # Mouse click lifted
                if event.button == 1:
                    # Reset to nothing being dragged, and snap blocks together if close
                    for function in level.functions:
                        if function.drag:
                            if function.snap(level.draglist):
                                pass
                            else:
                                function.index = -1
                                function.snapped = False
                        function.drag = False
                    for ingredient in level.ingredients:
                        if ingredient.drag:
                            if ingredient.snap(level.draglist):
                                pass
                            else:
                                ingredient.index = -1
                                ingredient.snapped = False
                        ingredient.drag = False
                    mousePoint = pygame.mouse.get_pos()
                    level.draglist.clear()  # Clear list of blocks being dragged
                    print("BOARD = ", BOARD)
            elif event.type == pygame.MOUSEMOTION:
                level.updateBlocks()
            elif event.type == pygame.VIDEORESIZE:
                settings.WINDOWWIDTH, settings.WINDOWHEIGHT = pygame.display.get_surface().get_size()

        DISPLAYSURF.fill(CYAN)  # Fills background with cyan
        level.draw()

        # DISPLAYSURF.blit(BACKGROUNDIMAGE, [0, 0])
        # DISPLAYSURF.blit(get_image('tile002.png'), (playerX, playerY))

        pygame.display.update()
        FPSCLOCK.tick(FPS)

        # if (level.check_win) -- triggered by button press of "Run Code" button,
        #     return level.next()

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 100)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


# Pause waiting for key press
def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showStartScreen():
    while True:
        DISPLAYSURF.fill(BLACK)
        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get()  # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def drawScore(score):
    scoreSurf = BASICFONT.render('levels: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


if __name__ == '__main__':
    main()

