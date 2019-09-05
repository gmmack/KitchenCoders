import Level
import settings
import Block


class Level1(Level.Level):
    def __init__(self):
        super(Level1, self).__init__()
        self.recipeTitle = "Toast"
        self.draglist = []
        # self.next = Level2
        toast = Block.FBlock('Toast', (settings.WINDOWWIDTH / 24, settings.WINDOWHEIGHT / 16), len('Toast'), True)
        breadSlice = Block.IBlock('Bread Slice', (settings.WINDOWWIDTH / 24, 9 * settings.WINDOWHEIGHT / 16),
                                  len('Bread Slice'), True)
        self.functions, self.ingredients = [toast], [breadSlice]

    # For success: Toast->Bread Slice
    # Create dict of function->ingredients
    def check_win(self):
        function_list = []
        ingredients_list = []
        for line_number in range(len(settings.BOARD)):
            if len(settings.BOARD[line_number]) > 0:  # If there's something in the line
                # Found a line with something, loop through chain
                first = True
                for block in settings.board[line_number]:
                    if first:
                        function = block
                        first = False
                    else:
                        ingredients_list.append(block)
