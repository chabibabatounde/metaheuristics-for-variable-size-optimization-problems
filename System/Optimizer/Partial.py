from System.Representation.Solution import Solution


class Partial:

    def get_some(self, representation='tree'):
        if representation == 'tree':
            return self.__tree_representation(self.generate())
        else:
            exit('Please specify the representation type')

    def __tree_representation(self, solution):
        exit(solution)
        tree = Solution()
        return tree

    def generate(self):
        exit('Please define the <generate> method for your partial')
