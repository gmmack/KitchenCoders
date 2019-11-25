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
        bread_slice_str, avocado_str, olive_oil_str = 'Bread Slice', 'Avocado', 'Olive Oil'
        toast_str, slice_str, spread_str, salt_str, pepper_str = 'Toast', 'Slice', 'Spread', 'Salt', 'Pepper'
        toast = Block.FBlock(toast_str, (settings.WINDOWWIDTH / 24, settings.WINDOWHEIGHT / 16), True,
                             'images/toast.png')
        slice = Block.FBlock(slice_str, (settings.WINDOWWIDTH / 24, 2 * settings.WINDOWHEIGHT / 16), True,
                             'images/slice.png')
        spread = Block.FBlock(spread_str, (settings.WINDOWWIDTH / 24, 3 * settings.WINDOWHEIGHT / 16), True,
                             'images/spread.png')
        salt = Block.FBlock(salt_str, (settings.WINDOWWIDTH / 24, 4 * settings.WINDOWHEIGHT / 16),
                              True, 'images/salt.png')
        pepper = Block.FBlock(pepper_str, (settings.WINDOWWIDTH / 24, 5 * settings.WINDOWHEIGHT / 16),
                            True, 'images/pepper.png')
        breadSlice = Block.IBlock(bread_slice_str, (settings.WINDOWWIDTH / 24, 9 * settings.WINDOWHEIGHT / 16),
                                  True, 'images/breadslice.png')
        avocado = Block.IBlock(avocado_str, (settings.WINDOWWIDTH / 24, 10 * settings.WINDOWHEIGHT / 16),
                                  True, 'images/avocado.png')
        oliveoil = Block.IBlock(olive_oil_str, (settings.WINDOWWIDTH / 24, 11 * settings.WINDOWHEIGHT / 16),
                               True, 'images/oliveoil.png')
        self.functions, self.ingredients = [toast, slice, spread, salt, pepper], [breadSlice, avocado, oliveoil]

    @staticmethod
    # SOLUTION: Toast->BreadSlice, Slice->Avocado, Spread->BreadSlice,Avocado, Salt->BreadSlice, Pepper->BreadSlice,
    # Spread->Bread Slice, Oil
    def create_solution_dicts():
        sol1 = settings.create_blank_dict()
        sol2 = settings.create_blank_dict()
        sol3 = settings.create_blank_dict()
        sol4 = settings.create_blank_dict()

        sol1[1] = ['Toast', 'Bread Slice']
        sol1[2] = ['Slice', 'Avocado']
        sol1[3] = ['Spread', 'Bread Slice', 'Avocado']
        sol1[4] = ['Salt', 'Bread Slice']
        sol1[5] = ['Pepper', 'Bread Slice']
        sol1[6] = ['Spread', 'Bread Slice', 'Oil']

        sol2[1] = ['Toast', 'Bread Slice']
        sol2[2] = ['Slice', 'Avocado']
        sol2[3] = ['Spread', 'Bread Slice', 'Avocado']
        sol2[4] = ['Pepper', 'Bread Slice']
        sol2[5] = ['Salt', 'Bread Slice']
        sol2[6] = ['Spread', 'Bread Slice', 'Oil']

        sol3[1] = ['Slice', 'Avocado']
        sol3[2] = ['Toast', 'Bread Slice']
        sol3[3] = ['Spread', 'Bread Slice', 'Avocado']
        sol3[4] = ['Salt', 'Bread Slice']
        sol3[5] = ['Pepper', 'Bread Slice']
        sol3[6] = ['Spread', 'Bread Slice', 'Oil']

        sol4[1] = ['Slice', 'Avocado']
        sol4[2] = ['Toast', 'Bread Slice']
        sol4[3] = ['Spread', 'Bread Slice', 'Avocado']
        sol4[4] = ['Pepper', 'Bread Slice']
        sol4[5] = ['Salt', 'Bread Slice']
        sol4[6] = ['Spread', 'Bread Slice', 'Oil']

        solution = [sol1, sol2, sol3, sol4]
        return solution
