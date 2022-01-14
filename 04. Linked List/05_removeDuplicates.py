# Write Code to remove duplicates from an unsorted Linked List
from GeneralLinkedList import LinkedList

# Approch #1 - With a Temp Buffer
# Time Complexity: O(n)
# Space Complexity: O(n)
def removeDuplicates(ll):
    if ll.head is None:
        return
    currentNode = ll.head
    visited = set([currentNode.value])
    while currentNode.next:
        # Duplicate - Delete the node
        if currentNode.next.value in visited:
            currentNode.next = currentNode.next.next
        # Not a duplicate - Add to the visited set
        visited.add(currentNode.next.value)
        currentNode = currentNode.next
    return ll
    

# Approch #2 - Without Temp Buffer
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def removeDups(ll):
    if ll.head is None:
        return
    currentNode = ll.head
    while currentNode:
        runner = currentNode
        while runner.next:
            # Duplicate - Delete the node
            if runner.next.value == currentNode.value: # But ll.head doesn't have a value?
                runner.next = runner.next.next
            # Not a duplicate
            else:
                runner = runner.next
        currentNode = currentNode.next
    return ll.head 
    

if __name__ == "__main__":
    customLL = LinkedList()
    customLL.generateLL(10, 0, 99)
    print(customLL)
    # removeDuplicates(customLL)
    removeDups(customLL)
    print(customLL)


# NOTE You can return either the whole LL or only the head of the LL, both are same


