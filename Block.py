import settings
import main


class Block(main.pygame.sprite.Sprite):
    def __init__(self, text, center, bank, path):
        super(Block, self).__init__()
        self.drag = False
        self.text = text
        self.bank = bank  # Use to keep track of static bank blocks which don't ever move/disappear
        self.snapped = False  # Use to update BOARD state when you pick up a snapped block
        self.path = path
        self.height = int(settings.WINDOWHEIGHT/24)
        # self.blockSurf = main.pygame.Surface((10 * length, 20))
        self.blockSurf = settings.get_image(path).convert_alpha()
        self.blockSurf = main.pygame.transform.scale(self.blockSurf, (self.height*2, self.height))
        self.blockRect = self.blockSurf.get_rect()
        # self.textSurf = settings.BASICFONT.render(text, True, settings.WHITE)
        # self.textRect = self.textSurf.get_rect()
        self.setPos(center)

    # Sets position of block to be centered on point
    def setPos(self, point):
        # self.textRect.center = point
        self.blockRect.center = point

    # Sets self block to be trailing behind block
    def trailBlock(self, block):
        self.blockRect.midleft = block.blockRect.midright
        # self.textRect.center = self.blockRect.center

    def draw(self):
        # main.pygame.draw.rect(settings.DISPLAYSURF, color, self.blockRect)
        # settings.DISPLAYSURF.blit(self.textSurf, self.textRect)
        settings.DISPLAYSURF.blit(self.blockSurf, self.blockRect)

    # Draws a shadow block where the block would appear if it were dropped
    # 7th index used to concatenate 'images/transparent_name.png'
    def draw_shadow(self, center):
        if self.type == 'function':
            block = FBlock(self.text, center, False, self.path[:7] + 'transparent_' + self.path[7:])
        elif self.type == 'ingredient':
            block = IBlock(self.text, center, False, self.path[:7] + 'transparent_' + self.path[7:])
        return block

    # Returns true if point is on the block
    def collide(self, point):
        mouseX, mouseY = point
        blockXMin, blockYMax = self.blockRect.bottomleft
        blockXMax, blockYMin = self.blockRect.topright
        # Compare mouseX and mouseY to blockRect.bottomleft, blockRect.topright
        if blockXMin <= mouseX <= blockXMax and blockYMin <= mouseY <= blockYMax:
            return True
        else:
            return False

    # Returns true if the two blocks overlap at any point
    def overlap(self, block):
        if len(self.text) >= len(block.text):
            rect2 = block.blockRect
            rect1 = self.blockRect
        else:
            rect2 = self.blockRect
            rect1 = block.blockRect
        if (rect1.top <= rect2.top <= rect1.bottom and rect1.left <= rect2.right <= rect1.right) \
                or (rect1.top <= rect2.top <= rect1.bottom and rect1.left <= rect2.left <= rect1.right) \
                or (rect1.top <= rect2.bottom <= rect1.bottom and rect1.left <= rect2.left <= rect1.right) \
                or (rect1.top <= rect2.bottom <= rect1.bottom and rect1.left <= rect2.right <= rect1.right):
            return True
        return False

    @staticmethod  # Returns the middle y-coordinate of the line where the block should snap to, -1 if error
    def getLine(y):
        yCoord = -1
        line_number = -1
        if y < 2 * settings.WINDOWHEIGHT / settings.NUMLINES:
            yCoord = 2 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY
            line_number = 1
        elif y < 3 * settings.WINDOWHEIGHT / settings.NUMLINES:
            yCoord = 3 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY
            line_number = 2
        elif y < 4 * settings.WINDOWHEIGHT / settings.NUMLINES:
            yCoord = 4 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY
            line_number = 3
        elif y < 5 * settings.WINDOWHEIGHT / settings.NUMLINES:
            yCoord = 5 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY
            line_number = 4
        elif y < 6 * settings.WINDOWHEIGHT / settings.NUMLINES:
            yCoord = 6 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY
            line_number = 5
        elif y < 7 * settings.WINDOWHEIGHT / settings.NUMLINES:
            yCoord = 7 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY
            line_number = 6
        elif y < 8 * settings.WINDOWHEIGHT / settings.NUMLINES:
            yCoord = 8 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY
            line_number = 7
        elif y < 9 * settings.WINDOWHEIGHT / settings.NUMLINES:
            yCoord = 9 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY
            line_number = 8
        elif y < 10 * settings.WINDOWHEIGHT / settings.NUMLINES:
            yCoord = 10 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY
            line_number = 9
        elif y < 11 * settings.WINDOWHEIGHT / settings.NUMLINES:
            yCoord = 11 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY
            line_number = 10
        elif y < 12 * settings.WINDOWHEIGHT / settings.NUMLINES:
            yCoord = 12 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY
            line_number = 11
        elif y < 13 * settings.WINDOWHEIGHT / settings.NUMLINES:
            yCoord = 13 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY
            line_number = 12
        elif y < 14 * settings.WINDOWHEIGHT / settings.NUMLINES:
            yCoord = 14 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY
            line_number = 13
        elif y < 15 * settings.WINDOWHEIGHT / settings.NUMLINES:
            yCoord = 15 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY
            line_number = 14
        elif y < 16 * settings.WINDOWHEIGHT / settings.NUMLINES:
            yCoord = 16 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY
            line_number = 15
        return yCoord, line_number


class FBlock(Block):
    def __init__(self, text, center, bank, path):
        super(FBlock, self).__init__(text, center, bank, path)
        self.type = "function"

    # Snaps function block and any trailing blocks into place in whatever line of code they were dropped nearest
    def snap(self, draglist):
        midBlockY = self.blockRect.centery
        yCoord, line_number = self.getLine(midBlockY)
        self.snapped = True
        self.blockRect.midleft = (settings.WINDOWWIDTH / 3 + settings.BUFFER * 2, yCoord)
        settings.BOARD[line_number].append(self)
        if len(draglist) > 1:  # If there's anything else being dragged
            for i in range(1, len(draglist)):
                draglist[i].trailBlock(draglist[i - 1])
                draglist[i].snapped = True
                settings.BOARD[line_number].append(draglist[i])

    # Returns tuple, true if the block will be snapped upon release and center point of shadow
    def snappable(self):
        midBlockY = self.blockRect.centery
        yCoord, line_number = self.getLine(midBlockY)
        if self.blockRect.right > settings.WINDOWWIDTH / 3 and self.blockRect.left < 2 * settings.WINDOWWIDTH / 3:
            midleft_position = (settings.WINDOWWIDTH / 3 + settings.BUFFER * 2, yCoord)
            center_position = (settings.WINDOWWIDTH / 3 + settings.BUFFER * 2 + self.height, yCoord)
            return True, center_position
        return False, -1


class IBlock(Block):
    def __init__(self, text, center, bank, path):
        super(IBlock, self).__init__(text, center, bank, path)
        self.type = "ingredient"

    # Snaps ingredient block and any trailing blocks into place
    def snap(self, draglist):
        midBlockY = self.blockRect.centery
        yCoord, line_number = self.getLine(midBlockY)

        self.blockRect.midleft = settings.BOARD[line_number][-1].blockRect.midright  # gets back of board list
        self.setPos(self.blockRect.center)
        self.snapped = True
        settings.BOARD[line_number].append(self)
        if len(draglist) > 1:  # If there's anything else being dragged
            for i in range(1, len(draglist)):
                draglist[i].trailBlock(draglist[i - 1])
                draglist[i].snapped = True
                settings.BOARD[line_number].append(draglist[i])

    # Returns true if the block will be snapped upon release and center point of shadow
    def snappable(self):
        midBlockY = self.blockRect.centery
        yCoord, line_number = self.getLine(midBlockY)

        # TODO: Make sure the block currently there is something that can be snapped onto
        # If there's anything in the current line and block is within snappable range
        if len(settings.BOARD[line_number]) > 0:
            other_block = settings.BOARD[line_number][-1]

            if self.overlap(other_block):
                center_position = settings.BOARD[line_number][-1].blockRect.midright
                center_position = (center_position[0] + self.height, center_position[1])
                return True, center_position
        return False, -1
