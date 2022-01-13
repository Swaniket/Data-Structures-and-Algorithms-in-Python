class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SLinkedList:
    # Constructor
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # Make the class iterable
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Traversal of LL 
    def traverseLL(self): # Time Complexity -> O(n)
        if self.head is None:
            print("The Linked List doesn't exists")

        current = self.head
        while(current):
            print(current.value)
            current = current.next

    # Insert at the start, middle and at the end of LL
    def insertSLL(self, value, location): # Time Complexity -> O(n)
        newNode = Node(value)

        # When the LL is empty
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            # Insert at the start
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            # Insert at the end of LL
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            # Insert at any location in the middle
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    # Searchs for a value in LL
    def searchLL(self, value): # Time Complexity -> O(n)
        if self.head is None:
            print("The Linked List doesn't exists")
        
        current = self.head
        while(current):
            if current.value == value:
                print("Element Found")
                return current.value            
            current = current.next 
        return "The Element Does not exists"

    # Delete a node from LL(start, middle, end)
    def deleteNode(self, location): # Time Complexity -> O(n)
        if self.head is None:
            print("The Linkedlist does not exists")
        # Delete first node from LL
        if location == 0:
            # We have only 1 node in LL
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # More than 1 node
            else:
                self.head = self.head.next
        # Delete last node from LL
        elif location == 1:
            # We have only 1 node in LL
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # More than 1 node
            else:
                node = self.head
                while node is not None:
                    # Finding the node before the last node
                    if node.next == self.tail:
                        break
                    node = node.next 
                node.next = None
                self.tail = node
        # Delete from middle of the LL
        else:
            tempNode = self.head
            index = 0
            # Travarse to the node before the node we want to delete
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next

    # Deletes the Entire Linked list
    def deleteEntireLL(self): # Time Complexity -> O(1)
        if self.head is None:
            print("The Linked list doesn't exists")
        self.head = None
        self.tail = None
        

if __name__ == "__main__":
    singlyLinkedList = SLinkedList()

    singlyLinkedList.insertSLL(10,1)
    singlyLinkedList.insertSLL(20,1)
    singlyLinkedList.insertSLL(30,1)
    singlyLinkedList.insertSLL(40,1)


    singlyLinkedList.insertSLL(00,0)

    singlyLinkedList.insertSLL(00,2)

    print([node.value for node in singlyLinkedList])
    # singlyLinkedList.traverseLL()
    # print(singlyLinkedList.searchLL(40))
    # singlyLinkedList.deleteNode(2)
    singlyLinkedList.deleteEntireLL()
    print([node.value for node in singlyLinkedList])



