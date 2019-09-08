import settings
import main
import Block


class Level(main.pygame.sprite.Sprite):
    def __init__(self):
        super(Level, self).__init__()
        # TODO: Create cookButton class and instantiate cookButton object as instance variable in level
        size = int(settings.WINDOWWIDTH / 8)
        stove_path, recycle_path = 'images/stove.png', 'images/recycle.png'
        self.cook_img = main.pygame.image.load(stove_path)
        self.cook_img = main.pygame.transform.scale(self.cook_img, (size, size))
        self.cook_top_left = (2*settings.WINDOWWIDTH/3, settings.WINDOWHEIGHT - size)
        self.cook_bot_right = (2*settings.WINDOWWIDTH/3 + size, settings.WINDOWHEIGHT)
        self.recycle_img = main.pygame.image.load(recycle_path)
        self.recycle_img = main.pygame.transform.scale(self.recycle_img, (size, size))
        settings.image_library[stove_path] = self.cook_img
        settings.image_library[recycle_path] = self.recycle_img

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
                    # Loop through board list finding curr block clicked
                    for i in range(len(settings.BOARD[line_number])-1, -1, -1):
                        curr = settings.BOARD[line_number][i]
                        if curr == block:
                            curr.setPos(mousePoint)
                            curr.drag = True
                            index = i+1
                            while index <= len(settings.BOARD[line_number])-1:
                                settings.BOARD[line_number][index].trailBlock(settings.BOARD[line_number][index-1])
                                index += 1
                            break
                    for j in range(i, len(settings.BOARD[line_number])):  # Loop from found block index until end
                        settings.BOARD[line_number][i].snapped = False
                        self.draglist.append(settings.BOARD[line_number].pop(i))
                else:
                    block.setPos(mousePoint)
                    block.drag = True
        elif self.cook_pressed(mousePoint):
            self.check_win()
            return True
        return False

    # Returns true if the cook button was pressed
    def cook_pressed(self, point):
        if self.cook_bot_right[0] > point[0] > self.cook_top_left[0] and \
                self.cook_top_left[1] < point[1] < self.cook_bot_right[1]:
            return True
        return False

    def draw(self):
        # Draw directions on right side of screen

        # Draw recipe title
        """
        recipeTitleSurf = settings.BACKGROUNDSFONT.render(self.recipeTitle, True, settings.WHITE)
        recipeTitleRect = recipeTitleSurf.get_rect()
        recipeTitleRect.midtop = (5*settings.WINDOWWIDTH/6, settings.WINDOWHEIGHT/16)
        settings.DISPLAYSURF.blit(recipeTitleSurf, recipeTitleRect)"""

        self.drawBackground()

        # Draw blocks
        for function in self.functions:
            function.draw(settings.RED)
        for ingredient in self.ingredients:
            ingredient.draw(settings.GREEN)

    # Draws background info
    def drawBackground(self):
        # create font
        backgroundsFont = main.pygame.font.Font('freesansbold.ttf', 34)

        # Draw recycle/cook sprites
        x_two_thirds = 2*settings.WINDOWWIDTH/3
        x_offset_by_size = settings.WINDOWWIDTH - settings.WINDOWWIDTH / 8
        y_offset_by_size = settings.WINDOWHEIGHT - settings.WINDOWWIDTH / 8
        settings.DISPLAYSURF.blit(self.recycle_img, (x_offset_by_size, y_offset_by_size))
        #settings.DISPLAYSURF.blit(self.cook_img, (x_two_thirds, y_offset_by_size))
        settings.DISPLAYSURF.blit(self.cook_img, self.cook_top_left)

        gridcolor = settings.PINK
        gridlength = 3

        # draw grid lines
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, 0), (settings.WINDOWWIDTH / 3, settings.WINDOWHEIGHT), 5)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (2 * settings.WINDOWWIDTH / 3, 0), (2 * settings.WINDOWWIDTH / 3, settings.WINDOWHEIGHT), 5)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (0, settings.WINDOWHEIGHT / 2), (settings.WINDOWWIDTH / 3, settings.WINDOWHEIGHT / 2), 5)
        # draws line in left column
        # pygame.draw.line(DISPLAYSURF, gridcolor, (2 * settings.WINDOWWIDTH / 3, settings.WINDOWHEIGHT / 4), (settings.WINDOWWIDTH, settings.WINDOWHEIGHT / 4), 5)

        # draw programming grid lines
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, settings.WINDOWHEIGHT / settings.NUMLINES),
                         (2 * settings.WINDOWWIDTH / 3, settings.WINDOWHEIGHT / 16), gridlength)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, 2 * settings.WINDOWHEIGHT / settings.NUMLINES),
                         (2 * settings.WINDOWWIDTH / 3, 2 * settings.WINDOWHEIGHT / settings.NUMLINES), gridlength)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, 3 * settings.WINDOWHEIGHT / settings.NUMLINES),
                         (2 * settings.WINDOWWIDTH / 3, 3 * settings.WINDOWHEIGHT / settings.NUMLINES), gridlength)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, 4 * settings.WINDOWHEIGHT / settings.NUMLINES),
                         (2 * settings.WINDOWWIDTH / 3, 4 * settings.WINDOWHEIGHT / settings.NUMLINES), gridlength)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, 5 * settings.WINDOWHEIGHT / settings.NUMLINES),
                         (2 * settings.WINDOWWIDTH / 3, 5 * settings.WINDOWHEIGHT / settings.NUMLINES), gridlength)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, 6 * settings.WINDOWHEIGHT / settings.NUMLINES),
                         (2 * settings.WINDOWWIDTH / 3, 6 * settings.WINDOWHEIGHT / settings.NUMLINES), gridlength)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, 7 * settings.WINDOWHEIGHT / settings.NUMLINES),
                         (2 * settings.WINDOWWIDTH / 3, 7 * settings.WINDOWHEIGHT / settings.NUMLINES), gridlength)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, 8 * settings.WINDOWHEIGHT / settings.NUMLINES),
                         (2 * settings.WINDOWWIDTH / 3, 8 * settings.WINDOWHEIGHT / settings.NUMLINES), gridlength)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, 9 * settings.WINDOWHEIGHT / settings.NUMLINES),
                         (2 * settings.WINDOWWIDTH / 3, 9 * settings.WINDOWHEIGHT / settings.NUMLINES), gridlength)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, 10 * settings.WINDOWHEIGHT / settings.NUMLINES),
                         (2 * settings.WINDOWWIDTH / 3, 10 * settings.WINDOWHEIGHT / settings.NUMLINES), gridlength)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, 11 * settings.WINDOWHEIGHT / settings.NUMLINES),
                         (2 * settings.WINDOWWIDTH / 3, 11 * settings.WINDOWHEIGHT / settings.NUMLINES), gridlength)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, 12 * settings.WINDOWHEIGHT / settings.NUMLINES),
                         (2 * settings.WINDOWWIDTH / 3, 12 * settings.WINDOWHEIGHT / settings.NUMLINES), gridlength)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, 13 * settings.WINDOWHEIGHT / settings.NUMLINES),
                         (2 * settings.WINDOWWIDTH / 3, 13 * settings.WINDOWHEIGHT / settings.NUMLINES), gridlength)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, 14 * settings.WINDOWHEIGHT / settings.NUMLINES),
                         (2 * settings.WINDOWWIDTH / 3, 14 * settings.WINDOWHEIGHT / settings.NUMLINES), gridlength)
        main.pygame.draw.line(settings.DISPLAYSURF, gridcolor, (settings.WINDOWWIDTH / 3, 15 * settings.WINDOWHEIGHT / settings.NUMLINES),
                         (2 * settings.WINDOWWIDTH / 3, 15 * settings.WINDOWHEIGHT / settings.NUMLINES), gridlength)

        # draw line numbers
        lineColor = settings.WHITE

        oneSurf = backgroundsFont.render('1', True, lineColor)
        oneRect = oneSurf.get_rect()
        oneRect.center = (settings.WINDOWWIDTH / 3 + settings.BUFFER, 2 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY)
        settings.DISPLAYSURF.blit(oneSurf, oneRect)

        twoSurf = backgroundsFont.render('2', True, lineColor)
        twoRect = twoSurf.get_rect()
        twoRect.center = (settings.WINDOWWIDTH / 3 + settings.BUFFER, 3 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY)
        settings.DISPLAYSURF.blit(twoSurf, twoRect)

        threeSurf = backgroundsFont.render('3', True, lineColor)
        threeRect = threeSurf.get_rect()
        threeRect.center = (settings.WINDOWWIDTH / 3 + settings.BUFFER, 4 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY)
        settings.DISPLAYSURF.blit(threeSurf, threeRect)

        fourSurf = backgroundsFont.render('4', True, lineColor)
        fourRect = fourSurf.get_rect()
        fourRect.center = (settings.WINDOWWIDTH / 3 + settings.BUFFER, 5 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY)
        settings.DISPLAYSURF.blit(fourSurf, fourRect)

        fiveSurf = backgroundsFont.render('5', True, lineColor)
        fiveRect = fiveSurf.get_rect()
        fiveRect.center = (settings.WINDOWWIDTH / 3 + settings.BUFFER, 6 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY)
        settings.DISPLAYSURF.blit(fiveSurf, fiveRect)

        sixSurf = backgroundsFont.render('6', True, lineColor)
        sixRect = sixSurf.get_rect()
        sixRect.center = (settings.WINDOWWIDTH / 3 + settings.BUFFER, 7 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY)
        settings.DISPLAYSURF.blit(sixSurf, sixRect)

        sevenSurf = backgroundsFont.render('7', True, lineColor)
        sevenRect = sevenSurf.get_rect()
        sevenRect.center = (settings.WINDOWWIDTH / 3 + settings.BUFFER, 8 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY)
        settings.DISPLAYSURF.blit(sevenSurf, sevenRect)

        eightSurf = backgroundsFont.render('8', True, lineColor)
        eightRect = eightSurf.get_rect()
        eightRect.center = (settings.WINDOWWIDTH / 3 + settings.BUFFER, 9 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY)
        settings.DISPLAYSURF.blit(eightSurf, eightRect)

        nineSurf = backgroundsFont.render('9', True, lineColor)
        nineRect = nineSurf.get_rect()
        nineRect.center = (settings.WINDOWWIDTH / 3 + settings.BUFFER, 10 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY)
        settings.DISPLAYSURF.blit(nineSurf, nineRect)

        tenSurf = backgroundsFont.render('10', True, lineColor)
        tenRect = tenSurf.get_rect()
        tenRect.center = (settings.WINDOWWIDTH / 3 + settings.BUFFER, 11 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY)
        settings.DISPLAYSURF.blit(tenSurf, tenRect)

        elevenSurf = backgroundsFont.render('11', True, lineColor)
        elevenRect = elevenSurf.get_rect()
        elevenRect.center = (settings.WINDOWWIDTH / 3 + settings.BUFFER, 12 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY)
        settings.DISPLAYSURF.blit(elevenSurf, elevenRect)

        twelveSurf = backgroundsFont.render('12', True, lineColor)
        twelveRect = twelveSurf.get_rect()
        twelveRect.center = (settings.WINDOWWIDTH / 3 + settings.BUFFER, 13 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY)
        settings.DISPLAYSURF.blit(twelveSurf, twelveRect)

        thirteenSurf = backgroundsFont.render('13', True, lineColor)
        thirteenRect = thirteenSurf.get_rect()
        thirteenRect.center = (settings.WINDOWWIDTH / 3 + settings.BUFFER, 14 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY)
        settings.DISPLAYSURF.blit(thirteenSurf, thirteenRect)

        fourteenSurf = backgroundsFont.render('14', True, lineColor)
        fourteenRect = fourteenSurf.get_rect()
        fourteenRect.center = (settings.WINDOWWIDTH / 3 + settings.BUFFER, 15 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY)
        settings.DISPLAYSURF.blit(fourteenSurf, fourteenRect)

        fifteenSurf = backgroundsFont.render('15', True, lineColor)
        fifteenRect = fifteenSurf.get_rect()
        fifteenRect.center = (settings.WINDOWWIDTH / 3 + settings.BUFFER, 16 * settings.WINDOWHEIGHT / settings.NUMLINES - settings.HALFWAY)
        settings.DISPLAYSURF.blit(fifteenSurf, fifteenRect)

        # draw words
        functionsSurf = backgroundsFont.render('Functions', True, settings.WHITE)
        functionsRect = functionsSurf.get_rect()
        functionsRect.midtop = (settings.WINDOWWIDTH / 6, settings.WINDOWHEIGHT / 100)
        settings.DISPLAYSURF.blit(functionsSurf, functionsRect)

        ingredientsSurf = backgroundsFont.render('Ingredients', True, settings.WHITE)
        ingredientsRect = ingredientsSurf.get_rect()
        ingredientsRect.midtop = (settings.WINDOWWIDTH / 6, settings.WINDOWHEIGHT / 2 + 2)
        settings.DISPLAYSURF.blit(ingredientsSurf, ingredientsRect)

        recipesSurf = backgroundsFont.render('Recipe', True, settings.WHITE)
        recipesRect = recipesSurf.get_rect()
        recipesRect.midtop = (settings.WINDOWWIDTH / 2, settings.WINDOWHEIGHT / 100)
        settings.DISPLAYSURF.blit(recipesSurf, recipesRect)

        titleSurf = backgroundsFont.render(self.recipeTitle, True,
                                           settings.WHITE)  # TODO: Will eventually want to change this to level.name instead of Directions
        titleRect = titleSurf.get_rect()
        titleRect.midtop = (5 * settings.WINDOWWIDTH / 6, settings.WINDOWHEIGHT / 16)
        settings.DISPLAYSURF.blit(titleSurf, titleRect)

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