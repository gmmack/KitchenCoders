import Level
import settings
import Block


class Level5(Level.Level):
    def __init__(self):
        super(Level5, self).__init__()
        # TODO: Implement class
        self.recipeTitle = "Avocado Toast"
        self.solutions = self.create_solution_dicts()
        # self.next = Level6.Level6
