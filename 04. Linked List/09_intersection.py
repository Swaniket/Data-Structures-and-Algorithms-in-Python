# Given two(singly) linked lists, determine if the two lists intersect. Return the intersecting node.
# Note that the intersection is defined based on reference, not value. That is, if the kth node of
# the first linked list is the exact same node(by reference) as the jth node of the second linked list,
# then they are intersecting.

# INTERSECTING LL
# 3 -> 1 -> 5 -> 9 ->
#                       7 -> 2 -> 1
#      2 -> 4 -> 6 ->

# NON-INTERSECTING LL
# 3 -> 1 -> 5 -> 9 -> 7 -> 2 -> 1
#
#      2 -> 4 -> 6 -> 7 -> 2 -> 1
from GeneralLinkedList import LinkedList, Node

# Helper addition method
def addSameNode(llA, llB, value):
    tempNode = Node(value)

    # Add end of 1st LL
    llA.tail.next = tempNode
    llA.tail = tempNode

    # Add end of 2nd LL
    llB.tail.next = tempNode
    llB.tail = tempNode

# Time Complexity: O(A+B), where A = len(llA), B = len(llB)
# Space Complexity: O(1)
def intersection(llA, llB):
    # In order to intersect, they have to point to the same tail
    if llA.tail is not llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    difference = len(longer) - len(shorter)

    longerNode = longer.head
    shorterNode = shorter.head

    # Ignore the first nodes of the longer list
    for _ in range(difference):
        longerNode = longerNode.next

    # Find the intersection point
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode

if __name__ == "__main__":
    llA = LinkedList()
    llA.generateLL(3, 0, 10)

    llB = LinkedList()
    llB.generateLL(4, 0, 10)

    addSameNode(llA, llB, 11)
    addSameNode(llA, llB, 14)

    print(llA)
    print(llB)

    print(intersection(llA, llB))

    