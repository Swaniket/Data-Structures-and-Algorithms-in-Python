# Implement stack using python lists (w/o size limit)
# This approch will have perfomance issue when the size grows

class Stack:
    def __init__(self) -> None:
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

    # Pushing an element into a stack
    def push(self, value): # Time Complexity -> O(1)
        self.list.append(value)
        return "The Element is insterted!"

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
    customStack = Stack()

    # print(customStack.isEmpty())

    customStack.push(1)
    customStack.push(2)
    customStack.push(3)

    # customStack.pop()
    print(customStack.peek())

    print(customStack)