class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, element):
        if element == self.data:
            return True
        if element < self.data:
            if self.data:
                return self.left.search(element)
            else:
                return False
        else:
            if self.right:
                return self.right.search(element)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()
        elements.append(self.data)
        return elements

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete_replace_by_right_min(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_replace_by_right_min(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete_replace_by_right_min(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_replace_by_right_min(min_val)

        return self

    def delete_replace_by_left_max(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_replace_by_left_max(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_replace_by_left_max(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete_replace_by_left_max(max_val)

        return self


def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    names = [25, 10, 15, 48, 27, 89, 110, 2, 75]
    t = build_tree(names)
    print(t.in_order_traversal())
    t.delete_replace_by_right_min(48)
    print(t.in_order_traversal())
    t.delete_replace_by_left_max(27)
    # t.delete_replace_by_right_min(48)
    print(t.in_order_traversal())
