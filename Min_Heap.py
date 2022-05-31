class MinHeap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def insert(self, data):
        if self.isFull():
            raise ("Storage is full")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp()

    def remove(self):
        if self.size == 0:
            raise ("Storage is empty")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return data

    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.getParentData(index) > self.storage[index]:
            self.swap(self.getParentIdx(index), index)
            index = self.getParentIdx(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallestChildIdx = self.getLeftChildIdx(index)
            if self.hasRightChild(index) and self.getRightChildData(index) < self.getLeftChildData(index):
                smallestChildIdx = self.getRightChildIdx(index)

            if self.storage[index] < self.storage[smallestChildIdx]:
                break
            else:
                self.swap(index, smallestChildIdx)
            index = smallestChildIdx

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    def getParentData(self, index):
        return self.storage[self.getParentIdx(index)]

    def getLeftChildData(self, index):
        return self.storage[self.getLeftChildIdx(index)]

    def getRightChildData(self, index):
        return self.storage[self.getRightChildIdx(index)]

    def hasParent(self, index):
        return self.getParentIdx(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIdx(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIdx(index) < self.size

    def getParentIdx(self, index):
        return (index - 1) // 2

    def getLeftChildIdx(self, index):
        return 2*index + 1

    def getRightChildIdx(self, index):
        return 2*index + 2


if __name__ == '__main__':
    array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
    mh = MinHeap(len(array))
    for a in array:
        mh.insert(a)
    print(mh.storage)
