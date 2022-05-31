from collections import deque


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.buffer)
    q.dequeue()
    print(q.buffer)
    print(q.dequeue())
    print(q.size())
    print(q.is_empty())
