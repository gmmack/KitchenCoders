import Level
import settings
import Block


class Level3(Level.Level):
    def __init__(self):
        super(Level3, self).__init__()
        # TODO: Write level info

    @staticmethod  #TODO: Write real solution
    def create_solution_dicts():
        sol1 = settings.create_blank_dict()
        sol1[1] = ['Toast', 'Bread Slice']
        sol1[2] = ['Butter', 'Bread Slice']
        solution = [sol1]
        return solution
