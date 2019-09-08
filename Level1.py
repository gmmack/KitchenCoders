import Level
import Level2
import settings
import Block


class Level1(Level.Level):
    def __init__(self):
        super(Level1, self).__init__()
        self.recipeTitle = "Toast"
        self.solution = [['Toast', 'Bread Slice']]
        self.draglist = []
        self.next = Level2.Level2
        toast = Block.FBlock('Toast', (settings.WINDOWWIDTH / 24, settings.WINDOWHEIGHT / 16), len('Toast'), True)
        breadSlice = Block.IBlock('Bread Slice', (settings.WINDOWWIDTH / 24, 9 * settings.WINDOWHEIGHT / 16),
                                  len('Bread Slice'), True)
        self.functions, self.ingredients = [toast], [breadSlice]

    # For success: Toast->Bread Slice
    # Returns true if BOARD is in a winning state
    def check_win(self):
        first_index = 0
        all_good = False
        for line_number in range(1, settings.NUMLINES):  # Loop through lines
            if len(settings.BOARD[line_number]) > 0:  # If there's something in the line
                second_index = 0
                for item in settings.BOARD[line_number]:  # Loop through current line
                    if item.text == self.solution[first_index][second_index]:  # If item matches solution
                        all_good = True
                    else:
                        all_good = False
                    second_index += 1
                second_index += 1
                """if not all_good: # Could use for early exit 
                    return all_good"""
        return all_good
