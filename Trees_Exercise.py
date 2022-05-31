class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, method):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if method == "n":
            print(prefix + self.name)
            if self.children:
                for child in self.children:
                    child.print_tree("n")
        if method == "d":
            print(prefix + self.designation)
            if self.children:
                for child in self.children:
                    child.print_tree("d")
        if method == "b":
            print(prefix + self.name + " "+"(" + self.designation + ")")
            for child in self.children:
                child.print_tree("b")

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


def product_tree():
    root = TreeNode("NilUpul", "CEO")
    cto = TreeNode("Tanmry", "CTO")
    hr = TreeNode("ALi", "HR")
    root.add_child(cto)
    root.add_child(hr)
    return root


if __name__ == '__main__':
    t = product_tree()
    method = input(''' what you want to print :
    
    enter 'n' for name
    enter 'd' for designation
    enter 'b' for both

    : ''')

    t.print_tree(method)
