# Implement stack using python lists (with size limit)

class Stack:
    def __init__(self, maxSize) -> None:
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # Check if the stack is empty
    def isEmpty(self): # Time Complexity -> O(1)
        if self.list == []:
            return True
        return False

    # Check if the stack is full (because we have a size limit)
    def isFull(self): # Time Complexity -> O(1)
        if len(self.list) == self.maxSize:
            return True
        return False

    # Push
    def push(self, value): # Time Complexity -> O(1) / O(n^2)
        if self.isFull():
            return "The Stack is full!"
        self.list.append(value)
        return "The element is successfully inserted"

    # Pop method
    def pop(self): # Time Complexity -> O(1)
        if self.isEmpty():
            return "There is no element in the stack"
        return self.list.pop()

    # Peek method
    def peek(self): # Time Complexity -> O(1)
        if self.isEmpty():
            return "There is no element in the stack"
        return self.list[-1]

    # Delete entire stack
    def deleteStack(self): # Time Complexity -> O(1)
        self.list = None

if __name__ == "__main__":
    customStack = Stack(4)

    print(customStack.isEmpty())
    print(customStack.isFull())

    customStack.push(1)
    customStack.push(2)
    customStack.push(3)
    customStack.push(4)
    # print(customStack.push(5))

    print(customStack)