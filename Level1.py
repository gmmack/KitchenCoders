import Level
import settings
import Block


class Level1(Level.Level):
    def __init__(self):
        super(Level1, self).__init__()
        self.recipeTitle = "Toast"
        self.draglist = []
        # self.next = Level2
        toast = Block.FBlock('Toast', (settings.WINDOWWIDTH / 24, settings.WINDOWHEIGHT / 16), len('toast'), True)
        breadSlice = Block.IBlock('Bread slice', (settings.WINDOWWIDTH / 24, 9 * settings.WINDOWHEIGHT / 16),
                                  len('bread slice'), True)
        self.functions, self.ingredients = [toast], [breadSlice]