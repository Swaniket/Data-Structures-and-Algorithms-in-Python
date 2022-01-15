# Implement an algorithm to find the nth to last element of a Singly Linked List.
from GeneralLinkedList import LinkedList

# Time Complexity: O(n)
# Space Complexity: O(1)
def nthToLast(ll, n):
    walker = ll.head
    runner = ll.head
    # Moving Runner to nth position from start
    for _ in range(n):
        if runner is None:
            return None
        runner = runner.next
    # Moving walker & runner at the same speed till runner reaches the end
    while runner:
        walker = walker.next
        runner = runner.next
    return walker

if __name__ == "__main__":
    customLL = LinkedList()
    customLL.generateLL(10, 0, 99)
    print(customLL)
    
    print(nthToLast(customLL, 3))

