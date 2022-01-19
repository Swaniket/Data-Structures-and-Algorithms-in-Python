from platform import node


class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # To make the LL iterable
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

class Stack:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    # Makes the stack printable
    def __str__(self) -> str:
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self): # Time Complexity -> O(1)
        if self.LinkedList.head == None:
            return True
        return False

    def push(self, value): # Time Complexity -> O(1)
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self): # Time Complexity -> O(1)
        if self.isEmpty():
            return "There is no element in the stack!"
        nodeValue = self.LinkedList.head.value
        self.LinkedList.head = self.LinkedList.head.next
        return nodeValue

    def peek(self): # Time Complexity -> O(1)
        if self.isEmpty():
            return "There is no element in the stack!"
        nodeValue = self.LinkedList.head.value
        return nodeValue

    def deleteStack(self): # Time Complexity -> O(1)
        self.LinkedList.head = None


if __name__ == "__main__":
    customStack = Stack()

    customStack.push(1)
    customStack.push(2)
    customStack.push(3)
    # print(customStack)

    # customStack.pop()
    # print(customStack)

    print(customStack.peek())

    # print(customStack.isEmpty())