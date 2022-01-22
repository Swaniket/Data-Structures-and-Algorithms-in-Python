class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

class Queue:
    def __init__(self) -> None:
        self.linkedList = LinkedList()

    def __str__(self) -> str:
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    # Returns true if the Queue is empty
    def isEmpty(self): # Time Complexity -> O(1)
        if self.linkedList.head is None:
            return True
        return False

    # Insert an element at the end of queue
    def enqueue(self, value): # Time Complexity -> O(1)
        newNode = Node(value)
        # When we don't have any node in the LL
        if self.linkedList.head is None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        # When we already have some nodes
        self.linkedList.tail.next = newNode
        self.linkedList.tail = newNode

    # Delete the first element from the queue
    def dequeue(self): # Time Complexity -> O(1)
        if self.isEmpty():
            return "We don't have any element in the queue"
        else:
            tempNode = self.linkedList.head
            # where there is only 1 node in the ll
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            # More than 1 node
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode

    # Returns the first element of the queue
    def peek(self): # Time Complexity -> O(1)
        if self.isEmpty():
            return "The queue is empty!"
        return self.linkedList.head

    # Delete the whole Queue
    def deleteQueue(self): # Time Complexity -> O(1)
        self.linkedList.head = None
        self.linkedList.tail = None


if __name__ == "__main__":
    customQueue = Queue()

    customQueue.enqueue(1)
    customQueue.enqueue(2)
    customQueue.enqueue(3)

    print(customQueue)

    # print(customQueue.dequeue())
    print(customQueue.peek())

    print(customQueue)