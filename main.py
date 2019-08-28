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
                            if function.snap():
                                line_number = function.getLine(function.blockRect.centery)[1]
                                BOARD[line_number] = [function]
                        function.drag = False
                    for ingredient in level.ingredients:
                        if ingredient.drag:
                            ingredient.snap()
                            line_number = function.getLine(function.blockRect.centery)[1]
                            BOARD[line_number].append(ingredient)
                        ingredient.drag = False
                    mousePoint = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEMOTION:
                level.updateBlocks()

        DISPLAYSURF.fill(CYAN)  # Fills background with cyan
        drawBackground()
        level.draw()

        # DISPLAYSURF.blit(BACKGROUNDIMAGE, [0, 0])
        # DISPLAYSURF.blit(get_image('tile002.png'), (playerX, playerY))

        pygame.display.update()
        FPSCLOCK.tick(FPS)

        # if (level.checkWin) -- triggered by button press of "Run Code" button,
        #     return level.next()


# Draws background info TODO: Should go in Level class
def drawBackground():
    # create font
    backgroundsFont = pygame.font.Font('freesansbold.ttf', 34)

    gridcolor = PINK
    gridlength = 3

    # draw grid lines
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, 0), (WINDOWWIDTH / 3, WINDOWHEIGHT), 5)
    pygame.draw.line(DISPLAYSURF, gridcolor, (2 * WINDOWWIDTH / 3, 0), (2 * WINDOWWIDTH / 3, WINDOWHEIGHT), 5)
    pygame.draw.line(DISPLAYSURF, gridcolor, (0, WINDOWHEIGHT / 2), (WINDOWWIDTH / 3, WINDOWHEIGHT / 2), 5)
    # draws line in left column
    #pygame.draw.line(DISPLAYSURF, gridcolor, (2 * WINDOWWIDTH / 3, WINDOWHEIGHT / 4), (WINDOWWIDTH, WINDOWHEIGHT / 4), 5)

    # draw programming grid lines
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, WINDOWHEIGHT / NUMLINES),
                     (2 * WINDOWWIDTH / 3, WINDOWHEIGHT / 16), gridlength)
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, 2 * WINDOWHEIGHT / NUMLINES),
                     (2 * WINDOWWIDTH / 3, 2 * WINDOWHEIGHT / NUMLINES), gridlength)
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, 3 * WINDOWHEIGHT / NUMLINES),
                     (2 * WINDOWWIDTH / 3, 3 * WINDOWHEIGHT / NUMLINES), gridlength)
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, 4 * WINDOWHEIGHT / NUMLINES),
                     (2 * WINDOWWIDTH / 3, 4 * WINDOWHEIGHT / NUMLINES), gridlength)
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, 5 * WINDOWHEIGHT / NUMLINES),
                     (2 * WINDOWWIDTH / 3, 5 * WINDOWHEIGHT / NUMLINES), gridlength)
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, 6 * WINDOWHEIGHT / NUMLINES),
                     (2 * WINDOWWIDTH / 3, 6 * WINDOWHEIGHT / NUMLINES), gridlength)
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, 7 * WINDOWHEIGHT / NUMLINES),
                     (2 * WINDOWWIDTH / 3, 7 * WINDOWHEIGHT / NUMLINES), gridlength)
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, 8 * WINDOWHEIGHT / NUMLINES),
                     (2 * WINDOWWIDTH / 3, 8 * WINDOWHEIGHT / NUMLINES), gridlength)
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, 9 * WINDOWHEIGHT / NUMLINES),
                     (2 * WINDOWWIDTH / 3, 9 * WINDOWHEIGHT / NUMLINES), gridlength)
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, 10 * WINDOWHEIGHT / NUMLINES),
                     (2 * WINDOWWIDTH / 3, 10 * WINDOWHEIGHT / NUMLINES), gridlength)
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, 11 * WINDOWHEIGHT / NUMLINES),
                     (2 * WINDOWWIDTH / 3, 11 * WINDOWHEIGHT / NUMLINES), gridlength)
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, 12 * WINDOWHEIGHT / NUMLINES),
                     (2 * WINDOWWIDTH / 3, 12 * WINDOWHEIGHT / NUMLINES), gridlength)
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, 13 * WINDOWHEIGHT / NUMLINES),
                     (2 * WINDOWWIDTH / 3, 13 * WINDOWHEIGHT / NUMLINES), gridlength)
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, 14 * WINDOWHEIGHT / NUMLINES),
                     (2 * WINDOWWIDTH / 3, 14 * WINDOWHEIGHT / NUMLINES), gridlength)
    pygame.draw.line(DISPLAYSURF, gridcolor, (WINDOWWIDTH / 3, 15 * WINDOWHEIGHT / NUMLINES),
                     (2 * WINDOWWIDTH / 3, 15 * WINDOWHEIGHT / NUMLINES), gridlength)

    # draw line numbers
    lineColor = WHITE

    oneSurf = backgroundsFont.render('1', True, lineColor)
    oneRect = oneSurf.get_rect()
    oneRect.center = (WINDOWWIDTH / 3 + BUFFER, 2 * WINDOWHEIGHT / NUMLINES - HALFWAY)
    DISPLAYSURF.blit(oneSurf, oneRect)

    twoSurf = backgroundsFont.render('2', True, lineColor)
    twoRect = twoSurf.get_rect()
    twoRect.center = (WINDOWWIDTH / 3 + BUFFER, 3 * WINDOWHEIGHT / NUMLINES - HALFWAY)
    DISPLAYSURF.blit(twoSurf, twoRect)

    threeSurf = backgroundsFont.render('3', True, lineColor)
    threeRect = threeSurf.get_rect()
    threeRect.center = (WINDOWWIDTH / 3 + BUFFER, 4 * WINDOWHEIGHT / NUMLINES - HALFWAY)
    DISPLAYSURF.blit(threeSurf, threeRect)

    fourSurf = backgroundsFont.render('4', True, lineColor)
    fourRect = fourSurf.get_rect()
    fourRect.center = (WINDOWWIDTH / 3 + BUFFER, 5 * WINDOWHEIGHT / NUMLINES - HALFWAY)
    DISPLAYSURF.blit(fourSurf, fourRect)

    fiveSurf = backgroundsFont.render('5', True, lineColor)
    fiveRect = fiveSurf.get_rect()
    fiveRect.center = (WINDOWWIDTH / 3 + BUFFER, 6 * WINDOWHEIGHT / NUMLINES - HALFWAY)
    DISPLAYSURF.blit(fiveSurf, fiveRect)

    sixSurf = backgroundsFont.render('6', True, lineColor)
    sixRect = sixSurf.get_rect()
    sixRect.center = (WINDOWWIDTH / 3 + BUFFER, 7 * WINDOWHEIGHT / NUMLINES - HALFWAY)
    DISPLAYSURF.blit(sixSurf, sixRect)

    sevenSurf = backgroundsFont.render('7', True, lineColor)
    sevenRect = sevenSurf.get_rect()
    sevenRect.center = (WINDOWWIDTH / 3 + BUFFER, 8 * WINDOWHEIGHT / NUMLINES - HALFWAY)
    DISPLAYSURF.blit(sevenSurf, sevenRect)

    eightSurf = backgroundsFont.render('8', True, lineColor)
    eightRect = eightSurf.get_rect()
    eightRect.center = (WINDOWWIDTH / 3 + BUFFER, 9 * WINDOWHEIGHT / NUMLINES - HALFWAY)
    DISPLAYSURF.blit(eightSurf, eightRect)

    nineSurf = backgroundsFont.render('9', True, lineColor)
    nineRect = nineSurf.get_rect()
    nineRect.center = (WINDOWWIDTH / 3 + BUFFER, 10 * WINDOWHEIGHT / NUMLINES - HALFWAY)
    DISPLAYSURF.blit(nineSurf, nineRect)

    tenSurf = backgroundsFont.render('10', True, lineColor)
    tenRect = tenSurf.get_rect()
    tenRect.center = (WINDOWWIDTH / 3 + BUFFER, 11 * WINDOWHEIGHT / NUMLINES - HALFWAY)
    DISPLAYSURF.blit(tenSurf, tenRect)

    elevenSurf = backgroundsFont.render('11', True, lineColor)
    elevenRect = elevenSurf.get_rect()
    elevenRect.center = (WINDOWWIDTH / 3 + BUFFER, 12 * WINDOWHEIGHT / NUMLINES - HALFWAY)
    DISPLAYSURF.blit(elevenSurf, elevenRect)

    twelveSurf = backgroundsFont.render('12', True, lineColor)
    twelveRect = twelveSurf.get_rect()
    twelveRect.center = (WINDOWWIDTH / 3 + BUFFER, 13 * WINDOWHEIGHT / NUMLINES - HALFWAY)
    DISPLAYSURF.blit(twelveSurf, twelveRect)

    thirteenSurf = backgroundsFont.render('13', True, lineColor)
    thirteenRect = thirteenSurf.get_rect()
    thirteenRect.center = (WINDOWWIDTH / 3 + BUFFER, 14 * WINDOWHEIGHT / NUMLINES - HALFWAY)
    DISPLAYSURF.blit(thirteenSurf, thirteenRect)

    fourteenSurf = backgroundsFont.render('14', True, lineColor)
    fourteenRect = fourteenSurf.get_rect()
    fourteenRect.center = (WINDOWWIDTH / 3 + BUFFER, 15 * WINDOWHEIGHT / NUMLINES - HALFWAY)
    DISPLAYSURF.blit(fourteenSurf, fourteenRect)

    fifteenSurf = backgroundsFont.render('15', True, lineColor)
    fifteenRect = fifteenSurf.get_rect()
    fifteenRect.center = (WINDOWWIDTH / 3 + BUFFER, 16 * WINDOWHEIGHT / NUMLINES - HALFWAY)
    DISPLAYSURF.blit(fifteenSurf, fifteenRect)

    # draw words
    functionsSurf = backgroundsFont.render('Functions', True, WHITE)
    functionsRect = functionsSurf.get_rect()
    functionsRect.midtop = (WINDOWWIDTH / 6, WINDOWHEIGHT / 100)
    DISPLAYSURF.blit(functionsSurf, functionsRect)

    ingredientsSurf = backgroundsFont.render('Ingredients', True, WHITE)
    ingredientsRect = ingredientsSurf.get_rect()
    ingredientsRect.midtop = (WINDOWWIDTH / 6, WINDOWHEIGHT / 2 + 2)
    DISPLAYSURF.blit(ingredientsSurf, ingredientsRect)

    recipesSurf = backgroundsFont.render('Recipe', True, WHITE)
    recipesRect = recipesSurf.get_rect()
    recipesRect.midtop = (WINDOWWIDTH / 2, WINDOWHEIGHT / 100)
    DISPLAYSURF.blit(recipesSurf, recipesRect)

    titleSurf = backgroundsFont.render('Toast', True, WHITE)  # TODO: Will eventually want to change this to level.name instead of Directions
    titleRect = titleSurf.get_rect()
    titleRect.midtop = (5 * WINDOWWIDTH / 6, WINDOWHEIGHT / 16)
    DISPLAYSURF.blit(titleSurf, titleRect)




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

