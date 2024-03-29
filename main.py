import sys

import pygame
from pygame.locals import *

from Level1 import *
from settings import *


def main():
    pygame.display.set_caption('Kitchen Coders')
    showStartScreen()
    level = Level1
    while level != -1:
        level = run_game(level())
        # showGameOverScreen()


def run_game(level):
    running = True
    while running:  # main game loop
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
                        if level.handleMouseDown(mousePoint, function):
                            running = False
                    for ingredient in level.ingredients:
                        if level.handleMouseDown(mousePoint, ingredient):
                            running = False
            elif event.type == MOUSEBUTTONUP:  # Mouse click lifted
                if event.button == 1:
                    # Reset to nothing being dragged, and snap blocks together if close
                    for function in level.functions:
                        if function.drag:
                            if level.recycle.check_position(pygame.mouse.get_pos()):
                                level.functions.remove(function)
                                for block in level.draglist:
                                    if block.type == 'function' and block in level.functions:
                                        level.functions.remove(block)
                                    elif block.type == 'ingredient' and block in level.ingredients:
                                        level.ingredients.remove(block)
                            if function.snappable()[0]:
                                function.snap(level.draglist)
                            else:
                                function.snapped = False
                        function.drag = False
                    for ingredient in level.ingredients:
                        if ingredient.drag:
                            if level.recycle.check_position(pygame.mouse.get_pos()):
                                level.ingredients.remove(ingredient)
                                for block in level.draglist:
                                    if block.type == 'function' and block in level.functions:
                                        level.functions.remove(block)
                                    elif block.type == 'ingredient' and block in level.ingredients:
                                        level.ingredients.remove(block)
                            if ingredient.snappable()[0]:
                                ingredient.snap(level.draglist)
                            else:
                                ingredient.snapped = False
                        ingredient.drag = False
                    mousePoint = pygame.mouse.get_pos()
                    level.draglist.clear()  # Clear list of blocks being dragged
                    print("BOARD = ", BOARD)
            elif event.type == pygame.MOUSEMOTION:
                level.updateBlocks()
                level.timer.set_start()
            elif event.type == pygame.VIDEORESIZE:
                settings.WINDOWWIDTH, settings.WINDOWHEIGHT = pygame.display.get_surface().get_size()

        # Recurring check for tooltips
        # level.update_tooltip()

        level.draw()

        # DISPLAYSURF.blit(BACKGROUNDIMAGE, [0, 0])
        # DISPLAYSURF.blit(get_image('tile002.png'), (playerX, playerY))

        pygame.display.update()
        FPSCLOCK.tick(FPS)

    settings.BOARD = settings.create_blank_dict()
    return level.next


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

