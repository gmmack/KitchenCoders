import Level
import Level2
import settings
import Block


class Level1(Level.Level):
    def __init__(self):
        super(Level1, self).__init__()
        self.recipeTitle = "Toast"
        self.solutions = self.create_solution_dicts()
        # self.solution = [['Toast', 'Bread Slice']]
        self.draglist = []
        self.next = Level2.Level2
        toast = Block.FBlock('Toast', (settings.WINDOWWIDTH / 24, settings.WINDOWHEIGHT / 16), len('Toast'), True)
        breadSlice = Block.IBlock('Bread Slice', (settings.WINDOWWIDTH / 24, 9 * settings.WINDOWHEIGHT / 16),
                                  len('Bread Slice'), True)
        self.functions, self.ingredients = [toast], [breadSlice]

    # For success: Toast->Bread Slice
    # Returns true if BOARD is in a winning state
    """def check_win(self):
        first_index = 0
        all_good = False
        for line_number in range(1, settings.NUMLINES):  # Loop through lines
            if len(settings.BOARD[line_number]) > 0:  # If there's something in the line
                second_index = 0
                if len(self.solution[first_index]) == len(settings.BOARD[line_number]):  # If line has correct length
                    for item in self.solution[first_index]:  # Loop through solution list
                        if item == settings.BOARD[line_number][second_index].text:  # Compare solution to board
                            all_good = True
                        else:
                            all_good = False
                            self.debug.debug_on = True
                            self.debug.line_number = line_number
                        second_index += 1

                    first_index += 1
                else:  # Line lengths don't match, return False immediately
                    self.debug.debug_on = True
                    self.debug.line_number = line_number
                    return False
                if not all_good:  # Used for early exit
                    return all_good
            if first_index >= len(self.solution):
                return all_good
        if not all_good:
            self.debug.debug_on = True
        return all_good"""

    @staticmethod
    def create_solution_dicts():
        sol1 = settings.create_blank_dict()
        sol1[1] = ['Toast', 'Bread Slice']
        solution = [sol1]
        return solution
