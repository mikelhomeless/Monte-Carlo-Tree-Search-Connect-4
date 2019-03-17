class UnionFind:
    def __init__(self, size):
        self.size = size
        self.data = [-1] * self.size

    def union(self, n1, n2):
        # Find parent nodes
        # Find min tree size
        # add sizes together - > set value to largest parent
        # have smallest parent point to parent
        # return equivalency set size
        n1_size, n1_parent = self.find(n1)
        n2_size, n2_parent = self.find(n2)
        min_indx, max_indx = self.min_max_parent_size(n1_size, n1_parent, n2_size, n2_parent)
        self.data[max_indx] = n1_size + n2_size
        self.data[min_indx] = max_indx
        return self.data[max_indx]

    # returns size of the equivalency set and parent node index
    def find(self, n):
        while self.data[n] >= 0:
            n = self.data[n]
        return self.data[n], n

    def min_max_parent_size(self, n1_size, n1_indx, n2_size, n2_indx):
        if n1_size <= n2_size:
            return n2_indx, n1_indx
        else:
            return n1_indx, n2_indx

class Player:
    def __init__(self):
        pass()
    # Has a union find for equivalency sets of linearly adjacent cells

    def take_turn(self):
        pass()

class Agent(Player):
    # has a search depth variable
    # has a structure for keeping track of data from the monte carlo search
    def __init__(self):
        pass()
