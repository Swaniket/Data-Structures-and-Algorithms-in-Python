# Write a function which takes head of a LL as an argument, reverses the LL and returns head of the modified LL

# from GeneralLinkedList import LinkedList, Node

# def reverseLL(ll):
#     prevNode = None
#     while ll.head is not None:
#         nextNode = ll.head.next
#         ll.head.next = prevNode
#         prevNode = ll.head
#         ll.head = nextNode
#     return prevNode

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.add(1)
#     ll.add(2)
#     ll.add(3)
#     ll.add(4)
#     ll.add(5)
#     print(ll)
#     reverseLL(ll)
#     print(ll)

class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, nodeValue):
        newNode = Node(nodeValue)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def reverse(self):
        previousNode = None
        currentNode = self.head
        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        self.head = previousNode

if __name__ == "__main__":
    ll = LinkedList()

    ll.push(1)
    ll.push(2)
    ll.push(3)

    ll.printList()

    ll.reverse()

    ll.printList()