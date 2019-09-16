import Level
import Level3
import settings
import Block


class Level2(Level.Level):
    def __init__(self):
        super(Level2, self).__init__()
        self.recipeTitle = "Buttered Toast"
        bread_slice_str = 'Bread Slice'
        toast_str = 'Toast'
        butter_str = 'Butter'
        self.solution = [[toast_str, bread_slice_str], [butter_str, bread_slice_str]]
        self.draglist = []
        self.next = Level3.Level3
        toast = Block.FBlock(toast_str, (settings.WINDOWWIDTH / 24, settings.WINDOWHEIGHT / 16), len(toast_str), True)
        butter = Block.FBlock(butter_str, (settings.WINDOWWIDTH / 24, 2*settings.WINDOWHEIGHT / 16), len(butter_str), True)
        breadSlice = Block.IBlock('Bread Slice', (settings.WINDOWWIDTH / 24, 9 * settings.WINDOWHEIGHT / 16),
                                  len('Bread Slice'), True)
        self.functions, self.ingredients = [toast, butter], [breadSlice]

    @staticmethod
    def create_solution_dicts():
        sol1 = settings.create_blank_dict()
        sol1[1] = ['Toast', 'Bread Slice']
        sol1[2] = ['Butter', 'Bread Slice']
        solution = [sol1]
        return solution
