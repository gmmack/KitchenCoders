import settings
import main
import Block


class Level1(main.pygame.sprite.Sprite):
    def __init__(self):
        super(Level1, self).__init__()
        self.recipeTitle = "Toast"
        # self.next = Level2
        toast = Block.FBlock('Toast', (settings.WINDOWWIDTH / 24, settings.WINDOWHEIGHT / 16), len('toast'), True)
        breadSlice = Block.IBlock('Bread slice', (settings.WINDOWWIDTH / 24, 9*settings.WINDOWHEIGHT / 16), len('bread slice'), True)
        self.functions, self.ingredients = [toast], [breadSlice]
        # self.functions.append(toast)
        # self.ingredients.append(breadSlice)

    # Checks for collision and moves the clicked block
    def handleMouseDown(self, mousePoint, block):
        if block.collide(mousePoint):
            if block.bank:
                # create new instance of function with bank=false
                if block.type == "function":
                    new_block = Block.FBlock(block.text, block.blockRect.center, len(block.text), False)
                    self.functions.append(new_block)
                elif block.type == "ingredient":
                    new_block = Block.IBlock(block.text, block.blockRect.center, len(block.text), False)
                    self.ingredients.append(new_block)
                new_block.setPos(mousePoint)
                new_block.drag = True
            else:  # Need to deal with non-snapped and snapped fcn blocks
                if block.snapped:
                    line_number = block.getLine(block.blockRect.centery)[1]
                    block.index = line_number
                    # Loop through board list finding curr block clicked
                    first, second = False, False
                    for curr in settings.BOARD[line_number]:
                        # TODO: Keep track of state of board[line_number] list to update
                        if curr == block:
                            first = True
                        if second:
                            # Other times:
                            curr.trailBlock(prev)
                        if first:
                            # First Time
                            curr.setPos(mousePoint)
                            curr.drag = True
                            first, second = False, True
                        prev = curr
                    settings.BOARD[line_number] = None
                else:
                    block.setPos(mousePoint)
                    block.drag = True

    # Loops through board seeing if the player has a winning state for the current level
    def checkWin(self):
        pass
        for num in range(1, 16):
            pass
            settings.BOARD[num]

    def draw(self):
        # Draw directions on right side of screen

        # Draw recipe title
        """
        recipeTitleSurf = settings.BACKGROUNDSFONT.render(self.recipeTitle, True, settings.WHITE)
        recipeTitleRect = recipeTitleSurf.get_rect()
        recipeTitleRect.midtop = (5*settings.WINDOWWIDTH/6, settings.WINDOWHEIGHT/16)
        settings.DISPLAYSURF.blit(recipeTitleSurf, recipeTitleRect)"""

        # Draw blocks
        for function in self.functions:
            function.draw(settings.RED)
        for ingredient in self.ingredients:
            ingredient.draw(settings.GREEN)

    # Resets block position to be on top of mouse if dragged
    def updateBlocks(self):
        for function in self.functions:
            if function.drag:
                function.setPos(main.pygame.mouse.get_pos())
        for ingredient in self.ingredients:
            if ingredient.drag:
                ingredient.setPos(main.pygame.mouse.get_pos())
