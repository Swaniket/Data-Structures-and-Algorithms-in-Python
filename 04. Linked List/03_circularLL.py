class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class CircularSinglyLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
            
    # Create CircularLL
    def createLL(self, nodevalue): # Time Complexity -> O(1)
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = node
        return "The LL has been created"

    # Insert (Start, End & Middle)
    def insertLL(self, nodeValue, location): # Time Complexity -> O(n)
        if self.head is None:
            return "The head referance is None"
        newNode = Node(nodeValue)
        # Insert at the Start
        if location == 0:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
        # Insert at the end
        elif location == 1:
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode
        # Insert at the middle
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = newNode
            newNode.next = nextNode
        return "Then node has been successfully inserted"

    # Travarse the circular LL
    def travarseLL(self): # Time Complexity -> O(n)
        if self.head is None:
            print("Head doesn't exists") 
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.next
            if tempNode == self.tail.next:
                break

    # Searching in CLL
    def searchLL(self, nodeValue): # Time Complexity -> O(n)
        if self.head is None:
            return "There is no node in this CLL"
        tempNode = self.head
        while tempNode:
            if tempNode.value == nodeValue:
                return tempNode.value
            tempNode = tempNode.next
            if tempNode == self.tail.next:
                return "This node doesn't exists"

    # Delete in CLL(Start, End & Middle)
    def deleteNode(self, location): # Time Complexity -> O(n)
        if self.head is None:
            print("There is no element in the CLL")
        # Delete from the start
        if location == 0:
            # Only 1 element
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            # More than 1 element
            else:
                self.head = self.head.next
                self.tail.next = self.head
        # Delete from the end
        elif location == 1:
            # Only 1 element
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            # More than 1 element
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = self.head
                self.tail = node
        # Delete from middle
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next

    # Delete the entire LL
    def deleteLL(self): # Time Complexity -> O(1)
        self.head = None
        self.tail.next = None
        self.tail = None



if __name__ == "__main__":
    ll = CircularSinglyLL()

    ll.createLL(10)
    ll.insertLL(0,0)
    ll.insertLL(2,1)
    ll.insertLL(3,1)
    ll.insertLL(2,2)

    print([node.value for node in ll])

    # ll.travarseLL()
    # print(ll.searchLL(5))

    # ll.deleteNode(0)
    ll.deleteLL()

    print([node.value for node in ll])
        