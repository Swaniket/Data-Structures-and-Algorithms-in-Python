class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Create Doubly Linked List
    def createDLL(self, nodeValue): # Time Complexity -> O(1)
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The DLL is created successfully!"

    # Insert a node (Start, Middle, End)
    def insertNode(self, nodeValue, location): # Time Complexity -> O(n)
        if self.head is None:
            print("The head referance is empty")
        newNode = Node(nodeValue)
        # Insert at the start
        if location == 0:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        # Insert at the end
        elif location == 1:
            newNode.next = None
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        # Insert at any position
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            newNode.next = tempNode.next
            newNode.prev = tempNode
            newNode.next.prev = newNode
            tempNode.next = newNode

    # Travarse the Linked List
    def travarseLL(self): # Time Complexity -> O(n)
        if self.head is None:
            print("There is no elements in the list")
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.next

    # Travarsal in reverse order
    def reverseTraverseLL(self): # Time Complexity -> O(n)
        if self.head is None:
            print("There is no element in the Linked List")
        tempNode = self.tail
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.prev

    # Search in Doubly Linked List
    def searchLL(self, nodeValue): # Time Complexity -> O(n)
        if self.head is None:
            print("There is no element in the Linked List")
        tempNode = self.head
        while tempNode:
            if tempNode.value == nodeValue:
                return tempNode.value
            tempNode = tempNode.next
        return "The node doesn't exists in the list"

    # Delete Node from DLL (Start, End, Middle)
    def deleteNode(self, location): # Time Complexity -> O(n)
        if self.head is None:
            print("There is no element in DLL")
        # Delete from the start
        if location == 0:
            # When only 1 node in DLL
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # More than 1 Node
            else:
                self.head = self.head.next
                self.head.prev = None
        # Delete from the end
        elif location == 1:
            # Only 1 node
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # More than 1 node
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        # Delete from any given location
        else:
            currNode = self.head
            index = 0
            while index < location - 1:
                currNode = currNode.next
                index += 1
            currNode.next = currNode.next.next
            currNode.next.prev = currNode
        print("The node has been successfully deleted")

    # Delete the whole DLL
    def deleteList(self): # Time Complexity -> O(n)
        if self.head is None:
            print("There is no node in DLL")
        tempNode = self.head
        while tempNode:
            tempNode.prev = None
            tempNode = tempNode.next
        self.head = None
        self.tail = None
        print("The DLL has been successfully deleted")


if __name__ == "__main__":
    ll = DoublyLinkedList()

    print(ll.createDLL(5))
    ll.insertNode(0,0)
    ll.insertNode(2,1)
    ll.insertNode(3,2)

    # ll.travarseLL()
    # ll.reverseTraverseLL()

    print([node.value for node in ll])

    # ll.deleteNode(-1)
    ll.deleteList()
    # print(ll.searchLL(7))

    print([node.value for node in ll])

