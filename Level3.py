import Level
import Level4
import settings
import Block


class Level3(Level.Level):
    def __init__(self):
        super(Level3, self).__init__()
        self.recipeTitle = "Avocado Toast"
        self.solutions = self.create_solution_dicts()
        self.next = Level4.Level4
        bread_slice_str = 'Bread Slice'
        toast_str = 'Toast'
        salt_str = 'Salt'
        pepper_str = 'Pepper'
        oil_str = 'Oil'
        toast = Block.FBlock(toast_str, (settings.WINDOWWIDTH / 24, settings.WINDOWHEIGHT / 16), True,
                             'images/toast.png')
        salt = Block.FBlock(salt_str, (settings.WINDOWWIDTH / 24, 2 * settings.WINDOWHEIGHT / 16),
                              True, 'images/salt.png')
        pepper = Block.FBlock(pepper_str, (settings.WINDOWWIDTH / 24, 3 * settings.WINDOWHEIGHT / 16),
                            True, 'images/pepper.png')
        oil = Block.FBlock(oil_str, (settings.WINDOWWIDTH / 24, 4 * settings.WINDOWHEIGHT / 16),
                            True, 'images/oil.png')
        breadSlice = Block.IBlock(bread_slice_str, (settings.WINDOWWIDTH / 24, 9 * settings.WINDOWHEIGHT / 16),
                                  True, 'images/breadslice.png')
        self.functions, self.ingredients = [toast, salt, pepper, oil], [breadSlice]

    @staticmethod  # TODO: Write real solution
    # SOLUTION: Toast->BreadSlice, Salt->BreadSlice, Pepper->BreadSlice, Oil->BreadSlice
    def create_solution_dicts():
        sol1 = settings.create_blank_dict()
        sol2 = settings.create_blank_dict()
        sol3 = settings.create_blank_dict()
        sol4 = settings.create_blank_dict()
        sol5 = settings.create_blank_dict()
        sol6 = settings.create_blank_dict()
        sol1[1] = ['Toast', 'Bread Slice']
        sol1[2] = ['Salt', 'Bread Slice']
        sol1[3] = ['Pepper', 'Bread Slice']
        sol1[4] = ['Oil', 'Bread Slice']
        sol2[1] = ['Toast', 'Bread Slice']
        sol2[2] = ['Pepper', 'Bread Slice']
        sol2[3] = ['Salt', 'Bread Slice']
        sol2[4] = ['Oil', 'Bread Slice']
        sol3[1] = ['Toast', 'Bread Slice']
        sol3[2] = ['Oil', 'Bread Slice']
        sol3[3] = ['Salt', 'Bread Slice']
        sol3[4] = ['Pepper', 'Bread Slice']
        sol4[1] = ['Toast', 'Bread Slice']
        sol4[2] = ['Oil', 'Bread Slice']
        sol4[3] = ['Pepper', 'Bread Slice']
        sol4[4] = ['Salt', 'Bread Slice']
        sol5[1] = ['Toast', 'Bread Slice']
        sol5[2] = ['Pepper', 'Bread Slice']
        sol5[3] = ['Oil', 'Bread Slice']
        sol5[4] = ['Salt', 'Bread Slice']
        sol6[1] = ['Toast', 'Bread Slice']
        sol6[2] = ['Salt', 'Bread Slice']
        sol6[3] = ['Oil', 'Bread Slice']
        sol6[4] = ['Pepper', 'Bread Slice']
        solution = [sol1, sol2, sol3, sol4, sol5, sol6]
        return solution
