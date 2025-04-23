from System.Representation.Solution import Solution


class Partial:

    def get_some(self, partial, representation='tree'):
        if representation == 'tree':
            return self.__tree_representation(self.generate(), partial)
        else:
            exit('Please specify the representation type')

    def __tree_representation(self, solution, partial):
        self
        tree = Solution()
        tree.init_from_partial(solution, partial)
        return tree

    def generate(self, partial):
        exit('Please define the <generate> method for your partial')

