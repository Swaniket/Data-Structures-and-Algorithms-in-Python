# Write down a function that takes a linked list and a data item x as a parameter,
# inserts the data item in a sorted way and returns the head of the linked list

from os import link
from GeneralLinkedList import LinkedList, Node

def sortedInsert(ll, nodeValue): 
    tempNode = Node(nodeValue)
    if ll.head is None:
        return ll.add(tempNode)
    elif nodeValue < ll.head.value:
        tempNode.prev = None
        tempNode.next = ll.head
        ll.head.prev = tempNode
        ll.head = tempNode
        return ll.head
    else:
        currNode = ll.head
        while currNode.next is not None and currNode.next.value < nodeValue:
            currNode = currNode.next
        tempNode.next = currNode.next
        currNode.next = tempNode
        return ll.head

if __name__ == "__main__":
    ll1 = LinkedList()
    sortedInsert(ll1, 5)
    print(ll1)

    ll2 = LinkedList()
    ll2.add(10)
    ll2.add(20)
    ll2.add(30)
    ll2.add(40)
    print(ll2)
    sortedInsert(ll2, 25)
    print(ll2)

    ll3 = LinkedList()
    ll3.add(10)
    ll3.add(25)
    print(ll3)
    sortedInsert(ll3, 5)
    print(ll3)
