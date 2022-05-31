class MinHeap:
    def __init__(self, array):
        self.heap = [0] * len(array)
        self.size = 0
        self.buildHeap(array)

    def buildHeap(self, array):
        for element in array:
            self.insert(element)
        return self.heap

    def siftDown(self):
        pass

    def siftUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.heap[index] < self.heap[self.getParentIdx(index)]:
            self.swap(index, self.getParentIdx(index))
            index = self.getParentIdx(index)

    def peek(self):
        return self.heap[0]

    def remove(self):
        ans = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.siftDown()
        return ans

    def insert(self, value):
        if self.size == 0:
            self.heap[0] = value
            self.size += 1

        else:
            index = self.size
            self.heap[index] = value
            self.size += 1
            self.siftUp()

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def hasParent(self, index):
        return self.getParentIdx(index) >= 0

    def hasLeftChild(self, index):
        return (2*index) + 1 < self.size

    def hasRightChild(self, index):
        return (2*index) + 2 < self.size

    def getParentIdx(self, index):
        return (index - 1) // 2

    def getLeftChildIdx(self, index):
        return (2 * index) + 1

    def getRightChildIdx(self, index):
        return (2 * index) + 2


if __name__ == '__main__':
    mh = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
    print(mh.heap)
