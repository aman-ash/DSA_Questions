from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == '__main__':
    st = Stack()
    st.push(5)
    st.push(4)
    st.push(3)
    st.push(2)
    st.push(1)
    print(st.container)
    print(st.is_empty())
    print(st.size())
    print(st.peek())
    st.pop()
    st.pop()
    print(st.container)
    print(st.is_empty())
    print(st.size())
    print(st.peek())
