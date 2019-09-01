import settings
import main
import Block


class Level1(main.pygame.sprite.Sprite):
    def __init__(self):
        super(Level1, self).__init__()
        self.recipeTitle = "Toast"
        self.draglist = []
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
                    position = 0
                    #for curr in settings.BOARD[line_number]:  # TODO: Loop is only iterating once because it's removing the item
                    #for i in range(len(settings.BOARD[line_number])):  #TODO: Need to change still,
                        # Could iterate back to front, keep curr and prev (prev being the later in the list
                        # When curr == block, call prev.setPos(mousePoint), prev.drag = True, then break
                        # Don't worry about calling trailBlock(), can do that in updateBlocks
                        # Keep count of number of iterations, then call pop() that many times
                        # TODO: Add blocks into self.draglist once I've found block being dragged
                        # Loop backwards until curr == block, then add curr to draglist.
                        # Loop from curr until end of BOARD[line_number] appending each item to draglist
                    for i in range(len(settings.BOARD[line_number])-1, -1, -1):
                        curr = settings.BOARD[line_number][i]
                        if curr == block:
                            curr.setPos(mousePoint)
                            curr.drag = True
                            break
                    for j in range(i, len(settings.BOARD[line_number])):  # Loop from found block index until end
                        # removing from BOARD and adding to draglist
                        settings.BOARD[line_number][i].snapped = False
                        self.draglist.append(settings.BOARD[line_number].pop(i))
                    """count = 0
                    for i in range(len(settings.BOARD[line_number]), 0, -1):
                        curr = settings.BOARD[line_number][i-1]
                        if curr == block:
                            prev.setPos(mousePoint)
                            prev.drag = True
                            break
                        else:
                            count+=1
                        prev = curr
                    for i in range(count):
                        settings.BOARD[line_number].pop()
                    
                        curr = settings.BOARD[line_number][i]
                        if curr == block:
                            first = True
                        if second:
                            # Other times:
                            curr.trailBlock(prev)
                            print("In if second 1st, Board = ", settings.BOARD)
                            settings.BOARD[line_number].pop(i)
                            print("In if second 2nd, Board = ", settings.BOARD)
                        elif first:
                            # First Time
                            curr.setPos(mousePoint)
                            curr.drag = True
                            print("In if first 1st, Board = ", settings.BOARD)
                            settings.BOARD[line_number].pop(i)
                            print("In if first 2nd, Board = ", settings.BOARD)
                            first, second = False, True
                        else:
                            position += 1
                        prev = curr
                        """
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
        # Set first block in draglist to be mouse position, and rest of list trail the previous block
        first = True
        for curr_block in self.draglist:
            if first:
                self.draglist[0].setPos(main.pygame.mouse.get_pos())
                first = False
            else:
                curr_block.trailBlock(prev)
                pass
            prev = curr_block
