# Design a stack where in addition to push & pop method, has a function called min which
# returns the minimum element. Push & Pop & Min should all operate in O(1)

# We can't use list for this problem because lists will have a O(n) for push
# That's why we need to use a linked list

# How it will work? 

# push(5), min() -> 5
# push(6), min() -> 5
# push(3), min() -> 3
# push(7), min() -> 3

# pop(), min() -> 3
# pop(), min() -> 5
# pop(), min() -> 5

class Node:
    def __init__(self, value = None, next = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        string = str(self.value)
        if self.next:
            string += ',' + str(self.next)
        return string

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.minNode = None

    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value

    def push(self, item):
        # When value of min node is less than item - min node stays the same
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node(value = self.minNode.value, next = self.minNode)
        # Else add the new node as the min node
        else:
            self.minNode = Node(value = item, next = self.minNode)
        # At the end add the new value at the top of the stack
        self.top = Node(value = item, next = self.top)

    def pop(self):
        if not self.top:
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        # Delete the value from the start of the LL
        self.top = self.top.next
        return item

if __name__ == "__main__":
    customStack = Stack()

    customStack.push(5)
    print(customStack.min())

    customStack.push(6)
    print(customStack.min())

    customStack.push(3)
    print(customStack.min())
    
    customStack.pop()
    print(customStack.min())
