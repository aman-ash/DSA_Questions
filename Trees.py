class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 2
        prefix = spaces + "|___" if self.parent else""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Windows"))
    laptop.add_child(TreeNode("Linux"))

    phone = TreeNode("phone")
    phone.add_child(TreeNode("iphone"))
    phone.add_child(TreeNode("Android"))
    phone.add_child(TreeNode("Vivo"))

    tv = TreeNode("tv")
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
