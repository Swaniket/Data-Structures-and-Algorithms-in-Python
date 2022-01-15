# Write code to partition a linked list around a value x, such that all nodes less 
# than x come before all node greter than or equal to x
from GeneralLinkedList import LinkedList

# Time Complexity: O(n)
# Space Complexity: O(1)
def partition(ll, x):
    currentNode = ll.head
    ll.tail = ll.head

    while currentNode:
        nextNode = currentNode.next
        currentNode.next = None
        # Insert at the beginning
        if currentNode.value < x:
            currentNode.next = ll.head
            ll.head = currentNode
        # Insert at the end of the LL
        else:
            ll.tail.next = currentNode
            ll.tail = currentNode
        currentNode = nextNode

    if ll.tail.next is not None:
        ll.tail.next = None

if __name__ == "__main__":
    customLL = LinkedList()
    customLL.generateLL(10, 0, 99)
    print(customLL)

    partition(customLL, 50)
    print(customLL)