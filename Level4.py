import Level
import Level5
import settings
import Block


class Level4(Level.Level):
    def __init__(self):
        super(Level4, self).__init__()
        # TODO: Implement class
        self.recipeTitle = "Chocolate Chip Cookie Dough"
        self.solutions = self.create_solution_dicts()
        self.next = Level5.Level5

    @staticmethod
    def create_solution_dicts():
        sol1 = settings.create_blank_dict()
        solution = [sol1]
        return solution
