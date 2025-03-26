class Partial:

    def get_some(self, representation='tree'):
        solution = self.__generate()
        return self.__tree_representation(solution)

    def __generate(self):
        pass

    def __tree_representation(self, solution):
        pass
