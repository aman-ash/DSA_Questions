class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data, None)
        itr.next = node

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def Print(self):
        if self.head is None:
            print("LinkedList is Empty")
            return
        llist = ''
        itr = self.head
        while itr:
            llist += str(itr.data) + " --> "
            itr = itr.next
        print(llist)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.Print()
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    ll.insert_at_end(6)
    ll.Print()
    ll.insert_values([7, 8, 9, 10])
    ll.Print()
