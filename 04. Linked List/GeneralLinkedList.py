from random import randint

class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None
        self.prev = None

    # To print the node: __str__ returns string representation of any given object
    def __str__(self) -> str:
        return str(self.value)

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # Making the Linked List iterable
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

    # To return a string representation of LL
    def __str__(self) -> str:
        values = [str(x.value) for x in self] 
        return ' -> '.join(values)

    # To return the length of the LL
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    # Insert to the end of LL
    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    # Generate LL based on random numbers
    def generateLL(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self

# if __name__ == "__main__":
#     customLL = LinkedList()
#     customLL.generateLL(10, 0, 99)
#     print(customLL)
#     print(len(customLL))