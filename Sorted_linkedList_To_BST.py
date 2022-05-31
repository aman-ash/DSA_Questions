class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def create_tree(self, value):
        if value < self.data:
            if self.left is not None:
                self.left = TNode(value)
            else:
                self.left.create_tree(value)
        else:
            if self.right is not None:
                self.right = TNode(value)
            else:
                self.right.create_tree(value)

        return self

    def sortedListToBST(self, array):
        Idx = len(array)//2
        root = array[Idx]
        array.pop(Idx)
        bst = TNode(root)
        for i in range(1, len(array)):
            bst.create_tree(array[i])
        return bst


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    ob = Solution()
    print(ob.sortedListToBST(array))
