class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


def Product_tree():
    root = TreeNode("Fav Singers")

    BTS = TreeNode("BTS")
    BTS.add_child(TreeNode("Jungkook"))
    BTS.add_child(TreeNode("Jimin"))
    BTS.add_child(TreeNode("Suga"))
    BTS.add_child(TreeNode("Jin"))
    BTS.add_child(TreeNode("V"))
    BTS.add_child(TreeNode("RM"))
    BTS.add_child(TreeNode("J-Hope"))

    Justin_Bieber = TreeNode("Justin Bieber")

    One_Direction = TreeNode("One Dorection")
    One_Direction.add_child(TreeNode("Harry"))
    One_Direction.add_child(TreeNode("Zayn"))
    One_Direction.add_child(TreeNode("Liam"))
    One_Direction.add_child(TreeNode("Nial"))
    One_Direction.add_child(TreeNode("Louis"))

    root.add_child(BTS)
    root.add_child(Justin_Bieber)
    root.add_child(One_Direction)
    return root


if __name__ == '__main__':
    tree = Product_tree()
    tree.print_tree()
