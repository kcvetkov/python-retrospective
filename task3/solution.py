class Person(object):
    def __init__(self, name, birth_year, gender, father=None, mother=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.father = father
        self.mother = mother
        self.create_successors()
        self.create_siblings()
        self.inform_parents()
        self.inform_siblings()

    def create_successors(self):
        self.sons_and_daughters = {'F': [], 'M': []}

    def create_siblings(self):
        self.siblings = {'F': [], 'M': []}

    def inform_parents(self):
        if not self.father is None:
            self.father.add_child(self)
        if not self.mother is None:
            self.mother.add_child(self)

    def add_child(self, child):
        self.sons_and_daughters[child.gender].append(child)

    def inform_siblings(self):
        if not self.father is None:
            self.inform_siblings_on_parents_side(self.father)
            return
        if not self.mother is None:
            self.inform_siblings_on_parents_side(self.mother)
            return

    def inform_siblings_on_parents_side(self, parent):
        for daughter in parent.sons_and_daughters['F']:
                if not daughter is self:
                    daughter.siblings[self.gender].append(self)
                    self.add_sibling(daughter)
        for son in parent.sons_and_daughters['M']:
                if not son is self:
                    son.siblings[self.gender].append(self)
                    self.add_sibling(son)

    def add_sibling(self, sibling):
        self.siblings[sibling.gender].append(sibling)

    def get_brothers(self):
        return self.siblings['M']

    def get_sisters(self):
        return self.siblings['F']

    def children(self, gender=None):
        if gender is None:
            return self.sons_and_daughters['F'] + self.sons_and_daughters['M']
        else:
            return self.sons_and_daughters[gender]

    def is_direct_successor(self, successor):
        if successor in self.sons_and_daughters[successor.gender]:
            return True
        else:
            return False
