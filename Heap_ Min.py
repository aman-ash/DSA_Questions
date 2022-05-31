class Heap:

    def __init__(self, array):
        #self.heap = [1, 2, 3, 4, 5, 6, 7]
        self.heap = [8, 12, 23, 17, 31, 30, 44, 102, 18]

    def build(self, array):
        pass

    def insert(self, value):
        self.heap.append(value)
        self.shifUp()

    def remove(self):
        pass

    def peek(self):
        pass

    def shifDown(self):
        pass

    def shifUp(self):
        childIdx = len(self.heap) - 1
        parentIdx = (childIdx - 1) // 2

        while parentIdx >= 0 and self.heap[childIdx] < self.heap[parentIdx]:
            self.heap[childIdx], self.heap[parentIdx] = self.heap[parentIdx], self.heap[childIdx]
            childIdx = parentIdx
            parentIdx = (childIdx - 1) // 2


if __name__ == '__main__':
    heap = Heap([])
    print(heap.heap)
    heap.insert(9)
    print(heap.heap)
    heap.insert(0)
    print(heap.heap)
